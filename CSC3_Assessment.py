import tkinter as tk
from tkinter import StringVar, messagebox
import random
from tkinter.constants import DISABLED

class User:
    def __init__(self, first_name, age, mathmethod, current_score):
        self.first_name = first_name  
        self.age = age
        self.mathmethod = mathmethod
        self.current_score = current_score

    def file_write():
        user_file = open("user_results_file.text", "a")
        user_file.write("Begin User File\n")
        user_file.write(f'User First Name: {root.player.first_name} \nUser Age: {root.player.age} \nChosen question type: {root.player.mathmethod}\n')
        user_file.write(f'Correct Questions: {root.player.current_score} / {root.q_number}\n')
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
        self.LoginPageFrame.grid_propagate(False)
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
                    self.player = User(self.fnameEntry.get(), self.ageEntry.get(), True, int(0))
                    self.LoginPageFrame.destroy()
                    self.LevelSelect()
            except (TypeError, ValueError):
                tk.messagebox.showwarning('Age Entry Error', 'Please enter your age in numbers')

    def LevelSelect(self):
        self.LevelSelectFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.LevelSelectFrame.grid()
        self.LevelSelectFrame.grid_propagate(False)
        tk.Label(self.LevelSelectFrame, text='Level Select').grid()
        tk.Label(self.LevelSelectFrame, text='Number of questions: ').grid()
        self.amount=tk.Entry(self.LevelSelectFrame)
        self.amount.grid()
        self.CHOICES = ['Addition', 'Subtraction', 'Multiplication']
        self.chosen_option = StringVar(self.LevelSelectFrame)
        self.chosen_option.set('Choose')
        tk.Label(self.LevelSelectFrame, text='Type of questions').grid()
        self.dropdown = tk.OptionMenu(self.LevelSelectFrame, self.chosen_option, *self.CHOICES)
        self.dropdown.grid()        
        tk.Button(self.LevelSelectFrame, text='Go to Questions', command=lambda: self.nextq()).grid()

    def nextq(self):
        self.player.check_question_amount(self.amount.get(), True)
        self.q_number = int(self.amount.get())
        if self.player.verify == True:
            if self.chosen_option.get() == 'Choose':
                tk.messagebox.showwarning('Method Select Error', 'Choose a question type using the dropdown menu')
            else:
                self.player = User(self.player.first_name, self.player.age, self.chosen_option.get(), int(0))
                self.Questions()
                self.LevelSelectFrame.destroy()
        else:
            tk.messagebox.showwarning(None, self.player.errormessage)        

    def Questions(self):
        self.QuestionsFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.QuestionsFrame.grid()
        self.QuestionsFrame.grid_propagate(False)
        self.question_create()
        self.question_window()

    def question_window(self):
        tk.Label(self.QuestionsFrame, text='Questions').grid()
        self.question_create()
        tk.Label(self.QuestionsFrame, text=f'{self.num1} {self.operator} {self.num2}').grid()
        self.answerEntry = tk.Entry(self.QuestionsFrame)
        self.answerEntry.grid()
        tk.Label(self.QuestionsFrame, text=f'{self.player.current_score} / {self.q_number} questions completed').grid()
        tk.Button(self.QuestionsFrame, text='Check Answer', command=lambda: self.answer_check(self.answerEntry.get())).grid()

    def finished_window(self):
        self.QuestionsFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.QuestionsFrame.grid()
        self.QuestionsFrame.grid_propagate(False)        
        tk.Label(self.QuestionsFrame, text='Questions').grid()
        tk.Label(self.QuestionsFrame, text=f'{self.num1} {self.operator} {self.num2}').grid()
        self.answerEntry = tk.Entry(self.QuestionsFrame, state=DISABLED, disabledbackground='#D3D3D3')
        self.answerEntry.grid(row=1, column=1)
        tk.Label(self.QuestionsFrame, text=f'{self.player.current_score} / {self.q_number} questions completed').grid()
        tk.Button(self.QuestionsFrame, text='Continue', command=lambda: self.nextr()).grid() 

    def question_create(self):
        self.num1 = random.randint(0,30)
        self.num2 = random.randint(0,30)
        if self.player.mathmethod == 'Addition':
            self.operator = '+'
        elif self.player.mathmethod == 'Subtraction':
            if self.num1 < self.num2:
                numPH = self.num2
                self.num2 = self.num1
                self.num1 = numPH
            self.operator = '-'
        else:
            self.operator = 'x'

    def correct_answer(self):
        if self.player.mathmethod == 'Addition':
            return self.num1 + self.num2
        elif self.player.mathmethod == 'Subtraction':
            return self.num1 - self.num2
        else:
            return self.num1 * self.num2

    def answer_check(self, answervar):        
        if answervar == str(self.correct_answer()):
            self.player.current_score += 1
            self.QuestionsFrame.destroy()
            if self.player.current_score >= self.q_number:
                self.finished_window()
            else:
                self.Questions()
            print(self.player.current_score)
        elif answervar != str(self.correct_answer()):
            self.QuestionsFrame.destroy()
            self.Questions()
            self.answerEntry.insert(0,'INCORRECT')

    def nextr(self):
        self.ResultsScreen()
        self.QuestionsFrame.destroy()

    def ResultsScreen(self):
        self.ResultsScreenFrame = tk.Frame(self.frame_container, width=380, height=140, bg='#ADD8E6')
        self.ResultsScreenFrame.grid()
        self.ResultsScreenFrame.grid_propagate(False)
        tk.Label(self.ResultsScreenFrame, text='Results').grid()
        tk.Button(self.ResultsScreenFrame, text='Go to Login', command=lambda: self.LoginPage()).grid()
        tk.Button(self.ResultsScreenFrame, text='Save your score', command=lambda: self.player.file_write()).grid()
        tk.Button(self.ResultsScreenFrame, text='Quit program', command=lambda: quit()).grid()
    
    def restart(self):
        self.LoginPage()
        self.ResultsScreenFrame.destroy()


root = root()
root.title("Maths-sistant")
root.geometry("380x140")
root.mainloop()