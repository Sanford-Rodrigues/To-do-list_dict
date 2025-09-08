# To Do List project using Dictionary

# Project Overview
This is a simple application for managing tasks. It  allows user to add, delete, update & view tasks. Each  task contains a name, deadline, priority and status.

# Features

Create new tasks with a name, deadline, priority & status.

Display or veiw all tasks or filter them based on priority or status.

Modify tasks

The application ensures user input are in correct format

# How to use

1. Add task: Enter the details for a task

2. Delete task: Provide the name of the task you want to delete

3. Update task: Provide the name of the task you want update and select what you want update(name, deadline, priority or status).

4. Veiw task: Select if want to veiw all task  or filter it based on priority or status.

0. Exit: Exits/quits the application


# Code

`task()` is main function that runs the task manager.

Initialized an empty list `tasklist()` where all the dictionaries containing task details will be stored.

`total_task` ask user input for number of task that helps the `for` loop to iterate the loop until all tasks are entered and stored.

Using `while` loop to ask and validate the correct input from user for `Deadline`, `Priority` & `Status`

Used `map` and `split` function to validate the date for deadline is in correct format (YYYY-MM-DD)

`task_details` stores the task name, deadline, priority and status in a dictionaries, which later are add to tasklist using `append` function.

After taking user input for option to add, delete, update, veiw or exit, I have used `while` loop to iterate the loop until user select to exit the task manager.

The code to add a task is similar to initial code for adding and store task details.

For deleting a task, `for` loop checks through each dictionary in `tasklist` if the user input matches any of the `Task Name` and deletes the dictionaty using `dict.remove` function or else returns task not found.

Similarly, `for` loop looks through the dictionaries if task entered by user is available in any dictionaries and ask user for what the need to update task name, deadline, priority or status.

Veiw option uses `while` loop and conditional statement `if-elif` to take user input to view all task or filter by priority or status.

Lastly, if user selects to exit the task manager, the program prints "Exiting the task manager. Goodbye!".

