import re


sd = ('sdfsdf', 'sdfsdfds')
print(type(sd))
a = tuple(sd)
b = list(a)

b.insert(1, a)
print(b)


task_pattern_r = re.compile(r'\\task')
texts = ['\task', '\\task', '\\\task', '\\\\task',]
for text in texts:
    print(f'match {text!r}: {task_pattern_r.match(text)}')



print(f"с вопросом {re.findall('yana?', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")
print(f"с плюсом {re.findall('yana+', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")
print(f"с умножением {re.findall('yana*', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")
print(f"с тройкой {re.findall('yana{3}', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")
print(f"с интервалом {re.findall('yana{2,3}', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")
print(f"с интервалом и +{re.findall('yana{1,+}', 'dsfsd gjsfpsok dy yna yana fdlskjfsop yan afayanan')}")


# '\d' - любая десятичная цифра
# \D' - любой символ, не являющийся десятичной цифрой.
# '\s' - любой пробельный символ, включая пробел \t, \n, \r, \f, \v
# '\S' - любой символ не являющийся пробельным
# '\w' - любой символ слова: алфавитно-цифровой или символ подчеркивания
# '\W' - любой символ, не являющийся символ слова
# '.' - любой символ, кроме новой строки
# '[ldm]' - множество перечисленных символов
# '[a-z]' данные символы в нижнем регистре
# '[A-Z]' данные символы в верхнем регистре
# '[^f]' - любой символ кроме указанного/указанных
# 'a|f' - a или f
# '(abc)' - abc как группа

# пример дан текст:
test_text = "dfs76234%^&sdfsdv trthnl\nsdfsd fkdsoi9857*&* 342 2SDFSDFSaa abcabc ab c"
patterns = ['\d', '\D', '\s', '\S', '\w', '\W', '.', '[ldm]', '[a-z]', '[^dfs]', '(abc)', 'a|f']

for pattern in patterns:
    print(f"{pattern: <9}--> {re.findall(pattern, test_text)}")