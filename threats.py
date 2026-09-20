# Module 2: Tracks active environmental and poaching threats

# Data storage list to hold threat dictionaries
active_threats = [
    {"zone": "Sector A", "hazard": "Illegal Wire Snare Trap", "severity": "CRITICAL"},
    {"zone": "Sector C", "hazard": "Broken Perimeter Fencing", "severity": "MEDIUM"}
]

def view_threats():
    """Displays all current logged warnings."""
    print("\n🚨 --- Active Sanctuary Threats --- 🚨")
    if not active_threats:
        print("✅ No active threats reported in the sanctuary!")
        return
    for idx, t in enumerate(active_threats, 1):
        print(f"{idx}. [{t['severity']}] Zone: {t['zone']} | Threat: {t['hazard']}")

def file_new_threat():
    """Logs a new active threat warning into the system with validation."""
    print("\n--- Report New Threat Incident ---")
    zone = input("Enter affected Sanctuary Zone (e.g., Sector B): ").strip()
    hazard = input("Describe the threat/hazard: ").strip()
    severity = input("Enter Severity Level (LOW / MEDIUM / CRITICAL): ").strip().upper()
    
    if not zone or not hazard:
        print("❌ Error: Zone and Hazard details are mandatory fields!")
        return
    if severity not in ["LOW", "MEDIUM", "CRITICAL"]:
        print("⚠️ Invalid severity entered. Defaulting to MEDIUM.")
        severity = "MEDIUM"
        
    new_alert = {"zone": zone, "hazard": hazard, "severity": severity}
    active_threats.append(new_alert)
    print(f"🚨 Alert logged for {zone} successfully!")
