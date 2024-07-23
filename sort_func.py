
mixed = [1, 2, 3, 'john', ['c', 'd'], ['a', 'b']]
'''добавляем ключ=строка. чтобы питон преобразовал все элементы в строки и тем самым
их сравнить и упорядочить
reverse=True это в обратном порядке 
ответ - ['john', ['c', 'd'], ['a', 'b'], 3, 2, 1]
'''
mixed.sort(key=str, reverse=True)
print(mixed)


'''
Пример # 2 ,  дан лист который содержит словари
нужно упорядочить объекты по степени сложности.
решение: 
'''

tasks = [
    {'title': 'HW', 'desc': 'Physics + Math', 'urgency': 5},
    {'title': 'Laundry', 'desc': 'Wash clothes', 'urgency': 1},
    {'title': 'Museum', 'desc': 'Egyptian things', 'urgency': 4}
]


def using_urgency_level(task):
    """создаем функицю"""
    return task["urgency"]


tasks.sort(key=using_urgency_level)

for i in tasks:
    print(i)


'''
значение key для сортировки по срочности можно задачать лямдой функцией.
'''
tasks.sort(key=lambda x: x['urgency'], reverse=True)
print(tasks)

'''
Метод sort работает только со списками, для словарей , 
кортежей и множеств- нужно использовать sorted.
Если функция аргумента key несложная , лучше рассмотреть лямбду функцию
'''


"""Задача сделать сортировку по длине описания """
def using_urgency_level(task):
    """создаем функицю"""
    return len(task['desc'])


tasks.sort(key=using_urgency_level, reverse=False)

for i in tasks:
    print(i)
