land_animals={
    "Tiger": 12,  
    "Elephant": 24,
    "Rhino": 5,
    "Leopard": 4, 
    "Panda": 21, 
    "Crocodile": 17
}
aquatic_animals={
    "Dolphin": 15,
    "Shark": 8,
    "Whale": 3,
    "Octopus": 12,
    "Sea Turtle": 9,
    "Seahorse": 14
}
volant_animals={
    "Eagle": 10,
    "Parrot": 25,
    "Bat": 30,
    "Owl": 7,
    "Hummingbird": 18,
    "Falcon": 5 
}
def show_all():
    print("\ncurrent inventory:-")
    print("\n--- Land Animals ---")
    for a in land_animals:
        print(a, ":", land_animals[a])
    print("\n--- Aquatic Animals ---")
    for a in aquatic_animals:
        print(a, ":", aquatic_animals[a])
    print("\n--- Volant Animals ---")
    for a in volant_animals:
        print(a, ":", volant_animals[a])

def positive_int (x):
    a=input(x)
    while not a.isdigit()  or int(a)<=0:
        a= input("Enter a positive integer : ")
    return int(a)
def update():
    print("\nWhich type of animal would you like to update?")
    b=positive_int("\n 1. Land Animal, 2. Aquatic Animal, 3. Volant Animal:- ")
    name=input("\nAnimal to update:- ")
    value=positive_int("Enter new count:- ")

    if b==1:
          land_animals[name]=value
    elif b==2:
            aquatic_animals[name]=value
    elif b==3:
            volant_animals[name]=value
    else:
        print("Invalid choice!")
        return
    print("Updated Animals!")
    show_all()