
a = "0550"
b = 550

if a == b:
    print('sdfs')


tasks_id = [1, 2, 3]
task_names = ['do hw', 'read book', 'watch youtube tutorial']
task_urgencies = [5, 4, 3]

for i in range(3):
    """В данном случае если понадобится изменить формат спецификатора , нужно будет менять в трех местах
    это не очень практично. поэтому лучше сделать функцию и менять в одном месте
    """
    print(f"{tasks_id[i]:{'^12'}}{task_names[i]:{'^12'}}{task_urgencies[i]:{'^12'}}")

print()


def create_formatted_records(frm):
    """Функция получающая произвольный спецификатор формата
    тем самым упорядочиваем вывод , чтобы было читабельно
    """
    for i in range(3):
        task_id = tasks_id[i]
        name = task_names[i]
        urgency = task_urgencies[i]
        print(f'{task_id:{frm}}{name:{frm}}{urgency:{frm}}')


create_formatted_records('^12')
dfsdf = 1