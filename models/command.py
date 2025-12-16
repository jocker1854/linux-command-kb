class CommandItem:
    def __init__(self, cid, command, description, usage):
        self.id = cid
        self.command = command
        self.description = description
        self.usage = usage

    def display_text(self):
        return f"{self.command}  —  {self.description}"
