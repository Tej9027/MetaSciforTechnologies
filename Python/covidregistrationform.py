"""Create a registration form to register for a covid vaccine that should accept the following information
Name of the visitor (Entry)
Age of the visitor (Entry)
Gender (Radio Button)
Address (Text)
Email Id (Entry)
Contact No (Entry)
Country (Entry)
State (Entry)
SELECT If you are having any following disease (checkbox)
->cold
->cough
->fever
->headache

import tkinter

create labels for all above mentioned fields

create their respective entries/texts/checkbox/radio based on the description
given above"""
import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Gather input data from the form
    name = entry_name.get()
    age = entry_age.get()
    gender = gender_var.get()
    address = text_address.get("1.0", tk.END).strip()
    email = entry_email.get()
    contact = entry_contact.get()
    country = entry_country.get()
    state = entry_state.get()
    diseases = [disease for disease, var in disease_vars.items() if var.get()]

    # Validate inputs
    if not name or not age or not email or not contact or not country or not state:
        messagebox.showerror("Error", "Please fill out all required fields.")
        return

    # Here you could add code to save the data or send it to a server
    # For this example, we will just print the data
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("Address:", address)
    print("Email:", email)
    print("Contact No:", contact)
    print("Country:", country)
    print("State:", state)
    print("Diseases:", diseases)

    messagebox.showinfo("Success", "Registration submitted successfully!")

# Create the main application window
root = tk.Tk()
root.title("COVID Vaccine Registration Form")

# Create labels and entry widgets
label_name = tk.Label(root, text="Name of the Visitor:")
entry_name = tk.Entry(root)

label_age = tk.Label(root, text="Age of the Visitor:")
entry_age = tk.Entry(root)

label_gender = tk.Label(root, text="Gender:")
gender_var = tk.StringVar(value="Male")
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male")
radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female")
radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other")

label_address = tk.Label(root, text="Address:")
text_address = tk.Text(root, height=3, width=30)

label_email = tk.Label(root, text="Email ID:")
entry_email = tk.Entry(root)

label_contact = tk.Label(root, text="Contact No:")
entry_contact = tk.Entry(root)

label_country = tk.Label(root, text="Country:")
entry_country = tk.Entry(root)

label_state = tk.Label(root, text="State:")
entry_state = tk.Entry(root)

label_diseases = tk.Label(root, text="Select if you have any of the following diseases:")

# Checkboxes for diseases
disease_vars = {
    "Cold": tk.BooleanVar(),
    "Cough": tk.BooleanVar(),
    "Fever": tk.BooleanVar(),
    "Headache": tk.BooleanVar(),
}

checkbox_cold = tk.Checkbutton(root, text="Cold", variable=disease_vars["Cold"])
checkbox_cough = tk.Checkbutton(root, text="Cough", variable=disease_vars["Cough"])
checkbox_fever = tk.Checkbutton(root, text="Fever", variable=disease_vars["Fever"])
checkbox_headache = tk.Checkbutton(root, text="Headache", variable=disease_vars["Headache"])

# Create the submit button
submit_button = tk.Button(root, text="Submit", command=submit_form)

# Arrange widgets using grid layout
label_name.grid(row=0, column=0, sticky="e", padx=5, pady=5)
entry_name.grid(row=0, column=1, padx=5, pady=5)

label_age.grid(row=1, column=0, sticky="e", padx=5, pady=5)
entry_age.grid(row=1, column=1, padx=5, pady=5)

label_gender.grid(row=2, column=0, sticky="e", padx=5, pady=5)
radio_male.grid(row=2, column=1, sticky="w", padx=5, pady=5)
radio_female.grid(row=2, column=1, padx=5, pady=5)
radio_other.grid(row=2, column=1, sticky="e", padx=5, pady=5)

label_address.grid(row=3, column=0, sticky="ne", padx=5, pady=5)
text_address.grid(row=3, column=1, padx=5, pady=5)

label_email.grid(row=4, column=0, sticky="e", padx=5, pady=5)
entry_email.grid(row=4, column=1, padx=5, pady=5)

label_contact.grid(row=5, column=0, sticky="e", padx=5, pady=5)
entry_contact.grid(row=5, column=1, padx=5, pady=5)

label_country.grid(row=6, column=0, sticky="e", padx=5, pady=5)
entry_country.grid(row=6, column=1, padx=5, pady=5)

label_state.grid(row=7, column=0, sticky="e", padx=5, pady=5)
entry_state.grid(row=7, column=1, padx=5, pady=5)

label_diseases.grid(row=8, column=0, sticky="w", padx=5, pady=5)
checkbox_cold.grid(row=9, column=0, sticky="w", padx=20)
checkbox_cough.grid(row=9, column=1, sticky="w", padx=20)
checkbox_fever.grid(row=10, column=0, sticky="w", padx=20)
checkbox_headache.grid(row=10, column=1, sticky="w", padx=20)

submit_button.grid(row=11, column=0, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()
