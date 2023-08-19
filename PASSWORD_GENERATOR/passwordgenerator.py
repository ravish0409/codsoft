import random
import string
import tkinter as tk
from tkinter import messagebox

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.username_label = tk.Label(root, text="Username:")
        self.username_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        self.username_entry = tk.Entry(root)
        self.username_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5)

        self.password_length_label = tk.Label(root, text="Password Length:")
        self.password_length_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        self.password_length_entry = tk.Entry(root)
        self.password_length_entry.grid(row=1, column=1, padx=10, pady=5)
        self.password_length_entry.insert(0, "8")

        self.capital_var = tk.IntVar()
        self.capital_check = tk.Checkbutton(root, text="Include Capital Letters", variable=self.capital_var)
        self.capital_check.grid(row=2, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.special_var = tk.IntVar()
        self.special_check = tk.Checkbutton(root, text="Include Special Characters", variable=self.special_var)
        self.special_check.grid(row=3, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.number_var = tk.IntVar()
        self.number_check = tk.Checkbutton(root, text="Include Numbers", variable=self.number_var)
        self.number_check.grid(row=4, column=0, columnspan=2, sticky="w", padx=10, pady=5)

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=5, column=0, padx=10, pady=10)

        self.password_label = tk.Label(root, text="Generated Password:")
        self.password_label.grid(row=6, column=0, columnspan=3, padx=10, pady=5)

        self.copy_button = tk.Button(root, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, padx=10, pady=5)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset)
        self.reset_button.grid(row=7, column=1, padx=10, pady=5)

    def generate_password(self):
        password_length = int(self.password_length_entry.get())
        include_capital = self.capital_var.get()
        include_special = self.special_var.get()
        include_numbers = self.number_var.get()

        characters = string.ascii_lowercase
        if include_capital:
            characters += string.ascii_uppercase
        if include_special:
            characters += string.punctuation
        if include_numbers:
            characters += string.digits

        if len(characters) == 0:
            messagebox.showerror("Error", "Please select at least one character type.")
            return

        password = ''.join(random.choice(characters) for _ in range(password_length))
        self.password_label.config(text="Generated Password: " + password)

    def copy_to_clipboard(self):
        generated_password = self.password_label.cget("text")
        password = generated_password.replace("Generated Password: ", "")
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
    app = PasswordGeneratorApp(root)
    root.mainloop()
