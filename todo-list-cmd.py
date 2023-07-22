def show(todos, display):
    """
    Enumerates and prints items of todo_list.
    :param todos: list of to-dos
    :param display: True if items should be displayed, else False.
    :return True, if list is empty
    :return False, if list is not empty
    """
    print('')
    if len(todos) == 0:
        print('Nothing here!')
        return True
    if not display:
        return False
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


def index_from_todo(todos, index_input):
    """
    Picks the index of the to-do to be edited/completed from the user. Checks if the index is valid and if there is any
    to-dos to be edited/completed.
    :param todos: list of to-dos
    :param index_input: index given from the user
    :return: False if index is invalid.
    :returns: the given index minus 1
    """
    if show(todos, False):
        return ''
    if not index_input.isnumeric():
        return ''
    todo_index = int(index_input)
    if todo_index > len(todos) or todo_index <= 0:
        return ''
    todo_index -= 1
    return todo_index


ERROR_MSG = "You must type a valid index or there isn't to-dos to be edited/completed. Please, try again."

with open('todos.txt', 'r') as todos_file:  # creates todo_list based on previous todos
    todo_list = todos_file.readlines()

print('🗹 TO-DO APP 🗹')

run = True
while run:
    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower().strip()

    if 'add' in user_input:
        todo_added = user_input[4:].capitalize() + '\n'

        todo_list.append(todo_added)
        update_file(todo_list)
        print(f'\nTo-do "{todo_added.strip()}" added!')

    elif 'show' in user_input:
        show(todo_list, True)

    elif 'edit' in user_input:

        edited_todo_index = index_from_todo(todo_list, user_input[5:])
        if edited_todo_index == '':
            print(ERROR_MSG)
            continue

        edited_todo = todo_list[edited_todo_index]
        new_todo_edit = input('\nEnter the new todo:\n > ').capitalize() + '\n'
        todo_list[edited_todo_index] = new_todo_edit
        update_file(todo_list)
        print(f'\n"{edited_todo.strip()}" changed to "{new_todo_edit.strip()}" successfully!"')

    elif 'complete' in user_input:

        completed_todo_index = index_from_todo(todo_list, user_input[9:])
        if completed_todo_index == '':
            print(ERROR_MSG)
            continue

        completed_todo = todo_list[completed_todo_index]
        todo_list.pop(completed_todo_index)
        update_file(todo_list)
        print(f'You completed "{completed_todo.strip()}"! Yay!!')

    elif 'exit' in user_input:
        break

    else:
        print(f'\nThe given command is unknown. Please, try again.')
