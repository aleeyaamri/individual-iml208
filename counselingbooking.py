import tkinter as tk
from tkinter import ttk, messagebox

# Initialize application window
root = tk.Tk()
root.title("Counseling Session Booking System")
root.geometry("800x500")

# Data storage
bookings = []

# Functions
def create_booking():
    """Create a new booking"""
    name = name_var.get()
    date = date_var.get()
    time = time_var.get()
    duration = duration_var.get()
    room = room_var.get()

    if not (name and date and time and duration and room):
        messagebox.showerror("Input Error", "All fields are required!")
        return

    if not duration.isdigit():
        messagebox.showerror("Input Error", "Duration must be a number!")
        return

    bookings.append({"Name": name, "Date": date, "Time": time, "Duration": duration, "Room": room})
    refresh_table()
    clear_inputs()
    messagebox.showinfo("Success", "Booking created successfully!")

def read_booking():
    """Read selected booking details"""
    try:
        selected_item = table.selection()[0]
        index = int(table.item(selected_item)['values'][0]) - 1
        booking = bookings[index]

        name_var.set(booking["Name"])
        date_var.set(booking["Date"])
        time_var.set(booking["Time"])
        duration_var.set(booking["Duration"])
        room_var.set(booking["Room"])

    except IndexError:
        messagebox.showerror("Error", "Please select a booking to view!")

def update_booking():
    """Update an existing booking"""
    try:
        selected_item = table.selection()[0]
        index = int(table.item(selected_item)['values'][0]) - 1

        if messagebox.askyesno("Confirm Update", "Are you sure you want to update this booking?"):
            bookings[index] = {
                "Name": name_var.get(),
                "Date": date_var.get(),
                "Time": time_var.get(),
                "Duration": duration_var.get(),
                "Room": room_var.get()
            }
            refresh_table()
            clear_inputs()
            messagebox.showinfo("Success", "Booking updated successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a booking to update!")

def delete_booking():
    """Delete a booking"""
    try:
        selected_item = table.selection()[0]
        index = int(table.item(selected_item)['values'][0]) - 1

        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this booking?"):
            bookings.pop(index)
            refresh_table()
            clear_inputs()
            messagebox.showinfo("Success", "Booking deleted successfully!")
    except IndexError:
        messagebox.showerror("Error", "Please select a booking to delete!")

def refresh_table():
    """Refresh the table with updated bookings"""
    for item in table.get_children():
        table.delete(item)

    for i, booking in enumerate(bookings, start=1):
        table.insert("", "end", values=(i, booking["Name"], booking["Date"], booking["Time"], booking["Duration"], booking["Room"]))

def clear_inputs():
    """Clear input fields"""
    name_var.set("aleeya")
    date_var.set("2024-04-04")
    time_var.set("18:00")
    duration_var.set("60 minutes")
    room_var.set("7")

# Variables
name_var = tk.StringVar()
date_var = tk.StringVar()
time_var = tk.StringVar()
duration_var = tk.StringVar()
room_var = tk.StringVar()

# Input fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=name_var).grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=date_var).grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Time (HH:MM)").grid(row=2, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=time_var).grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Duration (minutes)").grid(row=3, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=duration_var).grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Room").grid(row=4, column=0, padx=10, pady=5)
tk.Entry(root, textvariable=room_var).grid(row=4, column=1, padx=10, pady=5)

# Buttons
tk.Button(root, text="Create", command=create_booking, bg="green", fg="white").grid(row=5, column=0, padx=10, pady=10)
tk.Button(root, text="Read", command=read_booking, bg="blue", fg="white").grid(row=5, column=1, padx=10, pady=10)
tk.Button(root, text="Update", command=update_booking, bg="orange", fg="white").grid(row=5, column=2, padx=10, pady=10)
tk.Button(root, text="Delete", command=delete_booking, bg="red", fg="white").grid(row=5, column=3, padx=10, pady=10)
tk.Button(root, text="Clear", command=clear_inputs).grid(row=5, column=4, padx=10, pady=10)

# Table
columns = ("#", "Name", "Date", "Time", "Duration", "Room")
table = ttk.Treeview(root, columns=columns, show="headings", height=10)
for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100, anchor="center")

table.grid(row=6, column=0, columnspan=5, padx=10, pady=10)

# Run application
root.mainloop()
