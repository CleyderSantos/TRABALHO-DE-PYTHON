import tkinter as tk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tarefas")

        self.tasks = []

        self.label_task = tk.Label(root, text="Tarefa:")
        self.label_task.pack()

        self.entry_task = tk.Entry(root)
        self.entry_task.pack()

        self.add_button = tk.Button(root, text="Adicionar Tarefa", command=self.add_task)
        self.add_button.pack()

        self.listbox_tasks = tk.Listbox(root)
        self.listbox_tasks.pack()

        self.remove_button = tk.Button(root, text="Remover Tarefa", command=self.remove_task)
        self.remove_button.pack()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_tasks_listbox()
            self.entry_task.delete(0, tk.END)

    def remove_task(self):
        selected_task_index = self.listbox_tasks.curselection()
        if selected_task_index:
            index = selected_task_index[0]
            del self.tasks[index]
            self.update_tasks_listbox()

    def update_tasks_listbox(self):
        self.listbox_tasks.delete(0, tk.END)
        for task in self.tasks:
            self.listbox_tasks.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()