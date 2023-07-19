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
    Updates todos.txt file with new values of todo_list.
    :param todos: list of to-dos
    """
    with open('todos.txt', 'w') as todos_file_f:
        todos_file_f.writelines(todos)


"""
def todo_from_input():
    length = len(split_user_input)
    todo = ""
    for index in range(1, length):
        todo += split_user_input[index] + ' '
    return todo
"""

ERROR_MSG = '\nYou must type a number. Please, try again.'

with open('todos.txt', 'r') as todos_file:  # creates todo_list based on previous todos
    todo_list = todos_file.readlines()

print('🗹 TO-DO APP 🗹')

run = True
while run:
    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower().strip()
    # split_user_input = user_input.split()

    if 'add' in user_input:
        todo_added = user_input[4:]

        todo_list.append(todo_added)
        update_file(todo_list)
        print(f'To-do "{todo_added.strip()}" added!')

    elif 'show' in user_input:
        show(todo_list)

    elif 'edit' in user_input:
        empty_list = show(todo_list)
        if empty_list:
            continue

        chosen_todo_index = input('\nChoose an item to edit (type its number):\n > ')

        if not chosen_todo_index.isnumeric():
            print(ERROR_MSG)
            continue

        chosen_todo_index = int(chosen_todo_index) - 1
        # caso usuário digite um índice inválido
        # if chosen_todo_index > len(todo_list):
        #     print('')
        chosen_todo = todo_list[chosen_todo_index].strip()
        todo_edited = input('\nEnter the new todo:\n > ').capitalize() + '\n'
        todo_list[chosen_todo_index] = todo_edited
        update_file(todo_list)
        print(f'"{chosen_todo}" changed to "{todo_edited.strip()}" successfully!"')

    elif 'complete' in user_input:
        empty_list = show(todo_list)
        if empty_list:
            continue

        todo_completed_index = input('\nEnter the completed to-do (type its number):\n > ')

        if not todo_completed_index.isnumeric():
            print(ERROR_MSG)
            continue

        todo_completed_index = int(todo_completed_index) - 1
        todo_completed = todo_list[todo_completed_index].strip()
        todo_list.pop(todo_completed_index)
        update_file(todo_list)
        print(f'You completed "{todo_completed}"! Yay!!')

    elif 'exit' in user_input:
        break

    else:
        print(f'\nThe given command is unknown. Please, try again.')
