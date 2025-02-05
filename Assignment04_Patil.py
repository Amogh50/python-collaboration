#To do list 
tasks = []
#==============================================================================
# function that add tasks
def add_tasks():
    task_user = input("add a task:")
    tasks.append({"task": task_user, "Completed": False})
    print("Task " + task_user + " added successfully")
#==============================================================================
# function to view tasks
def view_tasks():
    if not tasks:
        print("No tasks available.\n")
        return
    print("\nTo-Do List:")
    for task in tasks:
        if task["completed"]:
            status = "Done"
        else:
            status = "Not Done"
        print(task +": " + status)
    print()
#==============================================================================
# function to mark tasks as complete
def mark_completed():
    view_tasks()
    task_number = int(input("Enter the task number to mark as completed: ")) -1
    #because array numbers start from 0
    tasks[task_number]["completed"] = True
    print("task "+str(task_number)+" marked as completed\n")
    while task_number>len(tasks) and task_number<0:
        print("invalid input, please enter an actual task number")
        task_number = int(input("Enter the task number to mark as completed: ")) -1
        #because array numbers start from 0
        tasks[task_number]["completed"] = True
        print("task "+str(task_number)+" marked as completed\n")
#==============================================================================
# function to delete task
def delete_task():
    view_tasks()
    task_number = int(input("Enter the task number to delete: ")) -1
    #because array numbers start from 0
    removed_task=tasks.pop[task_number]
    print("task "+removed_task+" removed\n")
    while task_number>len(tasks) and task_number<0:
        print("invalid input, please enter an actual task number")
        task_number = int(input("Enter the task number to delete: ")) -1
        #because array numbers start from 0
        removed_task=tasks.pop[task_number]
        print("task "+removed_task+" removed\n")
#==============================================================================
# function to do actions
def actions():
    while True:
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_tasks()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")
#==============================================================================
# Main function to invoke the two functions
def main():
    print("Executing Question 1:")
    actions() # Call the function for Question 1
#==============================================================================
# Invoke the main function
if __name__ == "__main__":
    main()
#============================================================================

            
     


    

