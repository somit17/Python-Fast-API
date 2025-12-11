import json
import os
FILE_NAME='tasks.json'


def print_Menu():
    """Show Main Menu"""
    print(f'1. Add a task')
    print(f'2. View all tasks ')
    print(f'3. Delete a task by id')
    print(f'0. Exit')
    print('==============================================')

def load_Tasks():
     if not os.path.exists(FILE_NAME):
         return []
     with open(FILE_NAME,mode='r') as json_reader:
         try:
             return json.load(json_reader)
         except json.JSONDecodeError:
             return []


def delete_Task(tasks):
    load_Tasks()
    idx = input(f'Delete task by id')
    if idx is None:
        return
    deleted_Task = tasks.pop(idx)
    save_tasks(tasks)
    print(f"Delete task successfully ! Description - {deleted_Task['description']}")

def main():
    tasks=load_Tasks()
    while True:
        print_Menu()
        choice = input(f'Choose an option')

        if choice=='0':
            print(f'GoodBye')
            break
        elif choice=='1':
            add_Task(tasks)
            break
        elif choice=='2':
            view_Tasks(tasks)
            break
        elif choice=='3':
            save_tasks(tasks)
            break
        elif choice=='4':
            delete_Task(tasks)
            break

def add_Task(tasks):
    print('Add a new task with description and priority')
    description = input(f'Please enter the description\n')
    if not  description:
        print(f'Description cannot be empty.')
        return
    priority = input(f'Please enter the priority\n')
    if priority not in ('high','low','medium'):
        print(f'Priority cannot be empty.By default it will be set to "LOW"')
        priority='low'

    task = {
        'description':description,
        'priority':priority,
        'isCompleted':False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f'Task Saved Successfully')


def save_tasks(tasks):
    with open(FILE_NAME,mode='w') as f:
        json.dump(tasks,f,indent=4)

def view_Tasks(tasks):
    if not tasks:
        print(f'No Tasks found !\n')
        return
    print('Tasks : ')
    for i,task in enumerate(tasks,start=1):
        print(f"{i} ) Status - {task['isCompleted']} ** Description  - {task['description']} ** Priority - {task['priority']}\n")




main()

