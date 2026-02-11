#          DAY_5
# To-Do List program (add, remove, view tasks).
tasks = []

def display_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def add_task():
    task = input("Enter the task: ")
    tasks.append({"task": task})
    print(f"✅ Task '{task}' added successfully!")

def remove_task():
    if len(tasks) == 0:
        print("⚠️ No tasks to remove!")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']}")

    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed_task = tasks.pop(num - 1)
            print(f"🗑️ Task '{removed_task['task']}' removed successfully.")
        else:
            print("⚠️ Please enter a valid task number!")
    except ValueError:
        print("❌ Please enter a valid number.")

def view_tasks():
    if len(tasks) == 0:
        print("📭 No tasks added yet!")
    else:
        print("\n📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['task']}")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            remove_task()
        elif choice == "3":
            view_tasks()
        elif choice == "4":
            print("👋 Thanks for using the To-Do List. Goodbye!")
            break
        else:
            print("❌ Invalid choice! Please try again.")

main()