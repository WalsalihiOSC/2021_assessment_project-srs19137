import tkinter as tk
import math

ROOT = tk.Tk()

loginframe = tk.Frame(master=None)
loginframe.grid(column=0,row=0)
testlabellogin = tk.Label(master=loginframe,text='Login Screen')
testlabellogin.grid()

levelselect = tk.Frame(master=None)
levelselect.grid(column=0,row=0)
testlabellevelselect = tk.Label(master=levelselect,text='Level Select')
testlabellevelselect.grid()

questions = tk.Frame(master=None)
questions.grid(column=0,row=0)
testlabelquestions = tk.Label(master=questions,text='Questions')
testlabelquestions.grid()

tk.Button(text='Raise Login Frame',command=levelselect.tkraise).grid()
tk.Button(text='Raise Level Select Frame',command=loginframe.tkraise).grid()
tk.Button(text='Raise Questions Frame',command=questions.tkraise).grid()
ROOT.mainloop()