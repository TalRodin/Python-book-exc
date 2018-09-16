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
