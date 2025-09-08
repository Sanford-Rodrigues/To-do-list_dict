def task():
    #Empty list to store tasks
    tasklist = []
    print("Welcome to task manager")

    #asking user input for number of tasks
    total_task = int(input("Enter the number of tasks you want to add: "))

    for i in range(total_task):
        task_name = input(f"Enter the name of the task{i+1}: ")
        while True:
            task_deadline = input("Enter the deadline of the task (YYYY-MM-DD): ")
            try:
                #splitting the date for check valid input from user using map and split function
                year, month, day = map(int, task_deadline.split('-'))
                if 1 <= month <= 12 and 1 <= day <= 31:
                    break
                else:
                    print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")
            except ValueError:
                print("Invalid format. Please enter the date in the format YYYY-MM-DD")

        while True:
            task_priority = input("Enter the priority of the task (High/Medium/Low): ")
            try:
                #checking the valid input from user to avoid further confusion when sorting or updating task
                if task_priority in ["High", "Medium", "Low"]:
                    break
                else:
                    print("Invalid priority. Please enter either 'High', 'Medium', or 'Low'.")
            except ValueError:
                print("Invalid input. Please enter either 'High', 'Medium', or 'Low'.")

        while True:
            task_status = input("Enter the status of the task (Pending/Completed):  ")
            try:
                #checking the valid input from user to avoid further confusion when sorting or updating task
                if task_status in ["Pending", "Completed"]:
                    break
                else:
                    print("Invalid status. Please enter either 'Pending' or 'Completed'.")
            except ValueError:
                print("Invalid input. Please enter either 'Pending' or 'Completed'.")
        print(" ")
        #storing task details in dictonary
        task_details = {
            "Task Name": task_name,
            "Deadline": task_deadline,
            "Priority": task_priority,
            "Status": task_status
        }
        #adding task details to tasklist using list of dictioneries
        tasklist.append(task_details)

    print("\nHere is your task list:")
    for t in tasklist:
        print(f"Task Name: {t['Task Name']}\nDeadline: {t['Deadline']}\nPriority: {t['Priority']}\nStatus: {t['Status']}\n" "\n")  
    
    while True:
        try:
            print("1.Add task\n2.Delete task\n3.Update task\n4.View task\n0.Exit")
            option = int(input("Select an option: \n"))

            if option == 1:
                task_name = input("Enter the name of the task: ")
                while True:
                    task_deadline = input("Enter the deadline of the task (YYYY-MM-DD): ")
                    try:
                        year, month, day = map(int, task_deadline.split('-'))
                        if 1 <= month <= 12 and 1 <= day <= 31:
                            break
                        else:
                            print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")
                    except ValueError:
                        print("Invalid format. Please enter the date in the format YYYY-MM-DD")
                while True:
                    task_priority = input("Enter the priority of the task (High/Medium/Low): ")
                    try:
                        if task_priority in ["High", "Medium", "Low"]:
                            break
                        else:
                            print("Invalid priority. Please enter either 'High', 'Medium', or 'Low'.")
                    except ValueError:
                        print("Invalid input. Please enter either 'High', 'Medium', or 'Low'.")
                while True:
                    task_status = input("Enter the status of the task (Pending/Completed):  ")
                    try:
                        if task_status in ["Pending", "Completed"]:
                            break
                        else:
                            print("Invalid status. Please enter either 'Pending' or 'Completed'.")
                    except ValueError:
                        print("Invalid input. Please enter either 'Pending' or 'Completed'.")
                print(" ")
                task_details = {
                    "Task Name": task_name,
                    "Deadline": task_deadline,
                    "Priority": task_priority,
                    "Status": task_status
                }
                tasklist.append(task_details)
                print("Task added successfully!\n")

            elif option == 2:
               task_delete=input("Enter the name of the task you want to delete: ")
               for t in tasklist:
                     if t["Task Name"]==task_delete:
                          tasklist.remove(t)
                          print("Task deleted successfully!\n")
                          break
                     else:
                            print("Task not found!\n")
                            break

            elif option == 3:
                task_update = input("Enter the name of the task you want to update: ")
                for t in tasklist:
                    if t["Task Name"] == task_update:
                        print("What do you want to update?\n1.Task Name\n2.Deadline\n3.Priority\n4.Status")
                        update_option = int(input("Select an option: \n"))
                        if update_option == 1:
                            new_name = input("Enter the new name of the task: ")
                            t["Task Name"] = new_name
                            print("Task name updated successfully!\n")
                        elif update_option == 2:
                            while True:
                                new_deadline = input("Enter the new deadline of the task (YYYY-MM-DD): ")
                                try:
                                    year, month, day = map(int, new_deadline.split('-'))
                                    if 1 <= month <= 12 and 1 <= day <= 31:
                                        t["Deadline"] = new_deadline
                                        print("Task deadline updated successfully!\n")
                                        break
                                    else:
                                        print("Invalid date. Please enter a valid date in the format YYYY-MM-DD.")
                                except ValueError:
                                    print("Invalid format. Please enter the date in the format YYYY-MM-DD")
                        elif update_option == 3:
                            while True:
                                new_priority = input("Enter the new priority of the task (High/Medium/Low): ")
                                try:
                                    if new_priority in ["High", "Medium", "Low"]:
                                        t["Priority"] = new_priority
                                        print("Task priority updated successfully!\n")
                                        break
                                    else:
                                        print("Invalid priority. Please enter either 'High', 'Medium', or 'Low'.")
                                except ValueError:
                                    print("Invalid input. Please enter either 'High', 'Medium', or 'Low'.")
                        elif update_option == 4:
                            while True:
                                new_status = input("Enter the new status of the task (Pending/Completed):  ")
                                try:
                                    if new_status in ["Pending", "Completed"]:
                                        t["Status"] = new_status
                                        print("Task status updated successfully!\n")
                                        break
                                    else:
                                        print("Invalid status. Please enter either 'Pending' or 'Completed'.")
                                except ValueError:
                                    print("Invalid input. Please enter either 'Pending' or 'Completed'.")
                        else:
                            print("Invalid option!\n")
                        break
                    else:
                        print("Task not found!\n")
                        break
            elif option == 4:
                print("\nHere is your task list:")
                for t in tasklist:
                    print(f"Task Name: {t['Task Name']}\nDeadline: {t['Deadline']}\nPriority: {t['Priority']}\nStatus: {t['Status']}\n" "\n")

                while True:
                    try:
                        print("1.View all tasks\n2.View tasks by status\n3.View tasks by priority")
                        view_option = int(input("Select an option: \n"))
                        if view_option == 1:
                            print("\nHere is your task list:")
                            for t in tasklist:
                                print(f"Task Name: {t['Task Name']}\nDeadline: {t['Deadline']}\nPriority: {t['Priority']}\nStatus: {t['Status']}\n" "\n")
                            break
                        elif view_option == 2:
                            status_option = input("Enter the status of the tasks you want to view (Pending/Completed): ")
                            print(f"\nHere are your {status_option} tasks:")
                            for t in tasklist:
                                if t["Status"] == status_option:
                                    print(f"Task Name: {t['Task Name']}\nDeadline: {t['Deadline']}\nPriority: {t['Priority']}\nStatus: {t['Status']}\n" "\n")
                            break
                        elif view_option == 3:
                            priority_option = input("Enter the priority of the tasks you want to view (High/Medium/Low): ")
                            print(f"\nHere are your {priority_option} priority tasks:")
                            for t in tasklist:
                                if t["Priority"] == priority_option:
                                    print(f"Task Name: {t['Task Name']}\nDeadline: {t['Deadline']}\nPriority: {t['Priority']}\nStatus: {t['Status']}\n" "\n")
                            break
                        else:
                            print("Invalid option!\n")
                    except ValueError:
                        print("Invalid input! Please enter a number.\n")

            elif option == 0:
                print("Exiting the task manager. Goodbye!")
                break

            else:
                print("Invalid option!\n")

        except ValueError:
            print("Invalid input! Please enter a number.\n")


task()
