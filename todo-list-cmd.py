PROMPT = 'Type add, show, edit, complete or exit: '
todo_list = []
user_input = None

while user_input != 'exit':
    user_input = input(PROMPT).lower()
    new_todo = input('TO-DO: ')
    todo_list.append(new_todo)
    print(todo_list)