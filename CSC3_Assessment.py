import tkinter as tk
from tkinter import messagebox
import math

class User:
    def __init__(self, first_name, age):
        self.first_name=first_name  
        self.age=age
        print(f'name from login: {first_name}')
        print(f'age from login: {age}')

    def file_write():
        user_file = open("user_results_file.text", "a")
        user_file.write("Begin User File\n")
        user_file.write(f'User First Name: {User.first_name} \nUser Age: {User.age} \n')
        user_file.write("End User File\n")
        user_file.close()

    def check_question_amount(self, amount, verify):
        self.verify = verify
        try:
            pamount = int(amount)
            if pamount > 0:
                return pamount
        except:
            self.errormessage = 'Error: Not an Integer'
            self.verify = False
        else:
            self.errormessage = 'Error: Input is a negative'
            self.verify = False


class root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(side='top',fill='both',expand=True)
        self.LoginPage()

    def LoginPage(self):
        self.LoginPage = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LoginPage.pack()
        tk.Label(self.LoginPage, text='Login Screen').pack(padx=10,pady=10)
        tk.Label(self.LoginPage, text='First Name:').pack()
        self.fnameEntry = tk.Entry(self.LoginPage)
        self.fnameEntry.pack()
        tk.Label(self.LoginPage, text='Age:').pack()
        self.ageEntry = tk.Entry(self.LoginPage)
        self.ageEntry.pack()
        tk.Button(self.LoginPage, text='Go to Level Select', command=lambda: self.nextw()).pack()

    def nextw(self):
        first_name=self.fnameEntry.get()
        age=self.ageEntry.get()
        self.player = User(first_name, age)
        self.LevelSelect()
        self.LoginPage.forget()

    def LevelSelect(self):
        self.LevelSelect = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LevelSelect.pack()
        tk.Label(self.LevelSelect, text='Level Select').pack(padx=10,pady=10)
        self.level=tk.Entry(self.LevelSelect)
        self.level.pack()
        tk.Button(self.LevelSelect, text='Go to Questions', command=lambda: self.nextq()).pack()


    def nextq(self):
        self.player.checklevel(self.level.get(), True)
        if self.player.verify == False:
            tk.messagebox.showwarning(title='ERROR!', message=self.player.errormessage)
        else:
            self.Questions()
            self.LevelSelect.forget()

    def Questions(self):
        self.Questions = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.Questions.pack()
        tk.Label(self.Questions, text='Questions').pack(padx=10,pady=10)
        tk.Button(self.Questions, text='Go to Results Screen', command=lambda: self.nextr()).pack()
    
    def nextr(self):
        self.ResultsScreen()
        self.Questions.forget()

    def ResultsScreen(self):
        self.ResultsScreen = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.ResultsScreen.pack()
        tk.Label(self.ResultsScreen, text='Results').pack(padx=10,pady=10)
        tk.Button(self.ResultsScreen, text='Go to Login', command=lambda: self.LoginPage()).pack()
    
    def restart(self):
        self.LoginPage()
        self.ResultsScreen.forget()


root = root()
root.title("Maths-sistant")
root.geometry("380x140")
root.mainloop()