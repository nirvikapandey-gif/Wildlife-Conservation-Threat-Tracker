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

 USER INPUT LAYER             SYSTEM PROCESSING LAYER (CODE FILE & LOGIC)         TERMINAL DISPLAY LAYER
 ════════════════             ══════════════════════════════════════════         ══════════════════════
 
  [Type Option 1] ───► Runs:  dashboard.py ➔ display_dashboard() ───────────► ┌───────────────────────────┐
                              • Fetches land/aquatic/volant dict data         │ 📊 SANCTUARY ANALYTICS    │
                              • Sums total individual counts                  │ • Total Animals Logged    │
                              • Filters active threats for 'CRITICAL'         │ • High-Risk Patrol Zones  │
                                                                              └───────────────────────────┘
 
  [Type Option 2] ───► Runs:  species.py ➔ show_all() ──────────────────────► ┌───────────────────────────┐
                              • Iterates through categorized dicts            │ 🌾 CATEGORIZED CENSUS     │
                              │                                               │ • Land / Aquatic / Volant │
                              ▼                                               └───────────────────────────┘
                    Prompt:  "Would you like to modify/add a record? (Y/N)"
                              │
                              ├─► If 'N' ──► Loops back to Main Menu
                              │
                              └─► If 'Y' ──► Runs: species.update() ────────► ┌───────────────────────────┐
                                             • Input validation (try/except)  │ ✅ Data Saved Successfully│
                                             • Boundary verification (< 0)    │ • Re-prints updated list  │
                                             • dict[name] = count             └───────────────────────────┘
 
  [Type Option 3] ───► Runs:  threats.py ➔ view_threats() ──────────────────► ┌───────────────────────────┐
                              • Checks if active_threats list is empty        │ 🚨 RISK INCIDENT SHEET    │
                              • Iterates and numbers logged hazard dicts      │ 1. Sector A [CRITICAL]    │
                              │                                               └───────────────────────────┘
                              ▼
                    Prompt:  "Would you like to file a new threat? (Y/N)"
                              │
                              ├─► If 'N' ──► Loops back to Main Menu
                              │
                              └─► If 'Y' ──► Runs: threats.new_threat() ────► ┌───────────────────────────┐
                                             • Sanitation (.strip() / .upper()│ 🚨 Threat Appended!       │
                                             • list.append(new_alert)         │ • Automatically shows list│
                                                                              └───────────────────────────┘
 
  [Type Option 4] ───► Runs:  data_io.py ➔ export_text_report() ────────────► ┌───────────────────────────┐
                              • open("sanctuary_report.txt", "w")             │ 💾 File Backup Successful!│
                              • Stream writes formatted text strings          │ • Creates permanent text  │
                              • Executes file.close() boundary flush          │   document in workspace   │
                                                                              └───────────────────────────┘
 
  [Type Option 5] ───► Runs:  main.py ➔ run_application() ──────────────────► ┌───────────────────────────┐
                              • Automatically triggers data_io file export    │ 🔌 Saving backups...      │
                              • Executes the 'break' routing utility          │ • System shutdown clean.  │
                                                                              │   Goodbye!                │
                                                                              └───────────────────────────┘


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
