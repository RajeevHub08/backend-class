def addTask():
    user_task = input("Enter Task Name: ")
    try:
        with open("todo.txt", "a") as file:
            file.write(user_task + "\n")

        print("Todo Added Successfully")
    except FileExistsError:
        print("Error", FileExistsError)

def viewTask():
    try:
        with open("todo.txt", "r") as file:
            print(file.read())

    except FileExistsError:
        print("Error", FileExistsError)
