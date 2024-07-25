"""
Именованные кортежи отличаются тем, что с их элементами связываются имена.
В отличии ль обычных кортежей, к элементам которых обращаемся по индексам.
Именованные кортежи поддерживают точечную запись т.е. по аналогии с классами
пример:
"""

from collections import namedtuple
# Создаем класс именованного кортежа.
# В функции namedtuple указываем имя класса и его атрибуты
Task = namedtuple('Task', 'title, desc, urgency')

# создаем экземпляр именованного кортежа
named_tuple_task = Task('Laundry', 'Wash clothes', 2)


assert named_tuple_task.title == 'Laundry'
print(named_tuple_task)
print(named_tuple_task.title)
print(named_tuple_task.desc)
print(named_tuple_task.urgency)

"""
пример задачи, данные данные ,
нужно их сохранить в именованном кортеже
"""

task_data = '''Laundry,Wash clothes,2
HW,Physics + Math,5
Museum,Egyptian things,4'''

for task_text in task_data.split('\n'):
    title, desc, urgency = task_text.split(',')
    task_nt = Task(title, desc, int(urgency))
    print(f'--> {task_nt}')


