def main():
    tasks = []  # Our temporary task storage

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            new_task = input("\nEnter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty!")
                
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to delete!")
                continue
            
            # Show tasks first so the user knows the index numbers
            print("\nYour Current Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("\nEnter the number of the task to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    print(f"Successfully deleted: '{removed}'")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()



import json
import os

FILENAME = "todo_list.json"

def load_tasks():
    """Loads tasks from a JSON file, or returns an empty list if the file doesn't exist."""
    if not os.path.exists(FILENAME):
        return []
    try:
        with open(FILENAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []  # Return empty list if the file is corrupted

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

def main():
    tasks = load_tasks()  # Load saved tasks at startup

    while True:
        print("\n--- PERSISTENT TO-DO LIST ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            if not tasks:
                print("\nYour to-do list is empty!")
            else:
                print("\nYour Current Tasks:")
                for index, task in enumerate(tasks, 1):
                    print(f"{index}. {task}")
                    
        elif choice == "2":
            new_task = input("\nEnter the task description: ").strip()
            if new_task:
                tasks.append(new_task)
                save_tasks(tasks)  # Save instantly
                print(f"Added: '{new_task}'")
            else:
                print("Task cannot be empty!")
                
        elif choice == "3":
            if not tasks:
                print("\nNo tasks to delete!")
                continue
                
            print("\nYour Current Tasks:")
            for index, task in enumerate(tasks, 1):
                print(f"{index}. {task}")
                
            try:
                task_num = int(input("\nEnter the number of the task to delete: "))
                if 1 <= task_num <= len(tasks):
                    removed = tasks.pop(task_num - 1)
                    save_tasks(tasks)  # Save configuration changes
                    print(f"Successfully deleted: '{removed}'")
                else:
                    print("Invalid task number!")
            except ValueError:
                print("Please enter a valid number.")
                
        elif choice == "4":
            print("\nProgress saved. Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()
