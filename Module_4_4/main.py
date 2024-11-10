"""ТЗ для ChatGpt - напиши мне задачу на python с использованием *args и **kwargs
    
    Задача составленная ChatGpt: 

    Реализация функции отправки сообщений с настройкой параметров.
    Реализуйте функцию send_messages, которая отправляет одно или несколько сообщений и позволяет настраивать дополнительные параметры для каждого сообщения.
    Функция send_messages принимает:
        Неопределённое количество сообщений через *args.
        Дополнительные параметры через **kwargs (например, такие, как priority, urgent, delay, timestamp и т.д.).

    Функция должна выводить каждое сообщение и его параметры (если они переданы).

    В функции:
        Проверьте, передано ли сообщение.
        Если да, выведите его с параметрами.
        Если нет, выведите сообщение о том, что сообщений нет.
        
        
    Пример работы функции:
        send_messages("Hello!", "How are you?", priority="high", urgent=True)
        
    Ожидаемый вывод:
        Сообщение: Hello!
        Параметры: {'priority': 'high', 'urgent': True}

        Сообщение: How are you?
        Параметры: {'priority': 'high', 'urgent': True}
                                                                                                """
def send_message(*args, **kwargs):
    for arg in args:
        if kwargs:
            print(f'Сообщение: {arg}\nПараметры: {kwargs}')
        else:
            print(f'Сообщение: {arg}')


send_message("Hello!", "How are you?", priority="high", urgent=True)
send_message("Goodbye!")
