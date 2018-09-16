#1

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.label=tkinter.Label(self.main_window, text='Programming is fun')
        self.label.pack()
        tkinter.mainloop()
my_gui=MyGUI()    

#2

import tkinter

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.label1=tkinter.Label(self.main_window, text='Programming is fun')
        self.label2=tkinter.Label(self.main_window, text='Programming is fun')
        self.label1.pack(side='left')
        self.label2.pack(side='left')
        tkinter.mainloop()
my_gui=MyGUI()

#3

import tkinter

class My_GUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        self.label1=tkinter.Label(self.top_frame, text='Text')
        self.label2=tkinter.Label(self.bottom_frame, text='Text')
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
my_gui=My_GUI()

#4

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.my_button=tkinter.Button(self.main_window, text='Click OK when you are ready to continue.', command=self.do_something)
        self.my_button.pack()
        tkinter.mainloop()
        
    def do_something(self):
        tkinter.messagebox.showinfo('Response', \
                                    'Program Paused')
        
        
my_gui=MyGUI()

#5

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame(self.main_window)
        self.button_frame=tkinter.Frame(self.main_window)
        
        self.prompt_label=tkinter.Label(self.top_frame, text='Calculate')
        self.calc_botton=tkinter.Button(self.button_frame, text='Calculate')
        
        self.prompt_label.pack(side='left')
        self.calc_botton.pack(side='left')
        
        self.top_frame.pack()
        self.button_frame.pack()
        
        tkinter.mainloop()

            
            
my_gui=MyGUI()


#6

import tkinter
import tkinter.messagebox



class MyGUI:
    def __init__(self):
            self.main_window=tkinter.Tk()
            self.top_frame=tkinter.Frame(self.main_window)
            self.bottom_frame=tkinter.Frame(self.main_window)
            
            self.prompt_label=tkinter.Label(self.top_frame, text='Calculate: ')
            self.data_entry=tkinter.Entry(self.top_frame, width=10)  
            
            self.prompt_label.pack(side='left')
            self.data_entry.pack(side='left')
            
            self.calc_button=tkinter.Button(self.bottom_frame, text='Calculate')
            self.quit_button=tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
            
            self.calc_button.pack(side='left')
            self.quit_button.pack(side='left')
            
            self.top_frame.pack()
            self.bottom_frame.pack()
            
            tkinter.mainloop()
            
            
my_guy=MyGUI()

#7

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.prompt_label=tkinter.Label(self.top_frame, text='Enter number')
        self.number=tkinter.Entry(self.top_frame, width=10)
        
        self.prompt_label.pack(side='left')
        self.number.pack(side='left')
        
        self.calc_button=tkinter.Button(self.bottom_frame, text='Convert', command=self.convert)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)

        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
        
    def convert(self):
        var=int(self.number.get())
        
        tkinter.messagebox.showinfo(var)
my_gui=MyGUI()




















