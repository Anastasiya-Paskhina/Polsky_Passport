polish_notation = list(input('Введите выражение вида: \nОПЕРАТОР(+ - * /) ЗНАЧЕНИЕ_1 ЗНАЧЕНИЕ_2: \n').split())


def calculation():
    try:
        assert float(polish_notation[1]) >= 0 and float(polish_notation[2]) >= 0, 'Введите положительное значение'
        if polish_notation[0] == '+':
            print(float(polish_notation[1]) + float(polish_notation[2]))
        elif polish_notation[0] == '-':
            print(float(polish_notation[1]) - float(polish_notation[2]))
        elif polish_notation[0] == '*':
            print(float(polish_notation[1]) * float(polish_notation[2]))
        elif polish_notation[0] == '/':
            try:
                answ = float(polish_notation[1]) / float(polish_notation[2])
                print(answ)
            except ZeroDivisionError:
                print('На ноль делить нельзя!')
        else:
            print('Введен неизвестный оператор')
    except AssertionError:
        print('Введите положительное значение')


calculation()