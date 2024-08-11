import tkinter as tk
from tkinter import messagebox
import random

#rng core
def generate_random_number():
    try:
        min_val = int(min_entry.get())
        max_val = int(max_entry.get())
        if min_val > max_val:
            messagebox.showerror("Error", "Minimum value cannot be greater than maximum value.")
        else:
            random_number = random.randint(min_val, max_val)
            result_label.config(text=f"Random Number: {random_number}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid integers.")

#UI
root = tk.Tk()
root.title("Random Number Generator")
root.geometry("300x200")

#Label
instructions = tk.Label(root, text="Enter the range for random number generation:")
instructions.pack(pady=10)

#UI range
min_label = tk.Label(root, text="Minimum:")
min_label.pack()
min_entry = tk.Entry(root)
min_entry.pack()

max_label = tk.Label(root, text="Maximum:")
max_label.pack()
max_entry = tk.Entry(root)
max_entry.pack()

#UI execution
generate_button = tk.Button(root, text="Generate Random Number", command=generate_random_number)
generate_button.pack(pady=10)

#Label for display
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

#execution
root.mainloop()