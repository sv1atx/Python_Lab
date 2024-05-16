tasks = []
priority_options = ["Високий", "Середній", "Низький"]
status_options = ["Нове", "У процесі", "Виконане"]

def add_task():
    title = input("Введіть назву завдання: ")
    description = input("Введіть опис завдання: ")
    
    print("Виберіть пріоритет:")
    for idx, option in enumerate(priority_options, start=1):
        print(f"{idx}. {option}")
    
    priority_choice = int(input("Ваш вибір: "))
    priority = priority_options[priority_choice - 1]
    
    status = "Нове"
    
    task = {"назва": title, "опис": description, "пріоритет": priority, "статус": status}
    tasks.append(task)
    tasks.sort(key=lambda x: (priority_options.index(x['пріоритет']), status_options.index(x['статус'])))
    print("Завдання додано успішно.")

def display_tasks():
    tasks.sort(key=lambda x: (priority_options.index(x['пріоритет']), status_options.index(x['статус'])))
    print("\nСписок завдань:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['назва']} ({task['статус']}) - {task['опис']} - Пріоритет: {task['пріоритет']}")

def edit_task():
    display_tasks()
    choice = int(input("Введіть номер завдання, яке бажаєте редагувати: ")) - 1
    
    if 0 <= choice < len(tasks):
        task = tasks[choice]
        print(f"\nРедагування завдання: {task['назва']}")
        
        task["назва"] = input("Введіть нову назву: ")
        task["опис"] = input("Введіть новий опис: ")
        
        print("Виберіть новий пріоритет:")
        for idx, option in enumerate(priority_options, start=1):
            print(f"{idx}. {option}")
        
        priority_choice = int(input("Ваш вибір: "))
        task["пріоритет"] = priority_options[priority_choice - 1]

        print("Виберіть новий статус:")
        for idx, option in enumerate(status_options, start=1):
            print(f"{idx}. {option}")
        
        status_choice = int(input("Ваш вибір: "))
        task["статус"] = status_options[status_choice - 1]
        
        print("Завдання відредаговано успішно.")
        
        tasks.sort(key=lambda x: (priority_options.index(x['пріоритет']), status_options.index(x['статус'])))
    else:
        print("Некоректний вибір.")

def delete_task():
    display_tasks()
    choice = int(input("Введіть номер завдання, яке бажаєте видалити: ")) - 1
    
    if 0 <= choice < len(tasks):
        task = tasks.pop(choice)
        print(f"Завдання '{task['назва']}' видалено успішно.")
    else:
        print("Некоректний вибір.")

def search_task():
    keyword = input("Введіть ключове слово для пошуку: ")
    
    found_tasks = [task for task in tasks if keyword.lower() in task['назва'].lower() or keyword.lower() in task['опис'].lower()]
    
    if found_tasks:
        print("\nРезультати пошуку:")
        for idx, task in enumerate(found_tasks, start=1):
            print(f"{idx}. {task['назва']} ({task['статус']}) - {task['опис']} - Пріоритет: {task['пріоритет']}")
    else:
        print("Завдань з введеним ключовим словом не знайдено.")

def main():
    while True:
        print("\nОберіть опцію:")
        print("1. Додати завдання")
        print("2. Переглянути завдання")
        print("3. Редагувати завдання")
        print("4. Видалити завдання")
        print("5. Пошук завдань")
        print("6. Вийти")
        
        choice = input("Ваш вибір: ")
        
        if choice == "1":
            add_task()
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            edit_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            search_task()
        elif choice == "6":
            print("Дякую за використання програми. До побачення!")
            break
        else:
            print("Некоректний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
