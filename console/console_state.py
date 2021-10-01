from models.password import Password
from database.db_password import get_passwords_by_user_uuid
from models import AuthenticateResult, LogoutResult, User
from services import authenticate, decrypt


class ConsoleState(object):

    def __init__(self):
        self._current_user = None
        self._password_list = []

    def login(self, username, password) -> AuthenticateResult:
        login_result = AuthenticateResult.Failed

        auth_result, user = authenticate(username, password, None)

        if auth_result == AuthenticateResult.Successful:
            self._is_logged_in = user
            self._current_user = user

            raw_passwords = get_passwords_by_user_uuid(user.unique_id)
            for raw_password in raw_passwords:
                password = Password(
                    raw_password.UniqueID,
                    decrypt(raw_password.Application, user.plaintext_random_key),
                    decrypt(raw_password.Username, user.plaintext_random_key),
                    decrypt(raw_password.Email, user.plaintext_random_key),
                    decrypt(raw_password.Description, user.plaintext_random_key),
                    decrypt(raw_password.Website, user.plaintext_random_key),
                    decrypt(raw_password.Category, user.plaintext_random_key),
                    raw_password.Passphrase,
                )
                self._password_list.append(password)
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

    def find_password_by_application(self, application: str):
        found_passwords = []

        for password in self._password_list:
            if application in password.application:
                found_passwords.append(password.application)
        return found_passwords

    def get_password_by_application(self, application: str):
        found_password = None
        for password in self._password_list:
            if application == password.application:
                found_password = password
                break
        decrypted_password = decrypt(found_password.passphrase, self._current_user.plaintext_random_key)
        found_password = None
        return decrypted_password
