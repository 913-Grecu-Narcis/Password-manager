class ValidatorException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        result = ''
        for error in self.__message:
            result = result + error + '\n'

        return result
