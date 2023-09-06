print("\n Here is your to-do list \n ")
todos = ["städa", "plugga", "handla", "ge blod"]
print(todos)

addtask = input("\n Add a task to the list \n")

if addtask in todos:
    print("These already exists in list")
else:
    confirm = input("Do you want to add task?(y/n) ").lower()
    if confirm == "y":
        todos.append(addtask)
        print("Task added to the list")
    else:
        print("Alright")
print("\nUpdated to-do list")
print(todos)
