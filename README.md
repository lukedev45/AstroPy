# AstroPy

A lightweight astronomy utility package in Python for performing basic astrophysical calculations and data processing.

> ⚠️ **Note:** This project is **not** the official *Astropy* library (the community Python astronomy core package). This repository is a personal/educational project.

---

## 🚀 Overview

This repository contains a Python project that demonstrates astronomical computations and utilities such as:

- Physical constants and unit definitions  
- Structured logging mechanisms  
- A main executable script entry point  
- Project configuration via `pyproject.toml`

The goal of this project is to provide a clean foundation for building astronomy-related tools in Python while demonstrating good project structure and coding practices.

---

## 📁 Repository Structure

```text
AstroPy/
├── .gitignore
├── .python-version
├── README.md
├── constants.py       # Physical and astronomical constants
├── logger.py          # Logging setup
├── main.py            # Main program entry point
├── pyproject.toml     # Build and dependency configuration
└── uv.lock            # Dependency lock file
```

## Installation

# 1. Clone the repository
```bash
git clone https://github.com/lukedev45/AstroPy.git
cd AstroPy
```

# 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate   # macOS / Linux
.\venv\Scripts\activate    # Windows PowerShell
```

# 3. Install dependencies
```bash
pip install -r requirements.txt
```

