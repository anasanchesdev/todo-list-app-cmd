def show(todos):
    """
    Enumerates and prints items of todo_list
    """
    print('')
    if len(todos) == 0:
        print('Nothing here!')
    for index, todo in enumerate(todos):
        print(f'{index + 1}.', todo)


def number_to_str(number):
    """
    Converts safely a number to string and then subtracts 1.
    :param number: number in string
    :return: number in integer - 1
    """
    if number.isnumeric():
        number = int(number) - 1
        return number


todo_list = []
print('🗹 TO-DO APP 🗹')
while True:
    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower().strip()

    match user_input:
        case 'add':
            todo_added = input('Enter a todo:\n > ').capitalize()
            todo_list.append(todo_added)

        case 'show':
            show(todo_list)

        case 'edit':
            show(todo_list)
            chosen_todo_index = input('Choose an item to edit (type its number):\n > ')
            chosen_todo_index = number_to_str(chosen_todo_index)
            todo_edited = input('Enter the new todo:\n > ').capitalize()
            todo_list[chosen_todo_index] = todo_edited

        case 'complete':
            todo_completed = input('Enter the completed to-do (type its number):\n > ')
            todo_completed = number_to_str(todo_completed)
            todo_list.pop(todo_completed)

        case 'exit':
            break

        case _:
            print(f'"{user_input}" is an unknown command. Please, type again.')
