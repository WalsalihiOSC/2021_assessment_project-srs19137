import tkinter as tk
from tkinter import messagebox
import math

class User:
    def __init__(self, first_name, age, mathmethod):
        self.first_name = first_name  
        self.age = age
        self.mathmethod = mathmethod

    def file_write():
        user_file = open("user_results_file.text", "a")
        user_file.write("Begin User File\n")
        user_file.write(f'User First Name: {root.player.first_name} \nUser Age: {root.player.age} \nChosen question type: {root.player.mathmethod}\n')
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
        tk.Label(self.LoginPageFrame, text='Login Screen').grid()
        tk.Label(self.LoginPageFrame, text='First Name:').grid()
        self.fnameEntry = tk.Entry(self.LoginPageFrame)
        self.fnameEntry.grid()
        tk.Label(self.LoginPageFrame, text='Age:').grid()
        self.ageEntry = tk.Entry(self.LoginPageFrame)
        self.ageEntry.grid()
        tk.Button(self.LoginPageFrame, text='Go to Level Select', command=lambda: self.nextl()).grid()

    def nextl(self):
        if len(self.fnameEntry.get()) == 0:
            tk.messagebox.showwarning('Name Error', 'Please enter your name')
        elif len(self.ageEntry.get()) == 0:
            tk.messagebox.showwarning('Age Error', 'Please enter your age')
        elif len(self.ageEntry.get()) > 0:
            try:
                ageInt = int(self.ageEntry.get())
                if ageInt == 0:
                    tk.messagebox.showwarning('Age Entry Error', 'Are you sure you typed your age correctly?')
                else:
                    self.player = User(self.fnameEntry.get(), self.ageEntry.get(), True)
                    self.LoginPage.destroy()
                    self.LevelSelect()
            except (TypeError, ValueError):
                tk.messagebox.showwarning('Age Entry Error', 'Please enter your age in numbers')

    def LevelSelect(self):
        self.LevelSelectFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LevelSelectFrame.grid()
        tk.Label(self.LevelSelectFrame, text='Level Select').grid()
        self.amount=tk.Entry(self.LevelSelectFrame)
        self.amount.grid()
        self.CHOICES = ['Addition', 'Subtraction', 'Multiplication', 'Division']
        self.chosen_option = StringVar(self.LevelSelectFrame)
        self.chosen_option.set('Choose')
        self.dropdown = tk.OptionMenu(self.LevelSelectFrame, self.chosen_option, *self.CHOICES)
        self.dropdown.grid()        
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
        tk.Label(self.QuestionsFrame, text='Questions').grid()
        tk.Button(self.QuestionsFrame, text='Go to Results Screen', command=lambda: self.nextr()).grid()
    
    def nextr(self):
        self.ResultsScreen()
        self.QuestionsFrame.destroy()

    def ResultsScreen(self):
        self.ResultsScreenFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.ResultsScreenFrame.grid()
        self.ResultsScreenFrame
        tk.Label(self.ResultsScreenFrame, text='Results').grid()
        tk.Button(self.ResultsScreenFrame, text='Go to Login', command=lambda: self.LoginPage()).grid()
    
    def restart(self):
        self.LoginPage()
        self.ResultsScreenFrame.destroy()


root = root()
root.title("Maths-sistant")
root.geometry("380x140")
root.mainloop()