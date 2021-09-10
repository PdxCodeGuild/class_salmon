import requests

# API - application programming interface (website for robots)

# url of a single todo item
# url = "https://jsonplaceholder.typicode.com/todos/5"

# url for a list of todo items
url = "https://jsonplaceholder.typicode.com/todos/"

# make an HTTP GET request to the url and save the HTTP response in a variable
response = requests.get(url)

# JSON - JavaScript Object Notation (JS's version of a dictionary)
# convert the response data from JSON to Python dictionary 
# using the .json() method of the response object
todo_list = response.json()


for todo in todo_list:
    output = f"""
    {todo['id']}. {todo['title']}
    Created by: {todo['userId']}
    Completed: {todo['completed']}
    """

    print(output)