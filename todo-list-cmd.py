def add(todo_list, action):
    """
    Adds one item to to-do list
    :return:
    """
    new_item = action.split()[1]
    todo_list.append(new_item)
    return todo_list


def show(todo_list, *args):
    for item in todo_list:
        print(item, '\n')
    return todo_list


def edit(todo_list, action):
    pass
    return todo_list


def complete(todo_list, action):
    pass
    return todo_list


PROMPT_DICT = {
    'add': add,
    'show': show,
    'edit': edit,
    'complete': complete,
}

todos = []
user_input = None

while user_input != 'exit':
    user_input = input('Type add, show, edit, complete or exit:\n> ').lower()
    for prompt in PROMPT_DICT:
        if user_input.split()[0] == prompt:
            todos = PROMPT_DICT[prompt](todos, user_input)
