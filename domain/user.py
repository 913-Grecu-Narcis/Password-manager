from dataclasses import dataclass

from domain.validator_exception import ValidatorException


@dataclass
class User:
    username: str
    email: str
    password: str


class UserValidator:
    @staticmethod
    def validate(user):
        errors = []
        if len(user.username) < 3:
            errors.append('Username must be at least 3 letters long!')

        if len(user.email) < 5:
            errors.append('Incorrect email!')

        if len(user.password) < 5:
            errors.append('Password must be at least 5 letters long!')

        if len(errors) > 0:
            raise ValidatorException(errors)
