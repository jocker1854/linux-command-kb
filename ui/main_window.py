import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class MainWindow:
    def __init__(self, root, handlers):
        self.handlers = handlers
        root.title("Linux Command Knowledge Base")
        root.geometry("1050x650")

        self.build_ui(root)

    def build_ui(self, root):
        top = tk.Frame(root)
        top.pack(fill=tk.X, padx=10, pady=5)

        tk.Label(top, text="Command").pack(side=tk.LEFT)
        self.command_entry = tk.Entry(top, width=25)
        self.command_entry.pack(side=tk.LEFT, padx=5)

        tk.Label(top, text="Description").pack(side=tk.LEFT)
        self.desc_entry = tk.Entry(top, width=30)
        self.desc_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(top, text="Add", command=self.handlers.add_command).pack(side=tk.LEFT)
        tk.Button(top, text="Delete", command=self.handlers.delete_command).pack(side=tk.LEFT)

        main = tk.Frame(root)
        main.pack(expand=True, fill=tk.BOTH, padx=10)

        left = tk.Frame(main)
        left.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(left, text="Search").pack()
        self.search_entry = tk.Entry(left)
        self.search_entry.pack(fill=tk.X)
        self.search_entry.bind("<KeyRelease>", self.handlers.search_commands)

        self.command_list = tk.Listbox(left, width=50)
        self.command_list.pack(fill=tk.Y, expand=True)
        self.command_list.bind("<<ListboxSelect>>", self.handlers.show_usage)

        right = tk.Frame(main)
        right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH, padx=10)

        tk.Label(right, text="How to use").pack()
        self.usage_text = ScrolledText(right)
        self.usage_text.pack(fill=tk.BOTH, expand=True)

        tk.Button(right, text="Run Command", command=self.handlers.run_command).pack()

        tk.Label(root, text="Output").pack()
        self.output_text = ScrolledText(root, height=10)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

    def clear_inputs(self):
        self.command_entry.delete(0, "end")
        self.desc_entry.delete(0, "end")
        self.usage_text.delete("1.0", "end")
