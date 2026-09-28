<h1>
<img width="50" alt="Image" src="https://github.com/user-attachments/assets/d82f3cb7-3054-4c7c-bb6e-ec7944028906" />
Wildlife Conservation & Threat Tracker
</h1>

![Python](https://img.shields.io/badge/Python-3.14%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge&logo=github)
![License](https://img.shields.io/badge/License-MIT-2ea44f?style=for-the-badge)

A modular, terminal-based Command Line Interface (CLI) application developed in Python to track endangered animal populations and active environmental threats across sanctuary sectors.

## ⚙️ Core Technical Specifications

| Attribute | Specification Details |
| :--- | :--- |
| **Programming Language** | Python 3.10+ |
| **Interface Type** | Command Line Interface (CLI) |
| **Architecture Layout** | Multi-file Decoupled Modular Pattern (5 Backend Files) |
| **Primary Data Primitives**| Nested Python Dictionaries & Dynamic Lists |
| **External Dependencies** | None (Built entirely using native Python libraries) |
| **Data Export Format** | Formatted Flat Text Document (`sanctuary_report.txt`) |

## 🛠️ System Features & Functional Modules

The application is architected across separate logical files to maximize code cleanlines and fulfill software maintainability standards:

*   **Main Orchestration Core (`main.py`):** Drives a continuous, memory-buffered interactive selection loop (`Options 1–5`) with automated screen-clearing utilities to keep the terminal clean.
*   **Categorized Species Directory (`species.py`):** Manages distinct data records for **Land**, **Aquatic**, and **Volant** animals. Includes custom type-casting validators to stop string mismatch errors.
*   **Incident Threat Ledger (`threats.py`):** Logs real-time field hazards with location tracking, description text cleanup via sanitation commands, and multi-tier priority ranks (`LOW`, `MEDIUM`, `CRITICAL`).
*   **Analytics Aggregator (`dashboard.py`):** Pulls live cross-module data streams to calculate total animal counts, evaluate species diversity indexes, and flag high-risk coordinates needing immediate patrol.
*   **Data Serialization Engine (`data_io.py`):** Formats internal runtime structures into a beautifully aligned ASCII audit text report for permanent file backups.

## ⚙️ System Overview Diagram

```text
               🐾 WILDLIFE CONSERVATION CORE
                             │
                             ▼
                      💻 MAIN SYSTEM MENU
                             │
      ┌──────────────┬───────┴───────┬──────────────┐
      │              │               │              │
      ▼              ▼               ▼              ▼
 📊 Dashboard   🌾 Species       🚨 Threats      💾 File I/O
 (dashboard.py)  (species.py)    (threats.py)    (data_io.py)
                     │               │              │
                     ├─► Land        ├─► Alerts     └─► Exporter
                     ├─► Aquatic     ├─► Hazards        (Generates
                     └─► Volant      └─► Severity        report.txt)
```

---

## 🏗️ Project Directory Structure

```text
WILDLIFE CONSERVATION CORE/
│
│── main.py                           # Main menu interface & application router
│   ├── species.py                    # Handles land, aquatic, & volant inventories
│   ├── threats.py                    # Incident risk logger & active danger tracker
│   ├── dashboard.py                  # Analytical panel & high-risk zone visualizer
│   └── data_io.py                    # Simple storage management file exporter
│
├── 📂 data/                          # Permanent Storage Target Output Folder
│   └── sanctuary_report.txt          # Automatically generated text audit backup
│
├── 📄 statement.md                   # Formal structural scope definition document
└── 📄 README.md                      # Technical installation & test instruction sheet

```

---

## 📚 Core Software Engineering Concepts Used

```text
Python Implementation Blueprint
│
├── Modularity & Imports (Separation of concerns using multi-file linking)
│
├── Data Types & Storage
│   ├── int           # Menu options validation, population counts
│   ├── str           # Casing formatting, zone alerts data
│   ├── dict          # Categorized inventories (land, aquatic, volant)
│   └── list          # Dynamic chronological array holding active threats
│
├── Input / Output & Formatting
│   ├── input()       # User selection data capture handles
│   ├── print()       # Text UI grids drawing & title bars
│   └── f-strings     # Live dictionary variables interpolation inside text
│
├── Robust Error Validation Strategy
│   ├── try / except  # Catches ValueError letter typos on integer entries
│   ├── conditional   # Boundary evaluation rules preventing negative values
│   ├── .strip()      # String method sanitation removing edge blank spaces
│   └── .upper()      # String standardizer resolving letter casing variations
│
└── Loop Execution Mechanics
    ├── while True    # Persistent menu loop preventing premature crashes
    └── dict.items()  # Key-value extraction scanner used for category reading
```


## 🚀 Steps to Install & Run the Project

### 1. Prerequisites
Ensure you have **Python 3** installed on your system. You can verify this by opening your terminal and typing:
```bash
python --version
```

### 2. Setup the Workspace
Clone your repository or navigate directly into the project directory where your files are stored:
```bash
cd Wildlife-Conservation-Threat-Tracker
```

### 3. Execution Command
Launch the main application control loop by running the following command in your terminal:
```bash
python m
ain.py
```
*(Note: If you are running on macOS or Linux, use `python3 main.py` instead).*


## 🛠️ Features & Functional Modules
* **Dashboard Module (`dashboard.py`):** Aggregates sanctuary census numbers and highlights critical security alert zones.
* **Species Inventory Module (`species.py`):** Handles complete data processing for tracking and modifying animal counts.
* **Threat Tracker Module (`threats.py`):** Logs environmental or poaching hazards with assigned severity tiers.
* **Data I/O Module (`data_io.py`):** Exists as a backup utility to compile and output data into a formatted `sanctuary_report.txt` file.

## 🛡️ Non-Functional Strengths
* **Maintainability:** Written across 5 clean, highly distinct code files to comply with architectural rubric requirements.
* **Robust Error Handling:** Protects user inputs using structured conditional checks and type validation blocks to avoid execution crashes.
