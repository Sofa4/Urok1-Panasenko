name = "Sofachka"
print('Hello, %s' % name, '\n')

age = 17
print('-Где ваш qr код?' '\n' '-Мне', age, 'лет.' '\n')

name5 = name * 5
print('я научилась конкатенации: ', name5, '\n')

namep = input("Как вас зовут? ")
agep = int(input("Сколько вам лет? "))

if 0<= agep <=150:
    if namep.isalpha() == True:
        print('Привет, ', namep,'! Тебе всего', agep, "лет!")
    else:
        print('Ошибка при заполнении имени')
else:
    print('Ошибка при заполнени возраста')