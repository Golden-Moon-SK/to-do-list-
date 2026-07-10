def task():
    tasks = []  # empty list
    print("------WELCOME TO THE TASK MANAGER------")
    
    total_tasks = int(input("Enter the number of tasks you want to add: "))
    for i in range(1, total_tasks + 1):
        task_name = input(f"Enter task {i} = ")
        tasks.append(task_name)
        
    print(f"\nToday's tasks are\n{tasks}\n")
    
    while True:
        operation = int(input("Enter 1 to add a task, 2 to update a task, 3 to delete a task, 4 to view tasks, and 5 to exit: "))
        
        if operation == 1:
            add = input("Enter the task you want to add: ")
            tasks.append(add)
            print(f"Task '{add}' added successfully.\n")
            
        elif operation == 2:
            updated_val = input("Enter the task you want to update = ")
            if updated_val in tasks:
                up = input("Enter the new task = ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print(f"Task '{up}' updated successfully.\n")
            else:
                print("Task not found.\n")
                
        elif operation == 3:
            del_val = input("Which task do you want to delete = ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"Task '{del_val}' deleted successfully.\n")
            else:
                print("Task not found.\n")
                
        elif operation == 4:
            print(f"\nToday's tasks are\n{tasks}\n")
            
        elif operation == 5:
            print("Closing the program...")
            break
            
        else:
            print("Invalid input. Please enter a valid operation number.\n")

# Call the function to run the program
task()
