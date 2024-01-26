import json

def print_tasks(data, completed=None):
    if completed == None:
        for task in data:
            print(f"{task['id']}: {task['title']}")

    if completed == True:
        for task in data:
            if task["completed"]:
                print(f"Completed {task['id']}: {task['title']}")
    
    if completed == False:
        for task in data:
            if not task["completed"]:
                print(f"Not completed {task['id']}: {task['title']}")

def most_tasks(data):
    max_userid = max(data, key=lambda x: x['id'])
    return max_userid['id']
    

def main():
    file_path = "./3/3B/todos.json"

    with open(file_path) as file:
        data = json.load(file)

    print_tasks(data, completed=True)

if __name__ == "__main__":
    main()