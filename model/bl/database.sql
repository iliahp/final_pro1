create database mft;

create table mft.teacher
(
    id           int primary key auto_increment,
    name         varchar(20),
    family       varchar(20),
    national_id  varchar(10),
    birthday     datetime,
    phone_number varchar(11),
    salary       int,
    study        varchar(20),
    skill        varchar(20)

);

create table mft.student
(
    id           int primary key auto_increment,
    name         varchar(20),
    family       varchar(20),
    national_id  varchar(10),
    birthday     datetime,
    phone_number varchar(11),
    grade        int

);

create table mft.course
(
    id         int primary key auto_increment,
    teacher_id int,
    title      varchar(20),
    grade      int,
    department varchar(20)

);

create table mft.select_course
(
    id         int primary key auto_increment,
    course_id  int,
    student_id int,
    date_time  datetime,
    score      int
);


create table mft.payment
(
    id               int primary key auto_increment,
    select_course_id int,
    amount           int,
    description      varchar(20)


)


