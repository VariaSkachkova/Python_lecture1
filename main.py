# Python - язык с динамической типизацией
# типы данных - int, float, boolean, str, list, None (не присвоен тип)
#a = 123
#b = 1.23
#print(a,b)
value = None # первое задание переменной
#print(type(b))
#print(type(value))

string = "hello' world" # кавычки - любые
#print(string)
new_string = "hello \nworld" # перенос на новую строку
#print(new_string)

#print('{}, {}, {}'.format(a, b, string)) # форматированный вывод
#print(f'{a}, {b}, {string}') # другой вариант форматированного вывода

f = True
#print(f)
# В питоне массивы заменяют списки
# list = [1, 2, 4, 6]
# list1 = ['1','2','8'] # список строк
#print(list)
#print(list1)

# Ввод и вывод
#print('Введите a')
#a = input()
#print('Введите b')
#b = input()
#print(a, b)
#print('{}, {}'.format(a, b))
#print(f'{a}, {b}')

#print(a, '+', b, '=', a+b) # питон по умолчанию работает со строками - будет конкатенация

#print('Введите a')
#a = int(input()) # ввод с указанием типа
#print('Введите b')
#b = int(input())
#print(a, '+', b, '=', a+b)

# Арифметические операции
# a = 8 # ограничений на размер числа нет
# b = 3
# c = a/b # деление с остатком
# c1 = a//b # целочисленное деление
# c2 = a %  b # остаток от деления
# d = a**b # возведение в степень
# print(c)
# print(c1)
# print(c2)
# print(d)
# e = 1.3
# f = 3
# h = e * f # показывает много знаков после точки
# print(h)
# k = round(e * f, 3) # округление с указанием количества значков после точки
# print(k)

# a = 3
# a += 5
# print(a)

# Логические операции
# a = 1 < 4 and 5 > 2 # можно использовать тройные и четверные неравенства
# b = 1!= 2
# print(a)
# print(b)

# c = 'oops'
# d = 'oop'
# print(c == d)

# e = 1 > 2 or 4 < 6
# print(e)

# f = [1,2,3,4]
# print(7 in f) # проверка наличия элемента
# print(not 2 in f) # проверка отсутствия элемента

# is_odd = f[0]%2 == 0
# print(is_odd)

# Управляющие конструкции

# a = 5
# b = 15
# if a > b:
#     print(a)
# else:
#     print(b)

# original = 23
# inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10

# else: # в питоне у while есть else - после того, как условие перестает выполняться
#     print('Вот и все')
# print(inverted)

# for i in 1, 2, 3, 4:
#     print(i**2)

# range = range(1,10, 2) # все целые числа от 1 до 9 с шагом = 2
# for i in range:
#     print(i)

# for i in 'oolala':
#     print(i)
# операции со строками
text = 'съешь еще этих мягких французских булок'
# print(len(text)) # количество символов
# print('еще' in text) # проверка наличия элемента в строке True/false
# print(text.isdigit()) # проверка наличия цифр True/false
# print(text.islower()) # проверка нижнего регистра True/false
# print(text.replace('еще','ЕЩЕ')) # замена элемента
# for c in text: # побуквенный вывод вертикально
#     print(c)
# print(text[1]) # второй символ
# print(text[len(text)-1]) # последний символ
# print(text[-5]) # пятый символ с конца
# print(text[:]) # print(text)
# print(text[len(text) - 2:]) # от минус 2-ого символа до конца
# print(text[6:-18])
# print(text[::6]) # вывод каждого шестого символа

# списки
# range = range(1, 6)
# numbers = list(range) # приведение рэнджа к списку
# numbers[0] = 10
# # print(len(numbers)) # вывод длины списка
# numbers.append(4) # добавление в конец списка
# print(numbers)
# numbers.remove(5) # удаление элемента из списка
# print(numbers)
# del numbers[0] # удаление элемента по индексу
# print(numbers)

# Функции
def f(x): # задание функции
    if x == 1:
        return 'Integer'
    elif x == 2.3:
        return 23
    else:
        return
arg = 12
print(f(arg)) # вызов функции
print(type(f(arg)))

















