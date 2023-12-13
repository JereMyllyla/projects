# A simple To-Do application, made with Python.

# Planned features:
#   Add a task to the to-do list.
#   Display the current tasks in the to-do list.
#   Mark tasks as completed.
#   Remove tasks from the to-do list.

tasks_to_do = ["placeholder[]", "placeholder2[x]"]

def add_task_to_list():
    to_add = input("What to add to list?")
    to_add = to_add + "[]"
    tasks_to_do.append(to_add)

def mark_task_done():
    to_mark_done = input("What did you do?")
    to_mark_done = [to_mark_done[:-2]]

def remove_task_from_list():
    to_remove = input("What to remove")
    tasks_to_do.remove(to_remove)

def view_tasks_in_list():
    for task in tasks_to_do:
        print(task)



user_input = input("What to do? add, delete, view or exit: ")

while user_input != "exit":
    if user_input == "add":
        add_task_to_list()
    elif user_input == "done":
        mark_task_done()
    elif user_input == "delete":
        remove_task_from_list()
    elif user_input == "view":
        view_tasks_in_list()
    else:
        print("yee")     
    user_input = input("What to do? add, delete or view: ")

print("Goodbye")   
