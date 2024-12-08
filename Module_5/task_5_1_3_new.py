import json


def get_user_level() -> dict:
    print('Выберите ваш уровень знания языка: ')
    for number, level in enumerate(difficulty_list):
        print(f'{number + 1}. {level[0].capitalize()}')

    try:
        difficulty_level = int(input('-> ')) - 1
    except ValueError:
        print('Вы ввели не число. Запустите программу заново...')
        exit(111)

    try:
        words = difficulty_list[difficulty_level][1]
    except IndexError:
        print('Из-за не правильно набранного номера вы переведены на EASY уровень')
        words = difficulty_list[0][1]
    return words


def base_program(**kwargs):
    if kwargs:
        for k, v in kwargs.items():
            user_answer = input(f'{k.capitalize()}, {len(v)} букв, начинается на "{v[0].capitalize()}"... Это - ')
            if user_answer.lower() == v.lower():
                print(f'Верно, {k.capitalize()} — это {v}')
                answers[k] = True
            else:
                print(f'Неверно. {k.capitalize()} — это {v}')
                answers[k] = False
    return False


def get_result():
    my_dict = get_user_level()
    base_program(**my_dict)
    dump_ = {
        'Правильно отвечены слова': ', '.join([k for k, v in answers.items() if v]),
        'Не правильно отвечены слова': ', '.join([k for k, v in answers.items() if not v]),
        'Ваша оценка': file_level.get(str(len([k for k, v in answers.items() if v])))
    }
    with open('result.txt', 'w', encoding='utf-8') as file:
        json.dump(dump_, file, ensure_ascii=False, indent=4)
    return True


if __name__ == '__main__':
    with open('questions.json', encoding='utf-8') as file:
        file_ = json.load(file)
        file_question = file_[0]['questions']
        file_level = file_[1]['levels']
        print(file_level)
        print(file_question)
        words = {}
        answers = {}
        difficulty_list = [['easy', file_question[0]], ['medium', file_question[1]], ['hard', file_question[2]]]

        get_result()
