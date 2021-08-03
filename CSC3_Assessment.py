import tkinter as tk
import math

class root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        frame_container = tk.Frame(self)
        frame_container.pack(side='top',fill='both',expand=True)
        frame_container.grid_rowconfigure(0,weight=1)
        frame_container.grid_columnconfigure(0,weight=1)

        self.frames={}
        for Frame in (LoginPage, LevelSelect, Questions):
            page_name = Frame.__name__
            frame = Frame(parent=frame_container,controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame('LoginPage')

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller= controller
        tk.Label(self, text='Login Label').pack(padx=10,pady=10)
        tk.Button(self, text='Go to Level Select', command=lambda: controller.show_frame('LevelSelect')).pack()

class LevelSelect(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Label(self, text='Level Select').pack(padx=10,pady=10)
        tk.Button(self, text='Go to Questions', command=lambda: controller.show_frame('Questions')).pack()

class Questions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Label(self, text='Questions').pack(padx=10,pady=10)
        tk.Button(self, text='Go to Login', command=lambda: controller.show_frame('LoginPage')).pack()

root = root()
root.mainloop()