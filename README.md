cat > README.md <<'EOF'
# Personal Mini-Toolkit

## Project Description

The Personal Mini-Toolkit is a Python program developed for the PLP Week 8 Final Project. It provides three useful tools through a simple menu.

## Tools Included

1. Simple Calculator: Adds, subtracts, multiplies, and divides two numbers.
2. To-Do List: Allows users to add, view, and remove tasks.
3. Even or Odd Checker: Determines whether a whole number is even or odd.

## Files

- toolkit_plan.txt: Contains the project plan, menu design, and concepts.
- toolkit.py: Contains the complete Python program.
- screenshots/: Contains screenshots showing the menu and tools in action.

## How to Run

1. Install Python 3.
2. Open Git Bash or a terminal in the project folder.
3. Run the command:

   python toolkit.py

4. Select a menu option from 1 to 4 and follow the instructions.

## Python Concepts Practiced

Variables, input, data types, type conversion, functions, lists, loops, conditionals, exception handling, comments, and f-strings.

## Reflection

The hardest part of this project was organizing the tools so that they work correctly through one menu. The part that required the most careful testing was handling invalid user input without crashing the program. I used try and except to handle invalid number entries. I also learned how a list can store tasks and change while a program is running. The menu loop helped me understand how to repeat actions until the user chooses to quit. I tested the calculator, to-do list, even or odd checker, invalid menu choices, and quit option. If I had one more week, I would add a number-guessing game and a feature to save tasks in a file.
EOF