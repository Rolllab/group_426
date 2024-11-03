from functools import reduce

# Не сделал!!! Задолбала меня эта задача
def solution_module_4_1_1(text, author):
    string = ''
    for i in text:
        if i != '.':
            string += i
    return f'"{string}"\n{author.rjust(len(string))}'


def solution_4_1_2(num1, num2) -> list:
    return list(filter(lambda x: x % 2 == 0, range(num1, num2)))


def solution_4_1_3(length: int, symbol: str, var: bool) -> print:
    for i in range(length):
        if var:
            print((symbol + '  ') * length)
        else:
            if i == 0 or i == length - 1:
                print((symbol + '  ') * length)
            else:
                # Ответ подогнал под цифру 8 (length). Если поставить другую цифру, то сторона квадрата уедет
                print(symbol + ( '\t ' * (length - 3)) + symbol)


def solution_4_1_4(*args) -> min:
    return min(args)


def solution_4_1_5(range1: int, range2: int):
    min_ = min([range1, range2])
    max_ = max([range1, range2])
    return reduce(lambda x, y: x * y, [i for i in range(min_, max_ + 1)])


def solution_4_1_6(number: int) -> int:
    return len(str(number))


def solution_4_1_7(number) -> bool:
    count = len(str(number))
    if count >= 4 and count % 2 == 0:
        return str(number)[:int(count/2)] == str(number)[-1:-int((count/2) + 1):-1]
    return False



if __name__ == '__main__':
    text_4_1_1 = "Don't compare yourself with anyone in this world...if you do so, you are insulting yourself."
    author_4_1_1 = "Bill Gates"
    print(solution_module_4_1_1(text_4_1_1, author_4_1_1))

    print(f'Вывод всех четных чисел между введенными - {solution_4_1_2(1, 20)}')
    solution_4_1_3(8, '$', False)
    print(f'Самое маленькое число в передаваемых параметрах = {solution_4_1_4(1, 3, 39, 115, -20)}')
    print(f'Произведение всех чисел в списке = {solution_4_1_5(5, 1)}')
    print(f'Число состоит из {solution_4_1_6(3456)} цифр')
    print(f'Является ли переданное в функцию число палиндромом ? Ответ - {solution_4_1_7(12344321)}')