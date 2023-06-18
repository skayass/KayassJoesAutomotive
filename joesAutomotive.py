# GUI Chapter 13: Programming Exercise Problem 6 Joes Automotive
# Samia Kayass

import tkinter
import tkinter.messagebox


# Creating class
class JoesAutomotiveGUI:
    
    def __init__(self):

        # Creating the main window.
        self.main_window = tkinter.Tk()
      

        # Creating two frames, One for the checkbox buttons
        # and another for the regular button widgets.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        # Creating the seven IntVar to use with the check buttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()

        # Seting the IntVar objects to 0.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)

        # Creating the check buttons widgets in the top frame,
        # for the routine maintenace.
        self.cb1 = tkinter.Checkbutton(self.top_frame, text= "Oil change - $30.00", variable= self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame, text= "Lube job - $20.00", variable= self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame, text= "Radiator flush - $40.00", variable= self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame, text= "Transmission flush - $100.00", variable= self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame, text= "Inspection - $35.00", variable= self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame, text= "Muffler replacement - $200.00", variable= self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame, text= "Tire rotation - $20.00", variable= self.cb_var7)

        # Pack all the check buttons.
        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()
        self.cb4.pack()
        self.cb5.pack()
        self.cb6.pack()
        self.cb7.pack()

        # Creating an Charges Button and Quit Button.
        self.charge_button = tkinter.Button(self.bottom_frame, text="Display Charges", command=self.show_choice)
        self.quit_button = tkinter.Button(self.bottom_frame, text="Quit", command=self.main_window.destroy)

        # Pack the Charges Button and Quit Button.
        self.charge_button.pack(side="left")
        self.quit_button.pack(side="left")

        # Pack the frames.
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Start the mainloop
        tkinter.mainloop()

      

    #The method show_choice is the callback function for the Charges Button.
    def show_choice(self):
        
        self.total = 0

        # Creating a message string.
        self.message = "Your Total Charges \n"

        
        # Creating an if statement to determine which check buttons are selected,
        # and calculate them, then build the message string accordingly.
        if self.cb_var1.get() == 1:
            self.message = self.message + "Oil change -$30.00\n"
            self.total = self.total + 30

        if self.cb_var2.get() == 1:
            self.message = self.message + "Lube job -$20.00\n"
            self.total = self.total + 20

        if self.cb_var3.get() == 1:
            self.message = self.message + "Radiator flush -$40.00\n"
            self.total = self.total + 40

        if self.cb_var4.get() == 1:
            self.message = self.message + "Transmission flush -$100.00\n"
            self.total = self.total + 100

        if self.cb_var5.get() == 1:
            self.message = self.message + "Inspection -$35.00\n"
            self.total = self.total + 35

        if self.cb_var6.get() == 1:
            self.message = self.message + "Muffler replacement -$200.00\n"
            self.total = self.total + 200

        if self.cb_var7.get() == 1:
            self.message = self.message + "Tire rotation -$20.00\n"
            self.total = self.total + 20

        self.final = "Your total charges is: $" + str(self.total)
        
        # Displaying the message in an info dialog box.
        tkinter.messagebox.showinfo("Total charges ", self.final)
        
# Creating an instance of the class JoesautomativeGUI
j_automative_gui = JoesAutomotiveGUI()
