list_1 = [1, 2, 'abc', 3, 4, 5]  # Структура данных список
list_2 = list([1, 2, 3, 4])

print(list_1[0])
print(list_1[2])


tuple_1 = (1, 2, 3, 4)  # Структура данных кортеж
tuple_2 = 1,
tuple_3 = tuple((1, 2))

dict_1 = {  # Структура данных Словарь
    'one': 1,
    'two': 2,
    (1, 2): 3,
    'three': [1, 2, 3]
}

print(dict_1['one'])
print(dict_1[(1, 2)])
print(dict_1['three'])

print(set([1, 2, 2, 2, 3]))  # Структура данных Множества

print(hash('string'))
print(hash('String'))

print(bool(True))  # Булевые значения True или False
print(bool(1))
print(bool(''))
print(bool([]))
print(bool(0,))


user_string = input('Enter something')  # Условный оператор if
if user_string:
    print(user_string[::-1])
else:
    print('String is empty')

if all(['abc', 10 > 5 and any([])]):
    pass

number = int(input('Enter number'))

if number > 100:
    print('More than 100')
else:
    print('I don\'t know')

result = 'More than 100' if number > 100 else None
print(result)

i = 0  # Цикл while
while i < 100:
    print(i)
    i += 1

    if i == 50:
        break

j = 0
while j < 10:
    print(j)
    j += 1

    if j == 5:
        continue

    print('something')


list_3 = range(100)
len_of_list = 8
i = 0
while i < len_of_list:
    print(list_3[i])
    i += 1

for i, j in enumerate(list_3):  # Упрощенный вариант
    print(i, j)


dict_2 = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': [1, 2, 3, 4, 5]
}

for keys, values in dict_2.items():
    print(keys, values)


try:
    1 / 0
except (ZeroDivisionError, TypeError) as e:
    print(e.args)
    a = None
else:
    print('Exception was not caught')
finally:
    print('Exception block ended')
