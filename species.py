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