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
