garage_size = 0

garage_size = int(input("Enter garage size >> "))

cars = []
for i in range(garage_size):
    car = input(f"Enter car #{i + 1} >> ")
    cars.append(car)

while True:
    print("\n--- Garage ---")
    if cars:
        for i in range(garage_size):
            print(f"Car #{i + 1}: {cars[i]}")
    else:
        print("No cars in here!")

    print("\nWhat do you want to do next?")
    print("(add): add a new car\n(rm): remove a car\n(cr): clear all cars\n(st): sort all cars\n")

    option = input(">> ").lower()
    if option == "add":
        new_car = input("Enter the new car's name >> ")
        cars.append(new_car)
        garage_size += 1
    elif option == "rm":
        car_to_remove = input("Enter the exact car name to remove >> ")
        cars.remove(car_to_remove)
        garage_size -= 1
    elif option == "cr":
        cars.clear()
    elif option == "st":
        cars.sort()
