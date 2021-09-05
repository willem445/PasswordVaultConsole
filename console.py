import sys

from prompt_toolkit import PromptSession
from prompt_toolkit.completion import NestedCompleter
from prompt_toolkit.styles import Style
from prompt_toolkit import prompt
import database
from services import authenticate
from models import AuthenticateResult, LogoutResult
from console import ConsoleState


sql_completer = NestedCompleter.from_nested_dict({
        'login': None,
        'logout': None,
        'add': {'password': None, 'account': None},
        'delete': {'password': None, 'account': None},
        'edit': {'password': None, 'account': None},
        'query': {'password': None},
        'exit': None,
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

def logout(session):
    result = state.logout()

    if not state.is_logged_in():
        print("Must login first!")
    elif result == LogoutResult.Failed:
        print("Logout failed!")
    elif result == LogoutResult.Success:
        print("Logged out.")

def main():
    session = PromptSession(
        completer=sql_completer, style=style
    )

    while True:
        try:
            text = session.prompt("> ", is_password=False)
        except KeyboardInterrupt:
            continue  # Control-C pressed. Try again.
        except EOFError:
            break  # Control-D pressed.

        if text == 'login':
            login(session)
        elif text == 'logout':
            logout(session)
        elif text == 'exit':
            break

    print("GoodBye!")


if __name__ == "__main__":
    main()