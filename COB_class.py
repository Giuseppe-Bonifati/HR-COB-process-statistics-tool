import tkinter as tk
from tkinter import messagebox


#Just for an information purpose on the submit function i multiplicate the value for 10, 15 or 30 base on the time that each process will require, here below the info for every process
# HIRING = 15
# TERMINATION  = 10
# EXTENSION = 10
# INAIL= 30
# TRANSFORMATION = 10


#class to use for hr process , will return a dictionary will how many ticket has been submitted for each process.

class Month(tk.Tk):
    '''the class inherited from tkinter ,and will be called to ask the user how many Hr ticket has been submitted , the function can check the entries and can return all the information within a dictionary'''
    def __init__(self,month):
        super().__init__()

        self.month = month

        self.process = {}

        self.window_closed_manually = False

        self.protocol("WM_DELETE_WINDOW", self.on_close)

        self.title(f"{self.month} COB ")
        self.geometry("800x500")
        self.configure(bg="lightblue")

        self.label = tk.Label(self, text=f"Insert All Ticket for {self.month}\n", fg="Green", font= "bold_font",bg="lightblue")
        self.label.grid(row =0, column= 2,  pady=10)

        self.labelhire_rehire_perm_and_temp_Employees = tk.Label(self, text="Hire or Rehire Full and Par times",bg="lightblue")
        self.labelhire_rehire_perm_and_temp_Employees.grid(row=1, column=0)
        
        self.entryhire_rehire_perm_and_temp_Employees= tk.Entry(self, width=8,  borderwidth =1, relief="solid", font=("Helvetica", 8))
        self.entryhire_rehire_perm_and_temp_Employees.grid(row= 1 , column= 2, pady=10)


        self.labelhire_rehire_internships_extracurriculare = tk.Label(self, text="Hire or Rehire an Internships Extracurricular", bg="lightblue")
        self.labelhire_rehire_internships_extracurriculare.grid(row=2, column=0)
        
        self.entryhire_rehire_internships_extracurriculare = tk.Entry(self, width=8, borderwidth = 1, relief="solid", font=("Helvetica", 8))
        self.entryhire_rehire_internships_extracurriculare.grid(row= 2 , column= 2, pady=10)


        self.labelContract_Renewals = tk.Label(self, text="Contract Renewals",bg="lightblue")
        self.labelContract_Renewals.grid(row=3, column=0)        

        self.entryContract_Renewals= tk.Entry(self, width=8, borderwidth =1, relief="solid", font=("Helvetica", 8))
        self.entryContract_Renewals.grid(row=  3, column= 2, pady=10)


        self.labelTransfer_Internal_Changes = tk.Label(self, text="Transfer Internal Changes",bg="lightblue")
        self.labelTransfer_Internal_Changes .grid(row=4, column=0)

        self.entryTransfer_Internal_Changes  = tk.Entry(self, width=8,borderwidth =1, relief="solid", font=("Helvetica", 8) )
        self.entryTransfer_Internal_Changes .grid(row= 4 , column= 2, pady=10)


        self.labelEmployee_Termination= tk.Label(self, text="Employee Termination", bg="lightblue")
        self.labelEmployee_Termination.grid(row=8, column=0)
    
        self.entryEmployee_Termination = tk.Entry(self, width=8, borderwidth =1, relief="solid", font=("Helvetica", 8))
        self.entryEmployee_Termination.grid(row= 8, column= 2, pady=10)



        self.labelinjuries= tk.Label(self, text="Injuries", bg="lightblue")
        self.labelinjuries.grid(row=10, column=0)
    
        self.entryinjuries = tk.Entry(self, width=8, borderwidth =1, relief="solid", font=("Helvetica", 8))
        self.entryinjuries.grid(row= 10, column= 2, pady=10)




        self.label = tk.Label(self, text=f"Before clicking submit all fields must be filled in\nif there were no tickets, 0 will be automatically added ", fg="Red", font= "bold_font",bg="lightblue")
        self.label.grid(row =36, column= 2,  pady=10)

        self.submit_button = tk.Button(self, text="Submit", command=self.on_submit, fg = "blue", font="bold_font",borderwidth =1, relief="solid")
        self.submit_button.grid(row= 38 , column= 2,  pady=10)


        self.submit_button_skip = tk.Button(self, text="Skip", command=self.skip, fg = "grey",borderwidth =1, relief="solid", width=4, height=2,font=("Helvetica", 8))
        self.submit_button_skip.grid(row= 0 , column= 0,  pady=10)



    def on_close(self):
        '''when we close the window then the program will start to work'''
        self.window_closed_manually = True
        self.destroy()

    def check(self,number,record):
            '''it is checking the number that we type inside our program, if something is wrong will raise an error'''
            try:
                if len(number) == 0 or int(number) == 0:
                    return 0
                elif not isinstance(int(number), (int)) :
                        raise ValueError
                elif len(number) > 1 and number[0] == "0":
                    raise ValueError
            except ValueError:
                    tk.messagebox.showerror(
            title="Error number", message=f"Record {record}, Invalid Number/Please enter a valid number\n"
        )    
                
            else:
                return int(number)
            
    def skip(self):
            '''the function will be called when we click on skip button on our app and will return all values 0 and will stop to run the first window loop'''
            yes = tk.messagebox.askquestion(title="Confirmation", message="\tDo you want Skip?\n  All the record will be filled with 0", )
            if yes == "yes":
                  n_a = 0
                  
                  self.process = {"Hire_Rehire":n_a,"Hire_Interns":n_a,"Extension":n_a,"Transfer ":n_a,
                    "Termination":n_a,"Injuries":n_a}
                 
                  self.destroy()
            else:
                  return self


    def on_submit(self):
            '''after the function will be called , on submit will get the information inside the entry(the value that we type in) and will call the function check the control the value of the entry . if everything is okay will return a dictionary containing the information  that was passed'''
   
            hire_rehire_perm_and_temp_Employees_input = self.entryhire_rehire_perm_and_temp_Employees.get()
            hire_rehire_perm_and_temp_Employees_checked =  self.check(hire_rehire_perm_and_temp_Employees_input,"Hire or Rehire Full and Par times")

            hire_rehire_internships_extracurriculare_input = self.entryhire_rehire_internships_extracurriculare.get()
            hire_rehire_internships_extracurriculare_checked =  self.check(hire_rehire_internships_extracurriculare_input,"Hire or Rehire an Internships Extracurricular")

            Contract_Renewals_input = self.entryContract_Renewals.get()
            Contract_Renewals_checked =  self.check(Contract_Renewals_input,"Contract Renewals")

            Transfer_Internal_Changes_input  = self.entryTransfer_Internal_Changes .get()
            Transfer_Internal_Changes_checked =  self.check(Transfer_Internal_Changes_input,"Transfer Internal Changes")


            Employee_Termination_input = self.entryEmployee_Termination.get()
            Employee_Termination_checked =  self.check(Employee_Termination_input,"Employee Termination")

            injuries_input = self.entryinjuries.get()
            injuries_checked =  self.check(injuries_input,"Injuries")

        

            process = {"Hire_Rehire":hire_rehire_perm_and_temp_Employees_checked*15,"Hire_Intern":hire_rehire_internships_extracurriculare_checked*15,"Extension":Contract_Renewals_checked*10,"Transfer":Transfer_Internal_Changes_checked*10,
                    "Termination":Employee_Termination_checked*10,"Injuries":injuries_checked*30}
            

        

        
            yes = tk.messagebox.askquestion(title="Confirmation", message="Do you want to confirm your data ?", )
            if yes == "yes":
                  self.process = process
                  self.destroy()
            else:
                  return self


                 

        

            



