import species
import threats
import dashboard
import data_io
def run_application():
    while True:
        print("\n*** MAIN TERMINAL SYSTEM MENU ***")
        print("1. View Sanctuary Status Dashboard")
        print("2. View and Update Animal Populations")
        print("3. View and Report Area Threat Alerts")
        print("4. Save System Report to Text File")
        print("5. Exit Application")
        
        choice=species.positive_int("Enter selection index (1-5):- ")
        
        if choice==1:
            dashboard.display_dashboard()
        elif choice==2:
            species.show_all()
            print("\nWould you like to modify or add a record?")
            sub_choice = input("(Y/N): ").strip().upper()
            if sub_choice=="Y":
                species.update()
            species.show_all
        elif choice==3:
            threats.view_threats()
            print("\nWould you like to file a new threat alert?")
            sub_choice = input("(Y/N): ").strip().upper()
            if sub_choice=="Y":
                threats.new_threat()
                threats.view_threats()
        elif choice==4:
            data_io.export_text()
        elif choice==5:
            print("\nSaving data backups before shutdown.")
            data_io.export_text()
            print("System shutting down securely. Goodbye!")
            break
        else:
            print("Invalid entry! Please type a number between 1 and 5.")
if __name__ == "__main__":
    run_application()