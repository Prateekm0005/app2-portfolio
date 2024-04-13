import functions

while True:
    user_action = input("type add, show, edit, complete, or exit:")
    user_action = user_action.strip()

    # if 'add':
    if user_action.startswith('add'):
        todo = user_action[4:].strip()
        todos = functions.get_todos()
        todos.append(todo + '\n')

        functions.write_todos(todos)

    # elif 'show':
    elif user_action.startswith('show'):
        todos = functions.get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}-{item}"
            print(row)

    # elif 'edit':
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number -= 1

            todos = functions.get_todos()

            print("here are the existing todos", todos)
            new_todo = input("enter the new todo:")
            todos[number] = new_todo + '\n'
            print("here is how it will be", todos)

            write_todos(todos)
        except:
            print("your command is not valid")
            user_action = input("type add, show, edit, complete, or exit:")
            user_action = user_action.strip()

    # elif 'complete':
    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        except:
            print("there is no item with that number")
            continue
            # elif 'exit':
    elif user_action.startswith('exit'):
        break

    else:
        print('command is invalid')

print("bye")
