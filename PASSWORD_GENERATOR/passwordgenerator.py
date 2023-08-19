import random
import string
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.configure(bg="#F0F0F0")

        self.container = ttk.Frame(root, padding=20)
        self.container.grid(column=0, row=0)
        
        self.username_label = ttk.Label(self.container, text="Username:")
        self.username_label.grid(column=0, row=0, sticky=tk.W, padx=10, pady=5)

        self.username_entry = ttk.Entry(self.container)
        self.username_entry.grid(column=1, row=0, padx=10, pady=5)

        self.password_length_label = ttk.Label(self.container, text="Password Length:")
        self.password_length_label.grid(column=0, row=1, sticky=tk.W, padx=10, pady=5)

        self.password_length_entry = ttk.Entry(self.container)
        self.password_length_entry.grid(column=1, row=1, padx=10, pady=5)
        self.password_length_entry.insert(0, "8")

        self.capital_var = tk.IntVar()
        self.capital_check = ttk.Checkbutton(self.container, text="Include Capital Letters", variable=self.capital_var)
        self.capital_check.grid(column=0, row=2, columnspan=2, sticky=tk.W, padx=10, pady=5)

        self.special_var = tk.IntVar()
        self.special_check = ttk.Checkbutton(self.container, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(column=0, row=3, columnspan=2, sticky=tk.W, padx=10, pady=5)

        self.number_var = tk.IntVar()
        self.number_check = ttk.Checkbutton(self.container, text="Include Numbers", variable=self.number_var)
        self.number_check.grid(column=0, row=4, columnspan=2, sticky=tk.W, padx=10, pady=5)

        self.generate_button = ttk.Button(self.container, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(column=0, row=5, columnspan=2, padx=10, pady=10)

        self.password_label = ttk.Label(self.container, text="Generated Password:")
        self.password_label.grid(column=0, row=6, columnspan=2, padx=10, pady=5)

        self.copy_button = ttk.Button(self.container, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(column=0, row=7, padx=10, pady=5)

        self.reset_button = ttk.Button(self.container, text="Reset", command=self.reset)
        self.reset_button.grid(column=1, row=7, padx=10, pady=5)

    def generate_password(self):
        password_length = int(self.password_length_entry.get())
        include_capital = self.capital_var.get()
        include_special = self.special_var.get()
        include_numbers = self.number_var.get()

        characters = ''.join(random.choice(string.ascii_lowercase) for _ in range(password_length))
        if include_capital:
            characters += ''.join(random.choice(string.ascii_uppercase) for _ in range(password_length))
        if include_special:
            characters += ''.join(random.choice(string.punctuation) for _ in range(password_length))
        if include_numbers:
            characters += ''.join(random.choice(string.digits) for _ in range(password_length))


        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_label.config(text="Generated Password: " + password)

    def copy_to_clipboard(self):
        password = self.password_label.cget("text").replace("Generated Password: ", "")
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update()
        messagebox.showinfo("Copied", "Password copied to clipboard.")

    def reset(self):
        self.username_entry.delete(0, "end")
        self.password_length_entry.delete(0, "end")
        self.password_length_entry.insert(0, "8")
        self.capital_var.set(0)
        self.special_var.set(0)
        self.number_var.set(0)
        self.password_label.config(text="Generated Password:")

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=330,height=300)
    app = PasswordGeneratorApp(root)
    root.mainloop()
