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
