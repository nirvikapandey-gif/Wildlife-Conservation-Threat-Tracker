# 📄 Project Statement: Wildlife Conservation & Threat Tracker (CLI)

---

## 1. Problem Statement
Modern wildlife sanctuaries and national parks struggle to maintain immediate, unified records of endangered animal populations and active environmental threats (like illegal traps, logging, or perimeter breaches) without using overly complicated software. Existing enterprise packages require heavy graphical interfaces, constant internet connectivity, and advanced administrative training. 

There is an operational need for a lightweight, zero-dependency, terminal-based tracking application. This engine allows conservation field staff to quickly log species data, record zone hazards, and review a live sanctuary status dashboard directly from a command-line interface without system overhead.

---

## 2. Scope of the Project
This project is a pure terminal-based Command Line Interface (CLI) management engine. It focuses entirely on data tracking using native Python data structures (dictionaries and lists) without any graphical interfaces or external internet dependencies. The application ensures complete operational continuity by dividing core tasks into distinct code files, facilitating robust error validation and automatic report writing.

### 🏗️ Project Architecture Layout
```text
WILDLIFE CONSERVATION TRACKER/
│
├── 📄 main.py                # Main menu interface & continuous execution loop
├── 📄 species.py             # Stores land, aquatic, and volant animal records
├── 📄 threats.py             # Incident risk logger and active hazard alerts ledger
├── 📄 dashboard.py           # Analytical status summary aggregator panel
└── 📄 data_io.py             # Flat text file backup data exporter
```

---

## 3. Target Users
*   **Sanctuary Field Coordinators:** To monitor live census shifts and review daily security status summaries.
*   **Wildlife Conservation Officers & Rangers:** To quickly log localized environmental hazards discovered during patrols.
*   **Environmental Research Staff:** To export permanent flat-text data snapshots for offline audit reporting.


---


## 4. High-Level Features (Functional Modules)

The application provides four specialized functional modules matching your project's code files:
*   **Species Inventory Manager (`species.py`):** Handles complete data processing for tracking and modifying animal counts partitioned across distinct categories: Land, Aquatic, and Volant.
*   **Threat Alert Tracker (`threats.py`):** Logs environmental or poaching hazards with assigned severity tiers (`LOW`, `MEDIUM`, `CRITICAL`) and tracks affected sanctuary zones.
*   **Sanctuary Status Dashboard (`dashboard.py`):** Aggregates cross-module counts to calculate global individual totals, count unique logged records, and explicitly flag high-risk coordinates.
*   **Data Serialization Exporter (`data_io.py`):** Acts as a backup utility to compile volatile runtime memory structures and stream them directly into a permanent file on disk (`sanctuary_report.txt`) [filegen-via-code].

---

## 🗺️ Functional Operation Flowchart

This flowchart illustrates exactly how user inputs travel through the core system modules to perform data transactions:


```text
               🐾 WILDLIFE CONSERVATION CORE (main.py)
                             │
                             ▼
             💻 INTERACTIVE CLI MAIN MENU PROMPT
                             │
        ┌──────────────┬─────┴───────┬──────────────┐
        │              │             │              │
        ▼              ▼             ▼              ▼
   [Option 1]     [Option 2]    [Option 3]     [Option 4/5]
        │              │             │              │
        ▼              ▼             ▼              ▼
  dashboard.py     species.py    threats.py     data_io.py
 ┌───────────┐   ┌───────────┐ ┌───────────┐  ┌────────────┐
 │ Read Only │   │ show_all()│ │view_threat│  │ export_text│
 │ Analytics │   └─────┬─────┘ └─────┬─────┘  └─────┬──────┘
 └─────────────────────┼─────────────┼──────────────┘
                       │             │
                       ▼             ▼
                   update()     new_threat()
                 ┌──────────┐  ┌──────────┐
                 │ Modify / │  │ Append   │
                 │ Create   │  │ Dynamic  │
                 │ Record   │  │ Incident │
                 └────┬─────┘  └─────┬────┘
                      │              │
                      ▼              ▼
         ┌────────────────────────────────┐
         │🗃️ LOCAL RUNTIME MEMORY OBJECTS │
         │  (Python Dictionaries & Lists) │
         └────────────────────────────────┘
```



---



## 🛡️ Input Sanitation & Security Strategy


1.  **Defensive Space Trimming (`.strip()`):** Slices off accidental spacebar entries from text string queries (e.g., matching `"  Tiger  "` directly back to `"Tiger"`).
2.  **Casing Standardization (`.upper()`):** Resolves lowercase typing variations on categorical inputs (e.g., standardizing user inputs cleanly to `"CRITICAL"` or `"Y"`).
3.  ** Implemented via a custom loop tracker (`species.positive_int()`) to catch alphabet string entries typed into number boxes, completely eliminating terminal crash risks.
