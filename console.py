import os
import sys
from typing import List
from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.styles import Style
from models import AuthenticateResult, LogoutResult
from console import ConsoleState


completer = NestedCompleter.from_nested_dict({
        'login': None,
        'logout': None,
        'add': {'password': None, 'account': None},
        'delete': {'password': None, 'account': None},
        'edit': {'password': None, 'account': None},
        'query': {'application': None, 'description': None, 'category': None},
        'get': {'password': None},
        'help': None,
        'exit': None,
        'clear': None,
    }
)

style = Style.from_dict(
    {
        "completion-menu.completion": "bg:#008888 #ffffff",
        "completion-menu.completion.current": "bg:#00aaaa #000000",
        "scrollbar.background": "bg:#88aaaa",
        "scrollbar.button": "bg:#222222",
    }
)

state = ConsoleState()

clear_console = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def login(session):
    username = session.prompt("Username: ")
    password = session.prompt("Password: ", is_password=True)

    result = state.login(username, password)

    if result == AuthenticateResult.UsernameDoesNotExist:
        print(f'Username: {username} does not exist!')
    elif result == AuthenticateResult.Failed:
        print("Failed to login!")
    elif result == AuthenticateResult.PasswordIncorrect:
        print("Password incorrect!")
    elif result == AuthenticateResult.Successful:
        print("Success!")

# TODO - create "is_logged_in" decorator
def logout(session):
    if not state.is_logged_in():
        print("Must login first!")
    else:
        result = state.logout()
        if result == LogoutResult.Failed:
            print("Logout failed!")
        elif result == LogoutResult.Success:
            print("Logged out.")

def query_password(session, query_type: str, search_string: str):
    if query_type == 'application':
        result = state.find_password_by_application(search_string)
        print(result)

def get_password(session, application: str):
    plaintext_password = state.get_password_by_application(application)
    print(plaintext_password)

def add_account(session):
    pass

def add_password(session):
    application = session.prompt("Application: ")
    username = session.prompt("Username: ")
    email = session.prompt("Email [blank to skip]: ")
    category = session.prompt("Category [blank to skip]: ")
    website = session.prompt("Website [blank to skip]: ")
    description = session.prompt("Description [blank to skip]: ")
    password = session.prompt("Password: ", is_password=True)

    state.add_password(application, username, email, description, category, website, password)

def _combine_args(args: List[str], start_index: int):
    combined_args = ""
    for x in range(start_index, len(args)):
        combined_args = combined_args + args[x] + " "
    combined_args = combined_args.strip()
    return combined_args


def main():
    session = PromptSession(
        completer=completer, style=style
    )

    while True:
        try:
            text = session.prompt("> ", is_password=False)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

        commands = text.split(' ')

        if commands[0] == 'login':
            login(session)
        elif commands[0] == 'logout':
            logout(session)
        elif commands[0] == 'add':
            if commands[1] == 'password':
                add_password(session)
            elif commands[1] == 'account':
                pass
        elif commands[0] == 'query':
            query_password(session, commands[1], commands[2])
        elif commands[0] == 'get':
            if commands[1] == 'password':
                combined = _combine_args(commands, 2)
                get_password(session, combined)
        elif commands[0] == 'exit':
            clear_console()
            state = None
            break
        elif commands[0] == 'clear':
            clear_console()
        else:
            print("Unknown command!")

    print("GoodBye!")


if __name__ == "__main__":
    main()