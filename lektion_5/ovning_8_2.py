todos = ["Städa", "Handla", "Plugga", "Ge blod", ]

print("Current tasks")
print(todos)

add_task = input("Add something to your to do list: ")
todos.append(add_task)
for task in todos:
    print("After change")
    print(task)

