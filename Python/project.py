"""
In a coding class the teacher has taught the kids about the python GUI and has now assigned the following
task to the students
1) Create a random name picker from a given list of students
2) should have a button clicking on which a random name should be picked
3) Once the random name is picked the name should be removed from the list so that the name is not repeated
and also the removed name should show in completed section #create a GUI with two sections one to see the
randomly generated name and the other one to see the names that are generated randomly and which are not
supposed to be considered for generating randomly again. zqy-msvc-eir
"""
import random
import tkinter as tk


class RandomName:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Name Picker")

        self.student = ["Shanu", "Ravi", "Nikki", "Amit", "Asha", "Nikhil", "Ashu", "Arun", "Amit", "Bhanu", "Navneet"]

        self.picked_names = []

        self.name_label = tk.Label(root, text="Pick a Name to Start!", font=("Arial", 16), pady=10)
        self.name_label.pack()

        self.pick_button = tk.Button(root, text="Pick a Name", command=self.pick_random_name, font=("Arial", 18),
                                     pady=5)
        self.pick_button.pack()

        self.completed_frame = tk.Frame(root)
        self.completed_frame.pack(pady=10)

        self.completed_label = tk.Label(self.completed_frame, text="Completed Names", font=("Arial", 14))
        self.completed_label.pack()

        self.completed_listbox = tk.Listbox(self.completed_frame, width=40, height=10, font=("Arial", 12))
        self.completed_listbox.pack()

    def pick_random_name(self):
        if self.student:
            random_name = random.choice(self.student)
            self.student.remove(random_name)

            self.name_label.config(text = f"Picked Name: {random_name}")

            self.picked_names.append(random_name)
            self.completed_listbox.insert(tk.END, random_name)
        else:
            self.name_label.config(text="All names have been picked")


root = tk.Tk()
app = RandomName(root)
root.mainloop()
