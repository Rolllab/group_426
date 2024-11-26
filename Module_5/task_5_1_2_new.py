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
    print('-' * 50)
    print('Правильно отвечены слова:\n {}'.format('\n '.join([k for k, v in answers.items() if v])))
    print('Не правильно отвечены слова:\n {}'.format('\n '.join([k for k, v in answers.items() if not v])))
    print('-' * 50)
    print(f'Ваша оценка - {levels.get(len([k for k, v in answers.items() if v]))}')
    return True


if __name__ == '__main__':
    words_easy = {"family": "семья", "hand": "рука", "people": "люди", "evening": "вечер", "minute": "минута",}
    words_medium = {"believe": "верить", "feel": "чувствовать", "make": "делать", "open": "открывать", "think": "думать",}
    words_hard = {"rural": "деревенский", "fortune": "удача", "exercise": "упражнение", "suggest": "предлагать", "except": "кроме",}
    words = {}
    answers = {}
    levels = {
        0: "Нулевой",
        1: "Так себе",
        2: "Можно лучше",
        3: "Норм",
        4: "Хорошо",
        5: "Отлично"
    }
    difficulty_list = [['easy', words_easy], ['medium', words_medium], ['hard', words_hard]]

    get_result()
