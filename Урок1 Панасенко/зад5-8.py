name = input("Как вас зовут? ")
age = int(input("Сколько вам лет? "))
if age < 14:
    print('Вам', age, 'лет...Неплохо..')
if 14 <=age <= 55:
    print('Вам', age, 'лет...Хорошо..')
if age > 55:
    print('Вам', age, 'лет...Хорошо..')

print('Имя от 2 до последнего символа: ', name[1:(len(name) - 1)])
print('Имя задом наперёд: ', name[::-1])
print('Последние 3 символа имени: ', name[(len(name) - 3):])
print('Первые 5 символов имени: ', name[:5])
print('Длина имени пользоватля: ',len(name))

sum_age=0
prois_age=1
while age > 0:
    n = age % 10
    sum_age = sum_age + n
    prois_age = prois_age * n
    age = age // 10
print('Сумма чисел возраста:',sum_age)
print('Произведение чисел возраста:', prois_age)

Z = name.capitalize()
Ver = name.upper()
Nij = Ver.swapcase()
print('Имя - с заглавной буквы:', Z)
print('Имя - в нижнем регистре:', Nij)
print('Имя - в верхнем регистре:', Ver)