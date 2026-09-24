# Module 4: Handles generating the offline .txt data report

from species import animal_database
from threats import active_threats

def export_text_report():
    try:
        with open("sanctuary_report.txt", "w", encoding="utf-8") as file:
            file.write("==============================================\n")
            file.write(" OFFICIAL SANCTUARY AUDIT AND SECURITY REPORT \n")
            file.write("==============================================\n\n")
            
            file.write("--- SPECIES INVENTORY ---\n")
            for animal, count in animal_database.items():
                file.write(f"- {animal}: {count} count\n")
                
            file.write("\n--- RECENT ACTIVE THREATS ---\n")
            for t in active_threats:
                file.write(f"[{t['severity']}] Zone: {t['zone']} | Hazard: {t['hazard']}\n")
                
            file.write("\nReport generated and verified successfully.\n")
        print("💾 File Backup Successful! 'sanctuary_report.txt' updated.")
    except Exception as e:
        print(f"❌ Error writing report file: {e}")
