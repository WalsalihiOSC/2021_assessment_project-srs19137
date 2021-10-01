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
        self.frame_container.grid()
        self.LoginPage()

    def LoginPage(self):
        self.LoginPageFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LoginPageFrame.grid()
        tk.Label(self.LoginPageFrame, text='Login Screen').grid(padx=10,pady=10)
        tk.Label(self.LoginPageFrame, text='First Name:').grid()
        self.fnameEntry = tk.Entry(self.LoginPageFrame)
        self.fnameEntry.grid()
        tk.Label(self.LoginPageFrame, text='Age:').grid()
        self.ageEntry = tk.Entry(self.LoginPageFrame)
        self.ageEntry.grid()
        tk.Button(self.LoginPageFrame, text='Go to Level Select', command=lambda: self.nextl()).grid()

    def nextl(self):
        first_name=self.fnameEntry.get()
        age=self.ageEntry.get()
        self.player = User(first_name, age)
        self.LevelSelect()
        self.LoginPageFrame.destroy()

    def LevelSelect(self):
        self.LevelSelectFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LevelSelectFrame.grid()
        tk.Label(self.LevelSelectFrame, text='Level Select').grid(padx=10,pady=10)
        self.level=tk.Entry(self.LevelSelectFrame)
        self.level.grid()
        tk.Button(self.LevelSelectFrame, text='Go to Questions', command=lambda: self.nextq()).grid()


    def nextq(self):
        self.player.checklevel(self.level.get(), True)
        if self.player.verify == False:
            tk.messagebox.showwarning(title='ERROR!', message=self.player.errormessage)
        else:
            self.Questions()
            self.LevelSelectFrame.destroy()

    def Questions(self):
        self.QuestionsFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.QuestionsFrame.grid()
        tk.Label(self.QuestionsFrame, text='Questions').grid(padx=10,pady=10)
        tk.Button(self.QuestionsFrame, text='Go to Results Screen', command=lambda: self.nextr()).grid()
    
    def nextr(self):
        self.ResultsScreen()
        self.QuestionsFrame.destroy()

    def ResultsScreen(self):
        self.ResultsScreenFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.ResultsScreenFrame.grid()
        self.ResultsScreenFrame
        tk.Label(self.ResultsScreenFrame, text='Results').grid(padx=10,pady=10)
        tk.Button(self.ResultsScreenFrame, text='Go to Login', command=lambda: self.LoginPage()).grid()
    
    def restart(self):
        self.LoginPage()
        self.ResultsScreenFrame.destroy()


root = root()
root.title("Maths-sistant")
root.geometry("380x140")
root.mainloop()