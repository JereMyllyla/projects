# A simple To-Do application, made with Python.

# Planned features:
#   Save tasks to a .JSON file
#   Add a task to the to-do list.
#   Display the current tasks in the to-do list.
#   Mark tasks as completed.
#   Mark tasks as uncompleted.
#   Remove tasks from the to-do list.
#   Empty the task list

import json
import time

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
    
def mark_task_done(task_id):
    tasks_to_do, _ = load_tasks_from_file(file_path)
    for task in tasks_to_do:
        if task["id"] == task_id:
            if task["completed"] == False:
                task["completed"] = True
                break
            else:
                task["completed"] = False
                break
    save_tasks_to_file(file_path, tasks_to_do)

def remove_task_from_list(task_id):
    tasks_to_do, _ = load_tasks_from_file(file_path)
    tasks_to_do = [task for task in tasks_to_do if task["id"] != task_id]
    save_tasks_to_file(file_path, tasks_to_do)
    
def view_tasks_in_list():
    tasks_to_do, max_id = load_tasks_from_file(file_path)
    for task in tasks_to_do:
        task_id = (task["id"])
        task_name = (task["task"])
        if (task["completed"]) == False:
            task_string = f"{task_id}: {task_name} [ ]"
            print(task_string)
        else:
            task_string = f"{task_id}: {task_name} [x]"
            print(task_string)

def delete_all_tasks():
    tasks_to_do, _ = load_tasks_from_file(file_path)
    tasks_to_do = []
    save_tasks_to_file(file_path, tasks_to_do)  

file_path = 'tasks.json'
tasks_to_do, max_id = load_tasks_from_file(file_path)

print("To-Do:")
view_tasks_in_list()
user_input = input("What to do? add, done, remove or exit: ")

while user_input != "exit":
    if user_input == "add":
        add_task_to_list()
    elif user_input == "done":
        try:
            id_to_done = int(input("What number did you do: "))
            mark_task_done(id_to_done)
        except:
            print("Please use integers only.")
    elif user_input == "remove":
        try:
            id_to_remove = int(input("What number to remove: "))
            remove_task_from_list(id_to_remove)
        except:
            print("Please use integers only.")
    elif user_input == "DELETE":
        print("WARNING! You are about to delete the whole list.")
        print("Re-type 'DELETE' to confirm, anything else to cancel.")
        delete_confirmation = input()
        if delete_confirmation == "DELETE":
            delete_all_tasks()
        else:
            print("Cancelled.")
    else:
        print("ERROR: Use one of the accepted keywords. (add, done, remove or exit).")
    print("To-Do:")
    view_tasks_in_list()         
    user_input = input("What to do? add, done, remove or exit: ")


print("Goodbye!")   
# A small delay before closing window.
time.sleep(2)