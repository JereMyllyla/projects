# A simple To-Do application, made with Python.

# Planned features:
#   Save tasks to a .JSON file
#   Add a task to the to-do list.
#   Display the current tasks in the to-do list.
#   Mark tasks as completed.
#   Remove tasks from the to-do list.

import json

def load_tasks_from_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            tasks_to_do = json.load(json_file)
            max_id = max(task['id'] for task in tasks_to_do) if tasks_to_do else 0
        return tasks_to_do, max_id
    except FileNotFoundError:
        return [], 0

def save_tasks_to_file(file_path, tasks_to_do):
    with open(file_path, 'w') as json_file:
        json.dump(tasks_to_do, json_file, indent=2)

def add_task_to_list():
    task_to_add = input("What to add to list? ")
    tasks_to_do, max_id = load_tasks_from_file(file_path)
    new_task_id = max_id + 1
    json_to_add = {
        "id": new_task_id,
        "task": task_to_add,
        "completed": False
    }
    tasks_to_do.append(json_to_add)
    save_tasks_to_file(file_path, tasks_to_do)
    
def mark_task_done():
    to_mark_done = input("What did you do?")
    to_mark_done = to_mark_done[:-2]

def remove_task_from_list():
    to_remove = input("What to remove")
    tasks_to_do.remove(to_remove)

def view_tasks_in_list():
    tasks_to_do, max_id = load_tasks_from_file(file_path)
    for task in tasks_to_do:
        print(task)

file_path = 'tasks.json'

tasks_to_do, max_id = load_tasks_from_file(file_path)

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
        print("ERROR: use an accepted keyword!")     
    user_input = input("What to do? add, delete or view: ")


#save_tasks_to_file(file_path, tasks_to_do)
print("Goodbye")   
