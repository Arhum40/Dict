d = {}
while True:
    choice = input("Enter 'add' to add a name, 'get' to retrieve names, or 'exit' to stop: ").lower()

    if choice == 'exit':
        break
    elif choice == 'add':
        name = input("Enter a name: ")
        if name:
            if name[0] not in d:
                d[name[0]] = []
            d[name[0]].append(name)
            print(f"Added {name}. Current dictionary: {d}")
        else:
            print("Name cannot be empty.")
    elif choice == 'get':
        key = input("Enter the first letter to retrieve names: ")
        if key in d:
            print(f"Names starting with '{key}': {d[key]}")
        else:
            print(f"No names found starting with '{key}'.")
    else:
        print("Invalid action. Please enter 'add', 'get', or 'exit'.")