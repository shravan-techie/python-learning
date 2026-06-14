# Python-learning

This repo is to learn the Python language and keep small practice projects and notes.

## Structure

- `basics/` — small example scripts demonstrating core concepts (strings, numbers, types, etc.)

## Quick Start

1. (Optional) Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Running examples

- Run all type conversion examples (non-interactive):

```bash
python basics/TypeCoversion.py
```

- Run the interactive type-conversion demo (prompts for input):

```bash
python basics/TypeCoversion.py interactive
```

- Run the string examples:

```bash
python basics/String.py
```

## Notes

- The code provides safe fallbacks where external packages are optional (for easier debugging).
- Use the `interactive` flag only when you want to provide input; examples run non-interactively by default.

Contributions: feel free to add more examples or improve existing ones.
