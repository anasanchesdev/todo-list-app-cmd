PROMPT = 'Type add, show, edit, complete or exit: '
todo_list = []

while PROMPT != 'exit':
    user_input = input(PROMPT).lower()
    new_todo = input('TO-DO: ')
    todo_list.append(new_todo)
    print(todo_list)