def add(

):
    pass


def show():
    pass


def edit():
    pass


def complete():
    pass


PROMPT_DICT = {
    'add': add,
    'show': show,
    'edit': edit,
    'complete': complete,
}

PROMPT = 'Type add, show, edit, complete or exit:\n> '
todo_list = []
user_input = None

while user_input != 'exit':
    user_input = input(PROMPT).lower()
    for prompt in PROMPT_DICT:
        if user_input == prompt:
            PROMPT_DICT[prompt]()
    # new_todo = input('TO-DO: ')
    # todo_list.append(new_todo)
