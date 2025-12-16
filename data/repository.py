import yaml
import os
from models.command import CommandItem

FILE_NAME = "commands.yaml"


class CommandRepository:
    def __init__(self):
        self.commands = []

    def load(self):
        self.commands.clear()
        if not os.path.exists(FILE_NAME):
            return

        with open(FILE_NAME, "r") as f:
            raw = yaml.safe_load(f) or []

        for item in raw:
            self.commands.append(
                CommandItem(
                    item["id"],
                    item["command"],
                    item.get("description", ""),
                    item.get("usage", "")
                )
            )

    def save(self):
        with open(FILE_NAME, "w") as f:
            yaml.dump(
                [
                    {
                        "id": c.id,
                        "command": c.command,
                        "description": c.description,
                        "usage": c.usage
                    }
                    for c in self.commands
                ],
                f,
                sort_keys=False
            )
