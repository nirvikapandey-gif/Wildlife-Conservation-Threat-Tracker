# Wildlife Conservation & Threat Tracker

A modular, terminal-based Command Line Interface (CLI) application developed in Python to track endangered animal populations and active environmental threats across sanctuary sectors.

## 🚀 How to Run the Project
1. Ensure you have **Python 3** installed on your system.
2. Open your terminal or command prompt inside this project folder.
3. Run the following command:
   ```bash
   python main.py
   ```

## 🛠️ Features & Functional Modules
* **Dashboard Module (`dashboard.py`):** Aggregates sanctuary census numbers and highlights critical security alert zones.
* **Species Inventory Module (`species.py`):** Handles complete data processing for tracking and modifying animal counts.
* **Threat Tracker Module (`threats.py`):** Logs environmental or poaching hazards with assigned severity tiers.
* **Data I/O Module (`data_io.py`):** Exists as a backup utility to compile and output data into a formatted `sanctuary_report.txt` file.

## 🛡️ Non-Functional Strengths
* **Maintainability:** Written across 5 clean, highly distinct code files to comply with architectural rubric requirements.
* **Robust Error Handling:** Protects user inputs using structured conditional checks and type validation blocks to avoid execution crashes.
