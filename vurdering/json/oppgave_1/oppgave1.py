import json
import matplotlib.pyplot as plt
import tabulate

def get_user_count(data) -> int:
    count = 0
    for user in data:
        if user["userId"] > count:
            count = user["userId"]
    return count

def get_tasks(data, completed) -> list:
    tasks = []
    for todo in data:
        if todo["completed"] == completed:
            tasks.append(todo)
    return tasks

def get_user_taskcount(data, find_max=True) -> int:
    tasks = get_tasks(data, completed=True)
    user_task_counts = {}
    for task in tasks:
        if task["userId"] in user_task_counts:
            user_task_counts[task["userId"]] += 1
        else:
            user_task_counts[task["userId"]] = 1

    if find_max:
        return max(user_task_counts, key=user_task_counts.get), max(user_task_counts)
    else:
        return user_task_counts
    
def task_graph(data):
    done = len(get_tasks(data, completed=True))
    not_done = len(get_tasks(data, completed=False))

    labels = f"Completed tasks: {done}", f"Not completed tasks: {not_done}"
    sizes = [done, not_done]
    
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')

    plt.show()

def user_graph(data):
    values = get_user_taskcount(data, find_max=False)
    labels = [f"UserID: {x}" for x in list(values.keys())]
    sizes = list(values.values())

    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.show()

def vaske_data(data):
    visited = []
    for i in range(len(data)-1):
        check = data[i]
        check["title"] = " ".join(check["title"].split())
        check["userId"] = int(check["userId"])
        if len(check["estimat"]) == 0:
            check["estimat"] = 3
        else:
            check["estimat"] = int(check["estimat"][:-1])

        if check in visited:
            data.remove(check)
        visited.append(check)

    return data

def main():
    with open('./oppgave_1/todos_oppgave1.json') as f:
        data = json.load(f)
        f.close()

    # vasker data
    data = vaske_data(data)

    # Finne antall brukere
    print(f"Det er {get_user_count(data)} antall brukere, {len(data)} oppgaver og {len(get_tasks(data, completed=True))} ferdige oppgaver\n")

    # skriv ut alle som ikke er ferdig
    values = get_tasks(data, completed=False)
    print(tabulate.tabulate(values, headers="keys"), "\n")

    # skriv ut alle som er ferdig
    values = get_tasks(data, completed=True)
    print(tabulate.tabulate(values, headers="keys"), "\n")

    # finne bruker med flest oppgaver gjort
    user, value = get_user_taskcount(data)
    print(f"Brukeren med flest oppgaver gjort er bruker {user} med {value} oppgaver gjort\n")

    # diagram over oppgaver
    task_graph(data)

    # diagram over brukere
    user_graph(data)

if __name__ == "__main__":
    main()