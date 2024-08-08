"""Задача 1. Электронная очередь
Нам дали заказ написать программу для электронной очереди.
У каждого человека в очереди есть номер: нулевой, первый, второй, третий и так далее.
Каждый час очередь уменьшается на одного человека, то есть уходит сначала нулевой номер,
затем первый, второй и так далее. Наша программа получает на вход одно число — количество людей
в очереди — и выводит на экран историю обслуживания очереди: какие номера в какой час оставались."""

people = int(input('enter people count: '))
for hour in range(people + 1):
    print("hour come out:", hour)
    for num in range(hour, people):
        print('Num of queue', num)
    print()
print('All people servered!')

# draw a road
for row in range(20):
    for col in range(50):
        if row == 9:
            print('-', end=' ')
        elif col == row + 29:
            print('\\', end=' ')
        elif col == -row + 19:
            print('/', end=' ')
        elif col == 24:
            print('|', end=' ')
        else:
            print(' ', end=' ')
    print()
