todo_list = []

while True:
    print("\nToDo App")
    print("1: Add Item")
    print("2: Show Items")
    print("3: Remove Item")
    print("4: Quit")
    choice = input("Choose an option: ")

    if choice == "1":
        item = input("Enter the item: ")
        todo_list.append(item)
        print(f"Added {item} to the list.")

    elif choice == "2":
        print("\nToDo List:")
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {item}")

    elif choice == "3":
        for i, item in enumerate(todo_list):
            print(f"{i+1}. {item}")
        item_no = int(input("Enter the number of the item to remove: "))
        if 1 <= item_no <= len(todo_list):
            print(f"Removed {todo_list.pop(item_no - 1)}.")
        else:
            print("Invalid item number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")

