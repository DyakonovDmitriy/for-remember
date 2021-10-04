'''
что-то про машины
'''

# name='Volvo'         #бренд
# engain_volume=1.6    # объем движка
# #horsepower=90        # лoшадиная сила
# sunroof=False        # Люк на крыше
#
# horsepower=int(input('введите лошадиные силы'))
# tax=0
#
# if horsepower<80:
#     print('notax')
# elif horsepower<100:
#     print('tax is', 90)
# elif horsepower<120:
#     print('tax is',95)
# else:
#     print('tax is', 150)


# Задача 1
# Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.

# count_number=int(input('введите колличество 0: \n'))
#
# a='0'*count_number
# n=1
# for i in range(5):
#     print(n,')', a)
#     n+=1

# Задача 2
# Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
# x=0
# i=1
# while i<=10:
#     a=int(input('введите число от 1 до 10 \n'))
#     i += 1
#     if a==5:
#         x+=1
#     else:
#         continue
#
# print('колличество введных цифр 5 равно',x)

# Задача 4
# Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.

# mul=1
# for i in range(1,11):
#     mul*=i
# print((mul))

# Задача 5
# Вывести цифры числа на каждой строчке.

# i=12345
# while i>=1:
#     print(i%10)
#     i//=10

# Задача 6
# Найти сумму цифр числа.

# x=int(input('введите положительное простое число'))
# k=0
# while x>0:
#     k+=x%10
#     x//=10
# # else:
# print(k)

# задача 7
# найти произведение числа

# x=int(input('введите число'))
# k=1
# while x>0:
#     k*=x%10
#     x//=10
# print(k)

# задача 9
# найти максимальную цифру в числе

digit_primary=int(input('введите число : \n'))
k=0
while digit_primary>0:
    if digit_primary%10>k:
        k=digit_primary%10
        digit_primary//=10
    else:
        digit_primary//=10
print("максимальное число =", k)
