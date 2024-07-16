import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone:
        contacts.append({"name": name, "phone": phone, "email": email, "address": address})
        messagebox.showinfo("Success", "Contact added successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Name and phone number are required!")

def display_contacts():
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def search_contact():
    query = search_entry.get().lower()
    contacts_list.delete(0, tk.END)
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            contacts_list.insert(tk.END, f"{contact['name']} - {contact['phone']}")

def update_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        index = selected_index[0]
        contacts[index] = {
            "name": name_entry.get(),
            "phone": phone_entry.get(),
            "email": email_entry.get(),
            "address": address_entry.get()
        }
        messagebox.showinfo("Success", "Contact updated successfully!")
        clear_entries()
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Select a contact to update!")

def delete_contact():
    selected_index = contacts_list.curselection()
    if selected_index:
        index = selected_index[0]
        del contacts[index]
        messagebox.showinfo("Success", "Contact deleted successfully!")
        display_contacts()
    else:
        messagebox.showwarning("Warning", "Select a contact to delete!")

def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Contact Management System")

tk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(root)
address_entry.grid(row=3, column=1, padx=5, pady=5)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
add_button.grid(row=4, column=0, padx=5, pady=5)

update_button = tk.Button(root, text="Update Contact", command=update_contact)
update_button.grid(row=4, column=1, padx=5, pady=5)

delete_button = tk.Button(root, text="Delete Contact", command=delete_contact)
delete_button.grid(row=5, column=0, padx=5, pady=5)

tk.Label(root, text="Search:").grid(row=6, column=0, padx=5, pady=5)
search_entry = tk.Entry(root)
search_entry.grid(row=6, column=1, padx=5, pady=5)

search_button = tk.Button(root, text="Search", command=search_contact)
search_button.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

contacts_list = tk.Listbox(root, width=50)
contacts_list.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

display_contacts()

root.mainloop()
