#1

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame()
        self.bottom_frame=tkinter.Frame()
        
        self.value=tkinter.StringVar()
        self.inf=tkinter.Label(self.top_frame, textvariable=self.value)
        
        self.inf.pack(side='left')
        
        self.inf_button=tkinter.Button(self.bottom_frame, text='Show Info',\
                                       command=self.show_info)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit',\
                                        command=self.main_window.destroy)
        
        self.inf_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
        
    def show_info(self):
        infor='First Name, Last Name \nAddress'
        self.value.set(infor)
        
my_gui=MyGUI()


#2

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame()
        self.mid_frame=tkinter.Frame()
        self.bottom_frame=tkinter.Frame()
        
        self.language_Latin=tkinter.Label(self.top_frame, text='Latin')
        self.language_English=tkinter.Label(self.top_frame, text='English')
        self.language_Latin.pack(side='left')
        self.language_English.pack(side='right')
        
        
        
        #self.sinister=tkinter.Label(self.mid_frame, text='sinister')
        #self.sinister.pack(side='top')
        self.value_sinister=tkinter.StringVar()
        self.sinister_label=tkinter.Label(self.mid_frame, textvariable=self.value_sinister)
        self.sinister_label.pack(side='left')
        
        
        #self.dexter=tkinter.Label(self.mid_frame, text='dexter')        
        #self.dexter.pack(side='left')
        self.value_dexter=tkinter.StringVar()
        self.dexter_label=tkinter.Label(self.mid_frame, textvariable=self.value_dexter)
        self.dexter_label.pack(side='right')
        
        
       # self.medium=tkinter.Label(self.mid_frame, text='medium')
       # self.medium.pack(side='left')
        self.value_medium=tkinter.StringVar()
        self.medium_label=tkinter.Label(self.mid_frame, textvariable=self.value_medium)
        self.medium_label.pack(side='right')
                
        self.sinister_button=tkinter.Button(self.bottom_frame, text='sinister',command=self.translate_sinister)
        self.dexter_button=tkinter.Button(self.bottom_frame, text='dexter',command=self.translate_dexter)
        self.medium_button=tkinter.Button(self.bottom_frame, text='medium',command=self.translate_medium)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy)

        self.sinister_button.pack(side='left')
        self.dexter_button.pack(side='left')
        self.medium_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
        
    def translate_sinister(self):
       translation='left'
       self.value_sinister.set('Sinister' + ' ' + translation)
    def translate_dexter(self):
       translation='right'
       self.value_dexter.set('Dexter' + ' '+ translation)
    def translate_medium(self): 
       translation='middle'
       self.value_medium.set('Medium' + ' '+ translation)
my_gui=MyGUI()

#3

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.num_gallons=tkinter.Label(self.top_frame, text='Number Gallons: ')
        self.gallons_entry=tkinter.Entry(self.top_frame, width=10)
        self.num_gallons.pack(side='left')
        self.gallons_entry.pack(side='left')
        
        self.num_miles=tkinter.Label(self.top_frame, text='Number Miles: ')
        self.miles_entry=tkinter.Entry(self.top_frame, width=10)
        self.num_miles.pack(side='left')
        self.miles_entry.pack(side='left')
        
        self.result=tkinter.Label(self.mid_frame, text='MPG: ')
        self.value=tkinter.StringVar()
        self.value_l=tkinter.Label(self.mid_frame, textvariable=self.value)
        
        self.calc_button=tkinter.Button(self.bottom_frame, text='Calculate', command=self.calc_MPG)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        
        
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')
        self.result.pack(side='left')
        self.value_l.pack(side='left')
        
        
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def calc_MPG(self):
        self.num_gallons=float(self.gallons_entry.get())
        self.num_miles=float(self.miles_entry.get())
        self.MPG=self.num_miles/self.num_gallons
        
        self.value.set(self.MPG)
        
my_gui=MyGUI()


#4

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.C=tkinter.Label(self.top_frame, text='Celcius: ')
        self.C_entry=tkinter.Entry(self.top_frame, width=10)
        
        self.C.pack(side='left')
        self.C_entry.pack(side='left')
        
        self.F=tkinter.Label(self.mid_frame, text='Fahrenheit: ')
        self.value=tkinter.StringVar()
        self.F_result=tkinter.Label(self.mid_frame, textvariable=self.value)
        
        self.F.pack(side='left')
        self.F_result.pack(side='left')
        
        
        self.conv_button=tkinter.Button(self.bottom_frame, text='Convert', command=self.converter)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit',command=self.main_window.destroy)
        
        self.conv_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
    def converter(self):
        F=(9/5)*float(self.C_entry.get())+32
        self.value.set(F)
        
my_gui=MyGUI()


#5

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        
        
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.value_label=tkinter.Label(self.top_frame, text='Value: ')
        self.value_entry=tkinter.Entry(self.top_frame, width=10)
        
        self.value_label.pack(side='left')
        self.value_entry.pack(side='left')
        
        self.assessment=tkinter.Label(self.mid_frame, text='Assessment: ')
        self.assessment_value=tkinter.StringVar()
        self.ass_label=tkinter.Label(self.mid_frame, textvariable=self.assessment_value)
        
        self.assessment.pack(side='left')
        self.ass_label.pack(side='left')
                
        self.tax=tkinter.Label(self.mid_frame, text='Tax: ')
        self.tax_value=tkinter.StringVar()
        self.tax_label=tkinter.Label(self.mid_frame, textvariable=self.tax_value)
        
        self.tax.pack(side='left')
        self.tax_label.pack(side='left')
        
        self.calc_Button=tkinter.Button(self.bottom_frame, text='Calculate',command=self.calculate)
        
        self.quit_Button=tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy)
        
        self.calc_Button.pack(side='left')
        self.quit_Button.pack(side='left')
        
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop() 
        
        
    def calculate(self):
        ass_value=float(self.value_entry.get())*0.60
        self.assessment_value.set(ass_value)
        tax_value=(ass_value/100)*0.64
        self.tax_value.set(tax_value)
        
        
        
my_gui=MyGUI()

#6












































