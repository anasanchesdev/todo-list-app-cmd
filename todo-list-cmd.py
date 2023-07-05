def show(todos):
    """
    Enumerates and prints items of todo_list
    :param todos: list of to-dos
    """
    print('')
    if len(todos) == 0:
        print('Nothing here!')
    for index, todo in enumerate(todos):
        print(f'{index + 1}.', todo)
    print()


ERROR_MSG = '\nYou must type a number. Please, try again.'
todo_list = []
print('🗹 TO-DO APP 🗹')
run = True
while run:
    user_input = input('Type add, show, edit, complete or exit:\n > ').lower().strip()

    match user_input:
        case 'add':
            todo_added = input('Enter a todo:\n > ').capitalize()
            todo_list.append(todo_added)

        case 'show':
            show(todo_list)

        case 'edit':
            show(todo_list)
            chosen_todo_index = input('Choose an item to edit (type its number):\n > ')
            if not chosen_todo_index.isnumeric():
                print(ERROR_MSG)
                continue
            chosen_todo_index = int(chosen_todo_index) - 1
            todo_edited = input('Enter the new todo:\n > ').capitalize()
            todo_list[chosen_todo_index] = todo_edited

        case 'complete':
            show(todo_list)
            todo_completed = input('Enter the completed to-do (type its number):\n > ')
            if not todo_completed.isnumeric():
                print(ERROR_MSG)
                continue
            todo_completed = int(todo_completed) - 1
            todo_list.pop(todo_completed)

        case 'exit':
            break

        case _:
            print(f'"{user_input}" is an unknown command. Please, type again.')
