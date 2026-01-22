tasks = []
def add_task():
    name = input("Enter task name: ")
    priority = input("Enter priority (High/Medium/Low): ")

    task = {
        "name": name,
        "completed": False,
        "priority": priority
    }

    tasks.append(task)
    print("✅ Task added successfully!\n")
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return

    for index, task in enumerate(tasks):
        status = "✔" if task["completed"] else "✘"
        print(f"{index}. {task['name']} | Priority: {task['priority']} | Completed: {status}")
    print()
def remove_task():
    view_tasks()
    try:
        index = int(input("Enter task number to remove: "))
        tasks.pop(index)
        print("🗑 Task removed!\n")
    except:
        print("Invalid task number.\n")
def mark_completed():
    view_tasks()
    try:
        index = int(input("Enter task number to mark as completed: "))
        tasks[index]["completed"] = True
        print("🎉 Task marked as completed!\n")
    except:
        print("Invalid task number.\n")
def main():
    while True:
        print("=== Secret Agency Task Manager ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_completed()
        elif choice == "5":
            print("Mission Complete. Exiting...")
            break
        else:
            print("Invalid choice.\n")
main()
