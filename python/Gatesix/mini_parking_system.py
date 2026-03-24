parking = [0] * 20   

def show_menu():
    print("\n--- Parking System ---")
    print("1. Park automatically")
    print("2. Park in a specific slot")
    print("3. Remove car")
    print("4. Show parking status")
    print("5. Exit")

def show_status():
    print("\nParking Slots:")
    for index in range(20):
        print(f"Slot {index+1}: {parking[index]}")
    
    empty = parking.count(0)
    occupied = parking.count(1)
    
    print(f"\nEmpty slots: {empty}")
    print(f"Occupied slots: {occupied}")

while True:
    show_menu()
    choice = input("Enter choice: ")

    
    if choice == "1":
        parked = False
        for index in range(20):
            if parking[index] == 0:
                parking[index] = 1
                print(f"Car parked in slot {index+1}")
                parked = True
                break
        if not parked:
            print("Parking full!")

        show_status()

   
    elif choice == "2":
        slot = int(input("Enter slot number (1-20): ")) - 1
        
        if slot < 0 or slot >= 20:
            print("Invalid slot number!")
        elif parking[slot] == 1:
            print("Slot already occupied!")
        else:
            parking[slot] = 1
            print(f"Car parked in slot {slot+1}")

        show_status()

    
    elif choice == "3":
        slot = int(input("Enter slot number to free (1-20): ")) - 1
        
        if slot < 0 or slot >= 20:
            print("Invalid slot number!")
        elif parking[slot] == 0:
            print("Slot already empty!")
        else:
            parking[slot] = 0
            print(f"Slot {slot+1} is now free")

        show_status()

   
    elif choice == "4":
        show_status()

    
    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
