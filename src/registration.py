import hashlib
import random
import secrets

from exceptions import InvalidPasswordException, InvalidUsernameException


class Registration:
    def __init__(self):
        self.database = {}

    def new_user_registration(self, *, username: str, unhashed_password: str) -> None:
        self.database[self._add_username(username)] = [0, 0, 0]
        self.database[username][0] = self._create_solt()
        self.database[username][2] = self._create_num_of_iter()
        valid_password = self._add_password(
            unhashed_password=unhashed_password,
            num_of_iter=self.database[username][2],
            salt=self.database[username][0])
        self.database[username][1] = valid_password
        print("A new user was created!")

    def _add_username(self, username: str) -> str:
        if username in self.database:
            raise InvalidUsernameException("The username already exists. Try another one or log in.")
        elif len(username) < 6:
            raise InvalidUsernameException("Your username must be at least 6 characters long.")
        else:
            return username

    def _add_password(self, *, unhashed_password: str, num_of_iter: int, salt: str) -> str:
        if len(unhashed_password) < 8:
            raise InvalidPasswordException("Your password must be at least 8 characters long.")
        else:
            return self._to_hash(salt=salt,
                                 password_to_hash=unhashed_password,
                                 num_of_iter=num_of_iter)

    def check_login(self, username: str, password: str) -> bool:
        if username in self.database:
            return self.database[username][1] == self._to_hash(salt=self.database[username][0],
                                                               password_to_hash=password,
                                                               num_of_iter=self.database[username][2])
        else:
            raise InvalidUsernameException("Incorrect username")

    @property
    def show_database(self):
        return self.database

    @staticmethod
    def _create_solt() -> str:
        salt = secrets.token_hex(16)
        return salt

    @staticmethod
    def _to_hash(*, salt: str, password_to_hash: str, num_of_iter: int) -> str:
        hashed_password = (salt + password_to_hash).encode('utf-8')
        for i in range(num_of_iter):
            hashy = hashlib.sha512()
            hashy.update(hashed_password)
            hashed_password = hashy.digest()
        return hashed_password.hex()

    @staticmethod
    def _create_num_of_iter() -> int:
        iter_cycle = random.randint(10000, 15000)
        return iter_cycle