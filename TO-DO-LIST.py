tasks = []
running = True
while running:
    print("\--- TO-DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for index in range(len(tasks)):
                task = tasks[index]
                if task[1]:
                    status = "Done"
                else:
                    status = "Not Done"
                print(f"{index + 1}. {task[0]} [{status}]")

    elif choice == "2":
        task_name = input("Enter task: ")
        tasks.append([task_name, False])
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            task_num = int(input("Enter task number to mark as done: "))
            if 0 < task_num <= len(tasks):
                tasks[task_num - 1][1] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 0 < task_num <= len(tasks):
                deleted = tasks.pop(task_num - 1)
                print("Deleted task: " + deleted[0])
            else:
                print("Invalid task number.")

    elif choice == "5":
        print("Thankyou for using!")
        running = False
    else:
        print("Invalid choice.")
