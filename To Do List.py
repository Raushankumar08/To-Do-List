import os
import json

# Function to load tasks from a JSON file
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
        return tasks
    else:
        return []

# Function to save tasks to a JSON file
def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)

# Function to display tasks
def display_tasks(tasks):
    print("\n*** To-Do List ***")
    if not tasks:
        print("No tasks.")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. [{task['status']}] {task['title']}")

# Function to create a new task
def create_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "status": "Not Done"})
    save_tasks(tasks)
    print("Task added!")

# Function to update the status of a task
def update_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter task number to update: ")) - 1
    if 0 <= task_num < len(tasks):
        tasks[task_num]["status"] = "Done"
        save_tasks(tasks)
        print("Task updated!")
    else:
        print("Invalid task number.")

# Main function
def main():
    tasks = load_tasks()

    while True:
        print("\n1. Display tasks")
        print("2. Create task")
        print("3. Update task")
        print("4. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            create_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select again.")

if _name_ == "_main_":
    main()
