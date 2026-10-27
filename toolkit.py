cat > toolkit.py <<'EOF'
# Personal Mini-Toolkit
# A menu-driven program containing three useful Python tools.

# Tool 1: Calculate the result of two numbers.
def simple_calculator():
    print("\n--- Simple Calculator ---")
    print("Operations: +  -  *  /")

    try:
        num1 = float(input("Enter the first number: "))
        operator = input("Enter an operation (+, -, *, /): ")
        num2 = float(input("Enter the second number: "))

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Sorry, division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operation. Please use +, -, *, or /.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Please enter valid numbers.")


# Tool 2: Manage a to-do list while the program is running.
def todo_list(tasks):
    while True:
        print("\n--- To-Do List ---")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Remove a task")
        print("4. Return to main menu")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task = input("Enter the task: ").strip()
            if task:
                tasks.append(task)
                print(f"Task added: {task}")
            else:
                print("Task cannot be empty.")

        elif choice == "2":
            if not tasks:
                print("Your to-do list is empty.")
            else:
                print("\nYour tasks:")
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

        elif choice == "3":
            if not tasks:
                print("There are no tasks to remove.")
            else:
                for number, task in enumerate(tasks, start=1):
                    print(f"{number}. {task}")

                try:
                    task_number = int(input("Enter the task number to remove: "))

                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f"Removed task: {removed_task}")
                    else:
                        print("That task number is not on the list.")

                except ValueError:
                    print("Please enter a valid whole number.")

        elif choice == "4":
            print("Returning to the main menu.")
            break

        else:
            print("Invalid choice. Please select a number from 1 to 4.")


# Tool 3: Check whether a whole number is even or odd.
def even_odd_checker():
    print("\n--- Even or Odd Checker ---")

    try:
        number = int(input("Enter a whole number: "))

        if number % 2 == 0:
            print(f"{number} is an even number.")
        else:
            print(f"{number} is an odd number.")

    except ValueError:
        print("Please enter a valid whole number.")


# Main program: repeat the menu until the user chooses to quit.
def main():
    tasks = []

    print("Welcome to Patrick's Personal Mini-Toolkit!")

    while True:
        print("\n=== PERSONAL MINI-TOOLKIT ===")
        print("1. Simple Calculator")
        print("2. To-Do List")
        print("3. Even or Odd Checker")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            simple_calculator()
        elif choice == "2":
            todo_list(tasks)
        elif choice == "3":
            even_odd_checker()
        elif choice == "4":
            print("Thank you for using the Personal Mini-Toolkit. Goodbye!")
            break
        else:
            print(f"Sorry, '{choice}' is not a valid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
EOF