import tkinter
from tkinter import *
from tkinter import messagebox as msg
from view.component import *


class LoginWindow():
    def __init__(self):
        self.win = tkinter.Tk()
        self.win.title("login")
        self.win.geometry("500x500")

        self.win.mainloop()


