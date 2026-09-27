from species import land_animals
from species import aquatic_animals
from species import volant_animals
from threats import active_threats

def display_dashboard():
    print("\n******************************************************")
    print("      WILDLIFE CONSERVATION MANAGEMENT CORE    ")
    print("******************************************************")

    total_animals = sum(land_animals.values()) + sum(aquatic_animals.values()) + sum(volant_animals.values())
    print(f"Total Monitored Individuals(Animals):- {total_animals}")
    print(f"Total Unique Species Logged:- {len(land_animals) + len(aquatic_animals) + len(volant_animals)}")
    print(f"Total Active Threat Alerts:- {len(active_threats)}")
    print("----------------------------------------------")
    
    critical_zones = [threats['zone'] for threats in active_threats if threats['severity'] == 'CRITICAL']
    if critical_zones:
        print(f"HIGH RISK ZONES NEEDING PATROL RIGHTNOW:- {', '.join(critical_zones)}")
    else:
        print("No critical emergency response zones today.")
    print("----------------------------------------------")