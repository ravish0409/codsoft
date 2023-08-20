import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        
        self.tasks = []

        self.frame = tk.Frame(root)
        self.frame.pack(padx=20, pady=20)

        self.task_label = tk.Label(self.frame, text="Enter Task:", font=("Helvetica", 8))
        self.task_label.pack(anchor="w")

        self.task_entry = tk.Entry(self.frame, font=("Helvetica", 14))
        self.task_entry.pack(pady=10, fill=tk.BOTH, expand=True)

        add_button = tk.Button(self.frame, text="Add Task", font=("Helvetica", 12), command=self.add_task, bg="green", fg="white",border=3)
        add_button.pack(fill=tk.BOTH, expand=True)
        
        self.tasks_frame = tk.Frame(self.frame)  # New frame to hold tasks and delete controls
        self.tasks_frame.pack(pady=15, fill=tk.BOTH, expand=True)
        
        self.delete_label = tk.Label(self.tasks_frame, text="Select to remove the task:", font=("Helvetica", 10))
        self.delete_label.pack(anchor="w")
        
        self.task_listbox = tk.Listbox(self.tasks_frame, font=("Helvetica", 14), selectbackground="gray", selectborderwidth=3)
        self.task_listbox.pack(fill=tk.BOTH, expand=True)
        
        delete_button = tk.Button(self.frame, text="Delete Task", font=("Helvetica", 12), command=self.delete_task, bg="red", fg="white",border=3)
        delete_button.pack(fill=tk.BOTH, expand=True)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.tasks, start=1):
            self.task_listbox.insert(tk.END, f"{index}. {task}")

    def delete_task(self):
        selected_indices = self.task_listbox.curselection()
        if selected_indices:
            for index in selected_indices[::-1]:
                del self.tasks[index]
            self.update_task_list()
        else:
            messagebox.showwarning("Warning", "Please select task(s) to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(width=275, height=525)
    app = ToDoListApp(root)
    root.mainloop()
