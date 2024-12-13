# A simple To-Do application, made with Python.

# Features:
#   Save tasks to a .JSON file
#   Add a task to the to-do list.
#   Display the current tasks in the to-do list.
#   Mark tasks as completed.
#   Mark tasks as uncompleted.
#   Remove tasks from the to-do list.
#   Empty the task list.

import json
import time

#A function to load the information from tasks.json .
def load_tasks_from_file(file_path):
    try:
        with open(file_path, 'r') as json_file:
            tasks_to_do = json.load(json_file)
            max_id = max(task['id'] for task in tasks_to_do) if tasks_to_do else 0
        return tasks_to_do, max_id
    except FileNotFoundError:
        return [], 0

# A function to save the current state of the list to tasks.json .
def save_tasks_to_file(file_path, tasks_to_do):
    with open(file_path, 'w') as json_file:
        json.dump(tasks_to_do, json_file, indent=2)

# A function to add a new task to the list.
def add_task_to_list():
    task_to_add = input("Enter the task you want to add: ")
    tasks_to_do, max_id = load_tasks_from_file(file_path)
    new_task_id = max_id + 1
    json_to_add = {
        "id": new_task_id,
        "task": task_to_add,
        "completed": False
    }
    tasks_to_do.append(json_to_add)
    save_tasks_to_file(file_path, tasks_to_do)
    print(f"Task '{task_to_add}' added successfully!")

# A function to mark an unfinished task to finished or vice versa.    
def mark_task_done(task_id):
    tasks_to_do, _ = load_tasks_from_file(file_path)
    for task in tasks_to_do:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            status = "completed" if task["completed"] else "not completed"
            print(f"Task '{task['task']}' marked as {status}.")

    save_tasks_to_file(file_path, tasks_to_do)

# A function to delete a single task from the list.
def remove_task_from_list(task_id):
    tasks_to_do, _ = load_tasks_from_file(file_path)
    tasks_to_do = [task for task in tasks_to_do if task["id"] != task_id]
    save_tasks_to_file(file_path, tasks_to_do)

# A function to display the tasks to the user.    
def view_tasks_in_list():
    tasks_to_do, _ = load_tasks_from_file(file_path)
    if not tasks_to_do:
        print("No tasks available.")
    else:
        print("Here are your current tasks:")
        for task in tasks_to_do:
            task_id = task["id"]
            task_name = task["task"]
            status = "[x]" if task["completed"] else "[ ]"
            print(f"{task_id}: {task_name} {status}")

# A function to delete every task from the list.
def delete_all_tasks():
    tasks_to_do, _ = load_tasks_from_file(file_path)
    tasks_to_do = []
    save_tasks_to_file(file_path, tasks_to_do)  
    print("All tasks have been deleted.")

file_path = 'tasks.json'
tasks_to_do, max_id = load_tasks_from_file(file_path)

print("Welcome to your To-Do List!")
view_tasks_in_list()
user_input = input("Choose an action (add, done, remove, DELETE, or exit): ")

# The main loop
while user_input != "exit":
    if user_input == "add":
        add_task_to_list()
    elif user_input == "done":
        try:
            id_to_done = int(input("Enter the task ID you completed/unchecked: "))
            mark_task_done(id_to_done)
        except ValueError:
            print("ERROR: Please enter a valid task ID (integer).")
    elif user_input == "remove":
        try:
            id_to_remove = int(input("Enter the task ID to remove: "))
            remove_task_from_list(id_to_remove)
        except ValueError:
            print("ERROR: Please enter a valid task ID (integer).")
    elif user_input == "DELETE":
        print("WARNING: This will delete all tasks.")
        delete_confirmation = input("Type 'DELETE' to confirm, or anything else to cancel: ")
        if delete_confirmation == "DELETE":
            delete_all_tasks()
        else:
            print("Operation cancelled.")
    else:
        print("ERROR: Invalid action. Please choose from (add, done, remove, DELETE, or exit).")

    print("\nUpdated To-Do List:")
    view_tasks_in_list()         
    user_input = input("Choose an action (add, done, remove, DELETE, or exit): ")

print("Goodbye!")   
exit_input = input("Press enter to close the program...")