from models import AuthenticateResult, LogoutResult, User
from services import authenticate


class ConsoleState(object):

    def __init__(self):
        self._current_user = None
        self._password_list = []

    def login(self, username, password) -> AuthenticateResult:
        login_result = AuthenticateResult.Failed

        auth_result, user = authenticate(username, password, None)

        if auth_result == AuthenticateResult.Successful:
            self._is_logged_in = user
            self._current_user = None
        else:
            self._current_user = None

        login_result = auth_result

        return login_result

    def logout(self) -> LogoutResult:
        logout_result = LogoutResult.Failed

        if self.is_logged_in():
            self._password_list.clear()
            self._current_user = None

            logout_result = LogoutResult.Success

        return logout_result

    def is_logged_in(self):
        logged_in = False

        if self._current_user is None:
            logged_in = False
        elif self._current_user.valid_user:
            logged_in = True

        return logged_in
