import tkinter as tk
import math

ROOT = tk.Tk()

loginframe = tk.Frame(master=None,width=200,height=200)
loginframe.grid(column=0,row=0)
testlabellogin = tk.Label(master=loginframe,text='Login Screen')
testlabellogin.grid()

levelselect = tk.Frame(master=None,width=200,height=200)
levelselect.grid(column=0,row=0)

testlabellevelselect = tk.Label(master=levelselect,text='Level Select')
testlabellevelselect.grid()

tk.Button(text='Login to Level Select',command=levelselect.tkraise).grid()
tk.Button(text='Level Select to Login',command=loginframe.tkraise).grid()
ROOT.mainloop()