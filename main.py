from task_manager import TaskManager

def print_menu():
    print("\nWelcome to the Task Manager!\n")
    print("1. Add Task")
    print("2. List Tasks")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Exit\n")

def main():

    manager = TaskManager()

    while True:

        print_menu()

        try:

            choice = int(input("Choose an option (1-5): "))

            match choice:
                case 1:
                    description = input("Enter task description: ")
                    manager.add_task(description)
                case 2:
                    manager.list_tasks()
                case 3:
                    id = int(input("Enter task ID to complete: "))
                    manager.complete_task(id)
                case 4:
                    id = int(input("Enter task ID to delete: "))
                    manager.delete_task(id)
                case 5:
                    print("Exiting Task Manager. Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please select a valid option.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
