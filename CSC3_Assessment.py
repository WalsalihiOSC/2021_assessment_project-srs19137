import tkinter as tk
import math

class User:
    def __init__(self, first_name, age):
        self.first_name=first_name  
        self.age=age
        print(f'name from login: {first_name}')
        print(f'age from login: {age}')

    def checklevel(self, plevel):
        try:
            plevel = int(plevel)
            if plevel < 1:
                return('Error less than 1')
            elif plevel == 1:
                return('Questions between 1 and 2')
            elif plevel == 2:
                return('Questions between 1- and 100')
        except:
            print('Error: Not an Integer')


class root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.frame_container = tk.Frame(self)
        self.frame_container.pack(side='top',fill='both',expand=True)
        self.frame_container.grid_rowconfigure(0,weight=1)
        self.frame_container.grid_columnconfigure(0,weight=1)
        self.LoginPage()

        '''self.frames={}
        for Frame in (LoginPage, LevelSelect, Questions, ResultsScreen):
            page_name = Frame.__name__
            frame = Frame(parent=frame_container,controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0,column=0,sticky='nsew')
        
        self.show_frame('LoginPage')'''

    def show_frame(self, page_name):
    
            frame = page_name
            frame.tkraise()

    def LoginPage(self):
        self.LoginPage = tk.Frame(self.frame_container)
        self.LoginPage.pack()
        tk.Label(self.LoginPage, text='Login Screen').pack(padx=10,pady=10)
        tk.Label(self.LoginPage, text='First Name:').pack()
        self.fnameEntry = tk.Entry()
        self.fnameEntry.pack()
        tk.Label(self.LoginPage, text='Last Name:').pack()
        self.ageEntry = tk.Entry()
        self.ageEntry.pack()
        tk.Button(self.LoginPage, text='Go to Level Select', command=lambda: self.nextw()).pack()
        #tk.Button(self, text='Go to Questions', command=lambda: controller.show_frame('Questions')).pack()
        #tk.Button(self, text='Go to Results Screen', command=lambda: controller.show_frame('ResultsScreen')).pack()

    def nextw(self):
        first_name=self.fnameEntry.get()
        age=self.ageEntry.get()
        self.player = User(first_name, age)
        self.LevelSelect()

    def LevelSelect(self):
        self.LevelSelect = tk.Frame(self.frame_container)
        self.LevelSelect.pack()
        tk.Label(self.LevelSelect, text='Level Select').pack(padx=10,pady=10)
        self.level=tk.Entry()
        self.level.pack()
        #tk.Button(self.LevelSelect, text='Go to Login', command=lambda: controller.show_frame('LoginPage')).pack()
        tk.Button(self.LevelSelect, text='Go to Questions', command=lambda: self.nextq()).pack()
        #tk.Button(self.LevelSelect, text='Go to Results Screen', command=lambda: controller.show_frame('ResultsScreen')).pack()

    def nextq(self):
        levels = self.level.get()
        errormessage = self.player.checklevel(levels)
        tk.Message(self.LevelSelect, text=errormessage).pack()



class Questions(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        tk.Label(self, text='Questions').pack(padx=10,pady=10)
        tk.Button(self, text='Go to Login', command=lambda: controller.show_frame('LoginPage')).pack()
        tk.Button(self, text='Go to Level Select', command=lambda: controller.show_frame('LevelSelect')).pack()
        tk.Button(self, text='Go to Results Screen', command=lambda: controller.show_frame('ResultsScreen')).pack()

class ResultsScreen(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        tk.Label(self, text='Results').pack(padx=10,pady=10)
        tk.Button(self, text='Go to Login', command=lambda: controller.show_frame('LoginPage')).pack()
        tk.Button(self, text='Go to Level Select', command=lambda: controller.show_frame('LevelSelect')).pack()
        tk.Button(self, text='Go to Questions', command=lambda: controller.show_frame('Questions')).pack()


root = root()
root.mainloop()