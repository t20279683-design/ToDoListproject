from rich import print
def taskslist():
    tasks = []
    inp = input("Choose lang RU or EN (Русский или Английский): ")
    if inp.lower() == "en":
        while True:
            print("")
            print(r"[red]1.[/red] [green]Add task[/green]")
            print(r"[blue]2.[/blue] [blue]Remove task[/blue]")
            print(r"[green]3[/green]. [red]Show tasks[/red]")
            print(r"4. [violet]Quit[/violet]")
            print(r"5. [blue4]Write All to file[/blue4]")
            print(r'6. [yellow]Show all tasks from file[/yellow]')
            print(r'7. [red]Clear file[/red]')
            print(r'8. [bright_green]Show our license[/bright_green]')
            num = input(r"Choice num: ")
            print("")
            if num == "1":
                task = input(r"Choice task to append: ")
                print('')
                tasks.append(task)
                print(f"Task [violet]\"{task}\"[/violet] has [bright_green]added[/bright_green] to list!")
            elif num == "2":
                task_to_del = input(r"What task you want to delete? ")
                print("")
                if task_to_del in tasks:
                    tasks.remove(task_to_del)
                    print(f"Task [violet]\"{task_to_del}\"[/violet] has been [red]removed[/red] from list!")
                else:
                    print("[red]Task not found[/red]")
            elif num == "3":
                if tasks == [] or tasks == None:
                    print("[red]No tasks detected[/red]")
                else:
                    for task in tasks:
                        print(fr'-{task}')
            elif num == "4":
                print("Program has been [red]closed[/red] correctly!",'\n')
                break
            elif num == "5":
                with open("tasks.txt",'w',encoding='utf-8') as f:
                    f.write("Tasks:" + '\n')
                    for index,task in enumerate(tasks,start=1):
                        f.write(f"{index}. -{task} \n")
                print(f"All has been written to [red]tasks.txt[/red]! \n")
            elif num == "6":
                try:
                    with open('tasks.txt','r',encoding='utf-8') as f:
                        c = f.read()
                    if c == None or c == "":
                        print(rf'[red]Tasks.txt has empty[/red]')
                    else:
                        print(c)
                except (FileNotFoundError):
                    with open('tasks.txt','w') as f:
                        f.write("")
                    print('[red]File tasks.txt no exists but it created now[/red]')
            elif num == "7":
                try:
                    with open('tasks.txt','r',encoding='utf-8') as f1:
                        c = f1.read()
                except (FileNotFoundError):
                    with open('tasks.txt','w',encoding='utf-8') as f:
                        f.write("")
                    print("[bright_green]File [red]tasks.txt[/red] has been created![/bright_green]")
                if c == None or c == "":
                    print('[red]tasks.txt[/red] has [blue]empty![/blue]')
                else:
                    with open('tasks.txt','w',encoding='utf-8') as f:
                        f.write("")
                    print("[red]tasks.txt[/red] has [bright_green]cleared[/bright_green]!")
            elif num == "8":
                with open("LICENSE",'r',encoding='utf-8') as f:
                    print("[red]License: [/red]")
                    print(f"[violet]{f.read()}[/violet]")
            else:
                print("[red]Invalid command[/red]")
    elif inp.lower() == "ru":
        while True:
            print("")
            print(r"[red]1.[/red] [green]Добавить задачу[/green]")
            print(r"[blue]2.[/blue] [blue]Убрать задачу[/blue]")
            print(r"[green]3[/green]. [red]Показать задачи[/red]")
            print(r"4. [violet]Выйти[/violet]")
            print(r"5. [blue4]Записать все в файл[/blue4]")
            print(r'6. [yellow]Показать все задачи из файла[/yellow]')
            print(r'7. [red]Очистить файл[/red]')
            print(r'8. [bright_green]Показать нашу лицензию[/bright_green]')
            num = input(r"Выберите пункт: ")
            print("")
            if num == "1":
                task = input(r"Введите задачу для добавления: ")
                print('')
                tasks.append(task)
                print(f"Задача [violet]\"{task}\"[/violet] была [bright_green]добавлена[/bright_green] в список!")
            elif num == "2":
                task_to_del = input(r"Какую задачу вы хотите убрать? ")
                print("")
                if task_to_del in tasks:
                    tasks.remove(task_to_del)
                    print(f"Задача [violet]\"{task_to_del}\"[/violet] была [red]убрана[/red] из списка!")
                else:
                    print("[red]Задача не обнаружена[/red]")
            elif num == "3":
                if tasks == [] or tasks == None:
                    print("[red]Не обнаружены задачи[/red]")
                else:
                    for task in tasks:
                        print(fr'-{task}')
            elif num == "4":
                print("Програма была [red]закрыта[/red] правильно!",'\n')
                break
            elif num == "5":
                with open("tasks.txt",'w',encoding='utf-8') as f:
                    f.write("Задачи:" + '\n')
                    for index,task in enumerate(tasks,start=1):
                        f.write(f"{index}. -{task} \n")
                print(f"Всё было записано в файл [red]tasks.txt[/red]! \n")
            elif num == "6":
                try:
                    with open('tasks.txt','r',encoding='utf-8') as f:
                        c = f.read()
                    if c == None or c == "":
                        print(rf'[red]Tasks.txt пустой![/red]')
                    else:
                        print(c)
                except (FileNotFoundError):
                    with open('tasks.txt','w') as f:
                        f.write("")
                    print('[red]Файл tasks.txt был создан![/red]')
            elif num == "7":
                try:
                    with open('tasks.txt','r',encoding='utf-8') as f1:
                        c = f1.read()
                except (FileNotFoundError):
                    with open('tasks.txt','w',encoding='utf-8') as f:
                        f.write("")
                    print("[bright_green]Файл [red]tasks.txt[/red] был создан![/bright_green]")
                if c == None or c == "":
                    print('[red]tasks.txt[/red][blue] Пустой[/blue]')
                else:
                    with open('tasks.txt','w',encoding='utf-8') as f:
                        f.write("")
                    print("[red]tasks.txt[/red] был [bright_green]очищен![/bright_green]!")
            elif num == "8":
                with open("LICENSE",'r',encoding='utf-8') as f:
                    print("[red]Лицензия: [/red]")
                    print(f"[violet]{f.read()}[/violet]")
            else:
                print("[red]Неправильная команда[/red]")
taskslist()
