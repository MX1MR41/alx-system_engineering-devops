#!/usr/bin/python3

"""
Module Name: my_module
Description: This module retrieves information about an employee's TODO list progress using the JSONPlaceholder API.
"""

import requests


def get_employee_todo_progress(employee_id):
    """
    Retrieves and displays the employee's TODO list progress.
    """
    # Make API request to fetch employee's TODO list
    response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

    if response.status_code == 200:
        todos = response.json()
        completed_tasks = []
        total_tasks = len(todos)

        # Iterate over the todos to find completed tasks and their titles
        for todo in todos:
            if todo.get("completed"):
                completed_tasks.append(todo.get("title"))

        # Display the progress information
        print(f"Employee EMPLOYEE_NAME is done with tasks({len(completed_tasks)}/{total_tasks}):")
        print(f"EMPLOYEE_NAME: John Doe")  # Replace with the actual employee name
        for task in completed_tasks:
            print(f"\t{task}")


if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
