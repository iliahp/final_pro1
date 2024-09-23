def entity_maker(class_name, fields_list):
    file = open(class_name.lower() + ".py", "wt")
    file.write(f"class {class_name}:\n")
    file.write(f"\tdef __init__(self, {', '.join(fields_list)}):\n")
    for field in fields_list:
        file.write(f"\t\tself.{field} = {field}\n")

    file.write("\n")

    for field in fields_list:
        file.write("\t@property\n")
        file.write(f"\tdef {field}(self):\n")
        file.write(f"\t\treturn self._{field}\n")
        file.write("\n")

        file.write(f"\t@{field}.setter\n")
        file.write(f"\tdef {field}(self, {field}):\n")
        file.write("\t\t#todo : Add Validator\n")
        file.write(f"\t\tself._{field} = {field}\n")
        file.write("\n")
    file.write("\tdef __repr__(self):\n\t\treturn f\"{self.__dict__}\"\n")
    file.close()


def da_maker(class_name, fields_list):
    file = open(f"{class_name.lower()}_da" + ".py", "wt")
    file.write(f"import mysql.connector\n")
    file.write("\n")
    file.write(f"from {class_name.lower()} import {class_name}\n")
    file.write("\n")
    file.write(f"class {class_name}Da:\n")
    file.write("\n")
    file.write("\tdef connect(self):\n")
    file.write("\t\tself.connection = mysql.connector.connect(host=\"localhost\", user=\"root\", password=\"root123\", database=\"mft\")\n")
    file.write("\t\tself.cursor = self.connection.cursor()\n")
    file.write("\n")
    file.write("\tdef disconnect(self, commit=False):\n")
    file.write("\t\tif commit:\n")
    file.write("\t\t\tself.connection.commit()\n")
    file.write("\t\tself.cursor.close()\n")
    file.write("\t\tself.connection.close()\n")
    file.write("\n")
    file.write(f"\tdef save(self, {class_name.lower()}):\n")
    file.write(f"\t\tself.connect()\n")
    file.write(f"\t\t#todo : complete sql command and parameters\n")
    file.write(f"\t\tself.cursor.execute(\"insert into {class_name.lower()}_tbl () values ()\",[])\n")
    file.write(f"\t\tself.disconnect(commit = True)\n")
    file.write("\n")
    file.write(f"\tdef edit(self, {class_name.lower()}):\n")
    file.write(f"\t\tself.connect()\n")
    file.write(f"\t\t#todo : complete sql command and parameters\n")
    file.write(f"\t\tself.cursor.execute(\"update {class_name.lower()}_tbl set    where id=%s\",[])\n")
    file.write(f"\t\tself.disconnect(commit = True)\n")
    file.write("\n")
    file.write(f"\tdef remove(self, id):\n")
    file.write(f"\t\tself.connect()\n")
    file.write(f"\t\tself.cursor.execute(\"delete from {class_name.lower()}_tbl where id=%s\",[id])\n")
    file.write(f"\t\tself.disconnect(commit = True)\n")
    file.write("\n")
    file.write(f"\tdef find_all(self):\n")
    file.write(f"\t\tself.connect()\n")
    file.write(f"\t\tself.cursor.execute(\"select * from {class_name.lower()}_tbl \")\n")
    file.write(f"\t\t{class_name.lower()}_list = [{class_name}(*{class_name.lower()}) for {class_name.lower()} in self.cursor.fetchall()]\n")
    file.write(f"\t\tself.disconnect()\n")
    file.write(f"\t\tif {class_name.lower()}_list:\n")
    file.write(f"\t\t\treturn {class_name.lower()}_list\n")
    file.write("\n")
    file.write(f"\tdef find_by_id(self, id):\n")
    file.write(f"\t\tself.connect()\n")
    file.write(f"\t\tself.cursor.execute(\"select * from {class_name.lower()}_tbl where id=%s\", [id])\n")
    file.write(f"\t\t{class_name.lower()} = self.cursor.fetchone()\n")
    file.write(f"\t\tself.disconnect()\n")
    file.write(f"\t\tif {class_name.lower()}:\n")
    file.write(f"\t\t\treturn {class_name}(*{class_name.lower()})\n")
    file.write("\n")
    file.close()
