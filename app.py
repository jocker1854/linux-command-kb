#imports
import tkinter as tk
from data.repository import CommandRepository
from search.semantic import SemanticSearch
from ui.handlers import UIHandlers
from ui.main_window import MainWindow


repo = CommandRepository()
repo.load()

search = SemanticSearch()
search.build(repo.commands)

#application setup
root = tk.Tk()
handlers = UIHandlers(repo, search, None)
ui = MainWindow(root, handlers)
handlers.ui = ui

handlers.refresh(repo.commands)
root.mainloop()
