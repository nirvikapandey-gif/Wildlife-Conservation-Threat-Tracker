from species import land_animals
from species import aquatic_animals
from species import volant_animals
from threats import active_threats


def export_text():
    try:
        file= open("sanctuary_report.txt", "w")
        file.write("*********************************************\n")
        file.write(" OFFICIAL SANCTUARY AUDIT AND SECURITY REPORT \n")
        file.write("*********************************************\n\n")


            
        file.write("*** SPECIES INVENTORY ***\n")
       
        for animal, count in land_animals.items():
            file.write(f"- {animal}: {count} count\n")
       
       
        for animal, count in aquatic_animals.items():
            file.write(f"- {animal}: {count} count\n")
       
        for animal, count in volant_animals.items():
            file.write(f"- {animal}: {count} count\n")

        total_animals = sum(land_animals.values()) + sum(aquatic_animals.values()) + sum(volant_animals.values())
        
        
        file.write("\n*** TOTAL NUMBER OF ANIMALS ***\n")
        
        file.write(f"Total Monitored Individuals(Animals):- {total_animals}\n")
        
        file.write(f"Total Unique Species Logged:- {len(land_animals) + len(aquatic_animals) + len(volant_animals)}\n")
        
        
        file.write(f"Total Active Threat Alerts:- {len(active_threats)}\n")
        
        file.write("----------------------------------------------")





        file.write("\n*** RECENT ACTIVE THREATS ***\n")
        
        for t in active_threats:
            file.write(f"[{t['severity']}], Zone: {t['zone']}, Hazard: {t['hazard']}\n")

        
        

    
        file.write("\nReport generated and verified successfully.\n")

        file.close()


        print("File Backup Successful! 'sanctuary_report.txt' updated.")
    except Exception as e:
        print(f"Error writing report file: {e}")
