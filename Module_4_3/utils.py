import re

questions = ['Введите имя пользователя -> ', 'Введите фамилию пользователя -> ',
                 'Введите телефон в формате +***(**)******* -> ', 'Введите email на яндексе -> ']
messages = ['Имя принято', 'Фамилия принята', 'Телефон принят', 'Почта принята']
error_messages = ['Содержит не подходящие символы.', 'Содержит не подходящие символы.',
                  'Не соответствует формату +***(**)*******', 'Почта должна содержать @yandex.ru']
patterns = [r'[A-Za-zА-Яа-яЁё]+', r'[A-Za-zА-Яа-яЁё]+', r'\+\d{1,3}\(\d{2,3}\)\d{7}$', r'(\w+|\d+)+@yandex\.ru$']

user_name, user_phone , user_mail= [], [], []

class MyRegular:
    def __init__(self, pattern: re, user_input:str, message:str, error_message:str, unique:int =None):
        self.pattern = pattern
        self.user_input = user_input
        self.message = message
        self.error_message = error_message
        self.unique = unique
        self.result = self.check_input()

    def __str__(self) -> str:
        return self.result

    def check_input(self):
        if not re.match(self.pattern, self.user_input):
            print(f'Синтаксическая ошибка: {self.error_message.upper()}')
        else:
            if self.unique and not self.check_unique():
                message = ' уже есть в базе...В регистрации отказано...'
                user_phone.pop() if self.unique == 3 else ...
                return f'Такой номер{message}' if self.unique == 2 else f'Такая почта{message}'
            return self.message


    def check_unique(self) -> bool:
        if self.unique == 2 and self.user_input not in user_phone:
            user_phone.append(self.user_input)
            return True
        if self.unique == 3 and self.user_input not in user_mail:
            user_mail.append(self.user_input)
            return True
        return False
