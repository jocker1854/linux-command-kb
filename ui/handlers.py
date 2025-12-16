import subprocess
from tkinter import messagebox


class UIHandlers:
    def __init__(self, repo, search, ui):
        self.repo = repo
        self.search = search
        self.ui = ui
        self.visible = []

    def refresh(self, cmds):
        self.visible = cmds
        self.ui.command_list.delete(0, "end")
        for c in cmds:
            self.ui.command_list.insert("end", c.display_text())

    def add_command(self):
        cmd = self.ui.command_entry.get().strip()
        desc = self.ui.desc_entry.get().strip()
        usage = self.ui.usage_text.get("1.0", "end").strip()

        if not cmd or not usage:
            messagebox.showwarning("Missing Data", "Command and usage required")
            return

        self.repo.commands.append(
            type(self.repo.commands[0])(
                cmd.replace(" ", "_"), cmd, desc, usage
            )
        )

        self.repo.save()
        self.search.build(self.repo.commands)
        self.refresh(self.repo.commands)
        self.ui.clear_inputs()

    def delete_command(self):
        sel = self.ui.command_list.curselection()
        if not sel:
            return

        self.repo.commands.remove(self.visible[sel[0]])
        self.repo.save()
        self.search.build(self.repo.commands)
        self.refresh(self.repo.commands)

    def show_usage(self, _):
        sel = self.ui.command_list.curselection()
        if not sel:
            return

        self.ui.usage_text.delete("1.0", "end")
        self.ui.usage_text.insert("end", self.visible[sel[0]].usage)

    def run_command(self):
        sel = self.ui.command_list.curselection()
        if not sel:
            return

        cmd = self.visible[sel[0]].command
        self.ui.output_text.delete("1.0", "end")

        result = subprocess.run(
            cmd, shell=True, text=True,
            stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )

        self.ui.output_text.insert("end", result.stdout)
        if result.stderr:
            self.ui.output_text.insert("end", "\n[ERROR]\n" + result.stderr)

    def search_commands(self, _):
        query = self.ui.search_entry.get()
        results = self.search.search(query, self.repo.commands)
        self.refresh(results)
