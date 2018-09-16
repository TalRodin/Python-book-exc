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
