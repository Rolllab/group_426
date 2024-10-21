import re

""" Ну и задание... Пора уже тесты писать... Замучился вводить донные пользователя... Ладно одного, а то троих надо...
    Поэтому я использовал аргументы (я их закомментировал)."""


questions = ['Введите имя пользователя -> ', 'Введите фамилию пользователя -> ',
                 'Введите телефон в формате +***(**)******* -> ', 'Введите email на яндексе -> ']
messages = ['Имя принято', 'Фамилия принята', 'Телефон принят', 'Почта принята']
error_messages = ['Содержит не подходящие символы.', 'Содержит не подходящие символы.',
                  'Не соответствует формату +***(**)*******', 'Почта должна содержать @yandex.ru']
patterns = [r'[A-Za-zА-Яа-яЁё]+', r'[A-Za-zА-Яа-яЁё]+', r'\+\d{1,3}\(\d{2,3}\)\d{7}$', r'(\w+|\d+)+@yandex\.ru$']


class MyRegException(Exception):
    def __init__(self, pattern, user_input, message, error_message):
        self.pattern = pattern
        self.user_input = user_input
        self.message = message
        self.error_message = error_message
        self.check_input()

    def check_input(self):
        if not re.match(self.pattern, self.user_input):
            print(f'Синтаксическая ошибка: {self.error_message.upper()}')
            return False
        else:
            print(self.message)
            return True


def main(*args):
    user_list = []
    count_people = 0
    try:
        count_people = int(input('Введите сколько человек вы хотите добавить в список -> '))
    except ValueError:
        print('Надо ввести число...')

    while len(user_list) < count_people:
        user_data_list = []
        for question in range(len(questions)):
            while True:
                answer = input(questions[question])
                if MyRegException(re.compile(patterns[question]), answer, messages[question], error_messages[question]):
                    user_data_list.append(answer)
                    break

        if user_data_list in user_list:
            print('\nПользователь с такими донными уже есть... Введите другие данные\n')
        else:
            user_list.append(user_data_list)
    print(user_list)

    # user_list.clear()
    # for i in args:
    #     if i not in user_list:
    #         user_list.append(i)
    # print(user_list)


if __name__ == '__main__':
    user_1 = ['Иван', 'Петров', '+375(17)1111111', 'mail@yandex.ru']
    user_2 = ['Николай', 'Сидоров', '+375(17)3333333', 'mail_2@yandex.ru']
    user_3 = ['Егор', 'Иванов', '+375(17)4444444', 'mail_3@yandex.ru']
    user_4 = ['Егор', 'Иванов', '+375(17)4444444', 'mail_3@yandex.ru']
    main(user_1, user_2, user_3, user_4)