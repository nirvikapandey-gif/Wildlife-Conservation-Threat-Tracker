# Module 2: Tracks active environmental and poaching threats

active_threats = [
    {"zone": "Sector A", "hazard": "Illegal Wire Snare Trap", "severity": "CRITICAL"},
    {"zone": "Sector C", "hazard": "Broken Perimeter Fencing", "severity": "MEDIUM"}
]

def view_threats():
    print("\n*** Active Sanctuary Threats ***")
    for idx, threats in enumerate(active_threats, 1):
        print(f"{idx}. Zone: {threats ['zone']} Threat: {threats ['hazard']}, [{threats ['severity']}]")

def file_new_threat():
    print("\n*** Report New Threat Incident ***")
    zone = input("Enter affected Sanctuary Zone (e.g., Sector B):- ")
    hazard = input("Describe the threat/hazard (e.g., Illegal Logging):- ")
    severity = input("Enter Severity Level (LOW / MEDIUM / CRITICAL):- ").upper()
    
    if not zone or not hazard:
        print("Error: Zone and Hazard details are mandatory fields!")
        return
    if severity not in ["LOW", "MEDIUM", "CRITICAL"]:
        print("Invalid severity entered. Defaulting to MEDIUM.")
        severity = "MEDIUM"
        
    new_alert = {"zone": zone, "hazard": hazard, "severity": severity}
    active_threats.append(new_alert)
    print(f"Logged threat for {zone} successfully!")
#view_threats()
#file_new_threat()
#view_threats()

