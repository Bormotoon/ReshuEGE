# https://inf-ege.sdamgia.ru/problem?id=13498

'''Исполнитель Май17 преобразует число на экране.
У исполнителя есть две команды, которым присвоены номера:
1. Прибавить 1
2. Прибавить 3

Первая команда увеличивает число на экране на 1, вторая увеличивает его на 3. Программа для исполнителя Май17 — это последовательность команд.

Сколько существует программ, для которых при исходном числе 1 результатом является число 17 и при этом траектория вычислений содержит число 9? Траектория вычислений программы — это последовательность результатов выполнения всех команд программы. Например, для программы 121 при исходном числе 7 траектория будет состоять из чисел 8, 11, 12.'''

def F(x, y):
    if x > y:
        return 0
    elif x == y:
        return 1
    else:
        return F(x + 1, y) + F(x + 3, y)


print(F(1, 9) * F(9, 17))

# >>> 169
