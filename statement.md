# Project Statement: Wildlife Conservation & Threat Tracker (CLI)

## 1. Problem Statement
Wildlife sanctuaries struggle to keep immediate, unified records of endangered animal populations and active environmental threats (like illegal traps or fences) without using overly complicated software. There is a need for a lightweight, terminal-based tracking application that allows conservation field staff to quickly log species data, record zone hazards, and review an immediate sanctuary status dashboard directly from a command-line interface.

## 2. Scope of the Project
This project is a pure terminal-based Command Line Interface (CLI) management engine. It focuses entirely on data tracking using native Python data structures (dictionaries and lists) without any graphical interfaces or external internet dependencies. The application ensures complete operational continuity by dividing core tasks into five distinct code files, facilitating robust error validation and automatic report writing.

## 3. Target Users
* Sanctuary Field Coordinators
* Wildlife Conservation Officers
* Environmental Research Staff

## 4. High-Level Features (Three Functional Modules)
* **Species Population Manager:** Full terminal-driven operations to input animal types, update existing population counts, and view current sanctuary counts.
* **Threat Alert Tracker:** A dedicated system to register active environmental hazards or poaching threats by zone and classify their severity levels.
* **Sanctuary Status Dashboard:** A clean, ASCII text-formatted terminal dashboard that aggregates all local species data and highlights critical high-threat zones alongside an automatic backup file exporter.
