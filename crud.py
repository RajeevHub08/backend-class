def addTask():
    try:
        with open("todo.txt", "x") as f:
            user_todo = input("Enter Task Name: ")
            f.write(user_todo)
            print("Todo Added Successfully")
    except FileExistsError:
        print("Error", FileExistsError)