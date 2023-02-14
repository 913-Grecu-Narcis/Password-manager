from business.service_exception import ServiceException
from domain.user import User, UserValidator
from infrastructure.repository import Repository


class ConnectService:
    def __init__(self, repo: Repository):
        self.__repo = repo


    def check_for_email_in_db(self, email):
        result = self.__repo.find_by_email(email)
        return len(result) != 0

    def check_for_login(self, user_email, user_password):
        result = self.__repo.find_by_email(user_email)
        if len(result) == 0:
            return False, 'Email not found!'

        if result[0][3] != user_password:
            return False, 'Password is incorrect!'

        return True, 'Login successfully!'


    def register_user(self, user_name, email, confirm_email, password, confirm_pass):
        if email != confirm_email:
            raise ValueError('Emails are not the same!')

        if password != confirm_pass:
            raise ValueError('Passwords are not the same!')

        user = User(user_name, email, password)
        UserValidator.validate(user)

        if self.check_for_email_in_db(email):
            raise ServiceException('There exists an account with this email!')

        self.__repo.add_user(user)
