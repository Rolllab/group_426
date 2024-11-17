import re

from utils import MyRegular
from utils import questions, messages, error_messages, patterns


def blank():
    try:
        for question in range(len(questions)):
            answer = input(questions[question])
            if question > 1:
                print(my_reg:= (MyRegular(re.compile(patterns[question]), answer, messages[question], error_messages[question], question)))
                if str(my_reg).startswith('Такой'):
                    print('-' * 100)
                    return False
            else:
                print(MyRegular(re.compile(patterns[question]), answer, messages[question], error_messages[question]))
        print('-' * 100)
        return True
    except TypeError:
        blank()


if __name__ == '__main__':
    for _ in range(3):
        if not blank():
            blank()
