def show(todos):
    """
    Enumerates and prints items of todo_list.
    :param todos: list of to-dos
    :returns True, if list is empty
    :returns False, if list is not empty
    """
    print('')
    if len(todos) == 0:
        print('Nothing here!')
        return True
    for index, todo in enumerate(todos):
        print(f'{index + 1}.', todo.strip())
        return False


def update_file(todos):
    """
    Updates todos.txt file with new values of raw todo_list.
    :param todos: list of to-dos
    """
    with open('todos.txt', 'w') as todos_file_f:
        todos_file_f.writelines(todos)


ERROR_MSG = '\nYou must type a number. Please, try again.'

with open('todos.txt', 'r') as todos_file:  # creates todo_list based on previous todos
    todo_list = todos_file.readlines()

print('🗹 TO-DO APP 🗹')

run = True
while run:
    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower().strip()

    match user_input:
        case 'add':
            todo_added = input('\nEnter a todo:\n > ').capitalize() + '\n'

            todo_list.append(todo_added)
            update_file(todo_list)

        case 'show':
            show(todo_list)

        case 'edit':
            empty_list = show(todo_list)
            if empty_list:
                continue

            chosen_todo_index = input('\nChoose an item to edit (type its number):\n > ')

            if not chosen_todo_index.isnumeric():
                print(ERROR_MSG)
                continue

            chosen_todo_index = int(chosen_todo_index) - 1
            todo_edited = input('\nEnter the new todo:\n > ').capitalize() + '\n'
            todo_list[chosen_todo_index] = todo_edited
            update_file(todo_list)

        case 'complete':
            empty_list = show(todo_list)
            if empty_list:
                continue

            todo_completed = input('\nEnter the completed to-do (type its number):\n > ')

            if not todo_completed.isnumeric():
                print(ERROR_MSG)
                continue

            todo_completed = int(todo_completed) - 1
            todo_list.pop(todo_completed)
            update_file(todo_list)

        case 'exit':
            break

        case _:
            print(f'\n"{user_input}" is an unknown command. Please, type again.')
