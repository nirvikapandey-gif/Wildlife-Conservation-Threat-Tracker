# Module 3: Aggregates data into a visual terminal panel

from species import animal_database
from threats import active_threats

def display_dashboard():
    """Generates a clean text-based matrix report of the sanctuary."""
    print("\n==============================================")
    print("      WILDLIFE CONSERVATION MANAGEMENT CORE    ")
    print("==============================================")
    
    # 1. Total population summary calculation
    total_animals = sum(animal_database.values())
    print(f"📊 Total Monitored Individuals: {total_animals}")
    print(f"🗃️ Total Unique Species Logged: {len(animal_database)}")
    print(f"⚠️ Total Active Threat Alerts: {len(active_threats)}")
    print("----------------------------------------------")
    
    # 2. Highlight critical risks directly in the loop
    critical_zones = [t['zone'] for t in active_threats if t['severity'] == 'CRITICAL']
    if critical_zones:
        print(f"🚨 HIGH RISK ZONES NEEDING PATROL: {', '.join(critical_zones)}")
    else:
        print("🟢 No critical emergency response zones today.")
    print("==============================================")
