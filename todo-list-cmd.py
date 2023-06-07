def show(todos):
    """
    Enumerates and prints items of todo list 
    """
    for index, todo in enumerate(todo_list):
                print(f'{index+1}.', todo)


todo_list = []
user_input = None

while user_input != 'exit':
    user_input = input('\nType add, show, edit, complete or exit:\n > ').lower()
    match user_input:
        case 'add':
            todo_added = input('Enter a todo:\n > ').capitalize()
            todo_list.append(todo_added)
        case 'show':
            show(todo_list)
        case 'edit':
            show(todo_list)
            choosen_todo_index = input('Choose an item to edit (type its number):\n > ')
            if choosen_todo_index.isnumeric():  # prevents bugs
                 choosen_todo_index = int(choosen_todo_index) - 1

            todo_edited = input('Enter the new todo:\n > ').capitalize()
            for todo in todo_list: 
                old_todo_index = todo_list.index(todo)    
                if old_todo_index == choosen_todo_index:
                    todo_list[old_todo_index] = todo_edited
        case 'complete':
            todo_completed = input('Enter the completed to-do (type its number):')
            if todo_completed.isnumeric():
                 todo_completed = int(todo_completed)
