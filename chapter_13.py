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

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
        
        self.cb_var_oil_change=tkinter.IntVar()
        self.cb_var_lube_job=tkinter.IntVar()
        self.cb_var_radiator_flush=tkinter.IntVar()
        self.cb_var_transmission_flush=tkinter.IntVar()
        self.cb_var_inspection=tkinter.IntVar()
        self.cb_var_muffler_replacement=tkinter.IntVar()
        self.cb_var_tire_rotation=tkinter.IntVar()
        
        self.cb_var_oil_change.set(0)
        self.cb_var_lube_job.set(0)
        self.cb_var_radiator_flush.set(0)
        self.cb_var_transmission_flush.set(0)
        self.cb_var_inspection.set(0)
        self.cb_var_muffler_replacement.set(0)
        self.cb_var_tire_rotation.set(0)
        
        self.cb_oil_change=tkinter.Checkbutton(self.top_frame, text='Oil Change',\
                                               variable=self.cb_var_oil_change)
        self.cb_lube_job=tkinter.Checkbutton(self.top_frame, text='Lube job',\
                                               variable=self.cb_var_lube_job)
        self.cb_radiator_flush=tkinter.Checkbutton(self.top_frame, text='Radiator flush',\
                                               variable=self.cb_var_radiator_flush)
        self.cb_transmission_flush=tkinter.Checkbutton(self.top_frame, text='Transmission flush',\
                                               variable=self.cb_var_transmission_flush)
        self.cb_inspection=tkinter.Checkbutton(self.top_frame, text='Inspection',\
                                               variable=self.cb_var_inspection)
        self.cb_muffler_replacement=tkinter.Checkbutton(self.top_frame, text='Muffler Replacement',\
                                               variable=self.cb_var_muffler_replacement)
        self.cb_tire_rotation=tkinter.Checkbutton(self.top_frame, text='Tire Rotation',\
                                               variable=self.cb_var_tire_rotation)
        
        
        self.cb_oil_change.pack()
        self.cb_lube_job.pack()
        self.cb_radiator_flush.pack()
        self.cb_transmission_flush.pack()
        self.cb_inspection.pack()
        self.cb_muffler_replacement.pack()
        self.cb_tire_rotation.pack()
        
        self.ok_button=tkinter.Button(self.bottom_frame, \
                                      text='Total', command=self.show_sum)
        self.quit_button=tkinter.Button(self.bottom_frame, \
                                        text='Quit', command=self.main_window.destroy)
        
        
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()
        
        
    def show_sum(self):
        self.message='You selected: \n'
        total=0.0
        
        if self.cb_var_oil_change.get()==1:
            self.message=self.message+'$26.00\n'
            total+=26.0           
        if self.cb_var_lube_job.get()==1:
            self.message=self.message+'$18.00\n'
            total+=18.00
        if self.cb_var_radiator_flush.get()==1:
            self.message=self.message+'$30.00\n'
            total+=30.00
        if self.cb_var_transmission_flush.get()==1:
            self.message=self.message+'$80.00\n'
            total+=80.00
        if self.cb_var_inspection.get()==1:
            self.message=self.message+'$15.00\n'
            total+=15.00
        if self.cb_var_muffler_replacement.get()==1:
            self.message=self.message+'$100.00\n'
            total+=100.00
        if self.cb_var_tire_rotation.get()==1:
            self.message=self.message+'$20.00\n'
            total+=20.00
        
        
        tkinter.messagebox.showinfo('Selection:',self.message )
        tkinter.messagebox.showinfo('Total: ',total)
        
my_guy=MyGUI()

#7

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()
        self.top_frame=tkinter.Frame(self.main_window)
        self.mid_frame=tkinter.Frame(self.main_window)
        self.bottom_frame=tkinter.Frame(self.main_window)
               
        self.radio_var=tkinter.IntVar()
        self.radio_var.set(1)
        
        self.rb_daytime=tkinter.Radiobutton(self.top_frame, text='Daytime',\
                                            variable=self.radio_var, value=1)
        self.rb_evening=tkinter.Radiobutton(self.top_frame, text='Evening',\
                                            variable=self.radio_var, value=2)
        self.rb_off_peak=tkinter.Radiobutton(self.top_frame, text='Off-Peak',\
                                            variable=self.radio_var, value=3)
        self.rb_daytime.pack()
        self.rb_evening.pack()
        self.rb_off_peak.pack()
        
        
        self.minutes=tkinter.Label(self.mid_frame, text='Number minutes: ')
        self.minutes_entry=tkinter.Entry(self.mid_frame, width=5)
        
        self.minutes.pack(side='left')
        self.minutes_entry.pack(side='left')
        
        
        self.ok_button=tkinter.Button(self.bottom_frame, text='Calculate', command=self.show_choice)
        self.quit_button=tkinter.Button(self.bottom_frame, text='Quit', command=self.main_window.destroy )
        
        self.ok_button.pack(side='left')
        self.quit_button.pack(side='left')
        
        
        
        self.top_frame.pack()
        self.mid_frame.pack()
        self.bottom_frame.pack()
        
        tkinter.mainloop()
        
        
    def show_choice(self):
        a=self.radio_var.get()
        if a==1:
            minutes_price=float(self.minutes_entry.get())*0.07
            
            message='Daytime (6:00 a.m. through 5:59 p.m.)\nCharge for call: $'
        if a==2:
            minutes_price=float(self.minutes_entry.get())*0.12
            message='Evening (6:00 p.m. through 11:59 p.m.)\nCharge for call: $'
        if a==3:
            minutes_price=float(self.minutes_entry.get())*0.05
            message='Off-Peak (midnight through 5:59 a.m.)\nCharge for call: $'
        tkinter.messagebox.showinfo('Selection', 'You selected option: '+ message+str(minutes_price))


my_guy=MyGUI()











































