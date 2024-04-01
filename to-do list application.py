def display_menu():
    print("Todo List Menu:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as done")
    print("4. Delete task")
    print("5. Exit")

def add_task(tasks):
    task = input("Enter task: ")
    tasks[len(tasks) + 1] = {"task": task, "done": False}
    print("Task added successfully!")

def view_tasks(tasks):
    print("Tasks:")
    if not tasks:
        print("No tasks.")
    else:
        for index, task in tasks.items():
            print(f"{index}. {'[x]' if task['done'] else '[ ]'} {task['task']}")

def mark_task_done(tasks):
    task_number = int(input("Enter task number to mark as done: "))
    if task_number in tasks:
        tasks[task_number]["done"] = True
        print("Task marked as done.")
    else:
        print("Task not found.")

def delete_task(tasks):
    task_number = int(input("Enter task number to delete: "))
    if task_number in tasks:
        del tasks[task_number]
        print("Task deleted.")
    else:
        print("Task not found.")

def main():
    tasks = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_task_done(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
