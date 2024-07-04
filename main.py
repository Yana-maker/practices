prime_numbers = [1, 3, 5]

# требуемый вывод (первое число это позиция в списке , второе - само значение)
# Prime number # 1: 1
# Prime number # 2: 3
# Prime number # 3: 5

for num_pos, num in enumerate(prime_numbers, start=1):
    print(f'Prime number # {str(num_pos)}: {str(num)}')

print()

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

# разделяем число запятой на группы
large_prime_number = 10000000
print(f'разделяет число запятой на группы: {large_prime_number:,d}')

# переводим число в проценты и после запятой 2 знака
large_prime_number = 0.10000000
print(f'разделяет число запятой на группы: {large_prime_number:.2%}')


# задача из книги № 1
# вывести в консоль Vacuum: {130.68} ,
# цену округлить до сотых и заключить в фигурные скобки

items = {'name': 'Vacuum', 'price': 130.675}
print(f"{items['name']}: {{{items['price']:.2f}}}")

print()

user_input = input('введите текст состоящий только из букв и цифр: ')
if user_input.isalnum():
    """isalnum проверяет, что строка содержит только цифры и/или 
    латинские/русские буквы a-z, A-Z, 0-9"""

    print('текст корректный')
else:
    print('текст некорректный')

print()


list_str = '[1, 2, 3, 4, 5]'
stripped_list = list_str.strip('[]')
print(stripped_list)  # строка
number_list = [int(x) for x in stripped_list.split(', ')]
print(number_list)  # лист

# добавляем новую запись в тестовую ветку чтобы слить ее с гл
# авной dsfsdf sd
# сново что то добавляю в тестовой ветки