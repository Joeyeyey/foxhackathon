path_to_jsons = r'I:\jsondata'
import os
import json
import tkinter as tk
from tkinter import ttk

class Employee(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)


class gui(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.title('Fox Optimization Hackathon Submission')
        self.create_new_employee_section()
    def create_new_employee_section(self):
        # self.pack(fill=BOTH, expand=1)
        quitButton = tk.Button(self, text="Quit")
        quitButton.place(x=0, y=0)

# this is going to become a method of the main gui
def main():
    potential_files = os.listdir(path_to_jsons)
    no_json_file_names = [i.split('.')[0] for i in potential_files]
    print(no_json_file_names)


    base_json = {
     "staffTypes": staffTypes_dict,
     "revenueGoal": rev_goal,
     "shiftStart": start_string,                                                             ### should have this export to the correct user
     "shiftEnd": end_string                                                                  ### should have this export to the correct user
}                                                                                            ### should have this export to the correct user
    with open(json_name, 'wb'):                                                              ### should have this export to the correct user
        json.dump(base_json)                                                                 ### should have this export to the correct user




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry('500x500')
    app = gui(root)
    root.mainloop()
