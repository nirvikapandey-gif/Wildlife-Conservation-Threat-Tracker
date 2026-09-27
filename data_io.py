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

        file.write("\n--- RECENT ACTIVE THREATS ---\n")
        for t in active_threats:
            file.write(f"[{t['severity']}] Zone: {t['zone']} Hazard: {t['hazard']}\n")
                
        file.write("\nReport generated and verified successfully.\n")
        print("File Backup Successful! 'sanctuary_report.txt' updated.")
    except Exception as e:
        print(f"Error writing report file: {e}")