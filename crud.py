# Add task functionallity------
def addTask():
    user_task = input("Enter Task Name: ")
    try:
        with open("todo.txt", "a") as file:
            file.write(user_task + "\n")

        print("Todo Added Successfully")
    except FileExistsError:
        print("Error", FileExistsError)

# View task functionallity
def viewTask():
    try:
        with open("todo.txt", "r") as file:
            data = file.read().strip()
            arrdata= data.split("\n")
            for index, item in enumerate(arrdata, start=1):
                print(index, item)

    except FileExistsError:
        print("Error", FileExistsError)

# Edit Task Functionlity
def editTask():
    try:
        with open("todo.txt", "r") as file:
            data = file.read().strip()
            arrdata = data.split("\n")

            edit_task = input("Enter Task to Edit: ")
            if edit_task in arrdata:
                new_task = input("Enter New Task to Edit: ")
                idx = arrdata.index(edit_task)
                arrdata[idx] = new_task
                print(arrdata)
                result = "\n".join(arrdata)

                with open("todo.txt", "w") as file:
                    file.write(result)
                    print("Data Edit Successfully")
            else:
                print("Task not Found")
    
    except FileExistsError:
            print("Error", FileExistsError)
