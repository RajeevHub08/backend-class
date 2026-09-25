from crud import addTask, viewTask

def mainLogic():

    while True:
        print("Press 1 for Add Task")
        print("Press 2 for View Task")
        print("Press 3 for Delete Task")
        print("Press 4 for Edit Task")
        print("Press 5 for Exit")

        try:
            user_choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Please enter valid integer choice")
        else:
            match user_choice:
                case 1: addTask()
                case 2: viewTask()
                case 3: pass
                case 4: pass
                case 5: pass

mainLogic()
                 