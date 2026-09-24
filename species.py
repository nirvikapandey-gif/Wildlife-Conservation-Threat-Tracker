<<<<<<< HEAD
# quick zoo inventory script
animals = {
    "Tiger": 12, 
    "Rhino": 5, 
    "Elephant": 24,
    "Leopard": 4, 
    "Panda": 21, 
    "Crocodile": 17
}

def show_all():
    print("\ncurrent inventory:")
    for a in animals:
        print(a, ":", animals[a])

def update_stock():
    name = input("\nAnimal to update: ")
    
    # just checking if it exists or adding it raw
    new_val = int(input("Enter new count: "))
    
    animals[name] = new_val
    print("updated!")
    show_all()

# let's run it
show_all()
update_stock()
=======
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
>>>>>>> 4a119142986d644b1463e494f066879e1d346490
