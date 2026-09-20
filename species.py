# Module 1: Handles animal population inventory

# Initial data storage using a standard Python dictionary
animal_database = {
    "Bengal Tiger": 12,
    "Indian Rhino": 5,
    "Asian Elephant": 24
}

def view_species():
    """Prints all tracked animals and their current numbers."""
    print("\n--- Current Species Populations ---")
    if not animal_database:
        print("No species are currently tracked.")
        return
    for animal, count in animal_database.items():
        print(f"🐾 {animal}: {count} individuals remaining")

def update_population():
    """Adds a new species or changes the count of an existing one with input protection."""
    print("\n--- Update/Add Species Record ---")
    name = input("Enter species name: ").strip()
    if not name:
        print("❌ Error: Species name cannot be empty!")
        return
        
    try:
        count = int(input(f"Enter current population count for {name}: "))
        if count < 0:
            print("❌ Error: Population count cannot be negative!")
            return
        # Store or update the value in the dictionary
        animal_database[name] = count
        print(f"✅ Successfully updated {name} population to {count}.")
    except ValueError:
        print("❌ Error: Please enter a valid whole number for the count!")
