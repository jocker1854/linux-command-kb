# Linux Command Knowledge Base

A desktop application to store, search, and run Linux commands with usage instructions.  
Built with **Python**, **Tkinter**, and **scikit-learn** for semantic search.

---

## Features

- Add, delete, and run Linux commands.
- View detailed usage instructions.
- Search commands using natural language (semantic search).
- Supports YAML-based storage (`commands.yaml`).
- Modular OOP structure for easy scalability.

---

## Project Structure
```powershell
linux_command_kb/
│
├── app.py # Entry point
├── commands.yaml # Command storage
├── models/
│ └── command.py
├── data/
│ └── repository.py
├── search/
│ └── semantic.py
├── ui/
│ ├── main_window.py
│ └── handlers.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

1. Clone the repo:
```bash
git clone <your-repo-url>
cd linux_command_kb
```

2. Create a virtual environment(optional)
```bash
python3 -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

# Usage
```bash
python app.py
```

# YAML Structure
```yaml
- id: list_files
  command: "ls -l"
  description: "List files with details"
  usage: |
    ls -l
    Shows file permissions, owner, size, and timestamp.
```
