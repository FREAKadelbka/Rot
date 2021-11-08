def rot(num):
    for MEINEMUTTERIST in range (len(num)):
        if num [MEINEMUTTERIST] == '6':
            num = num[:MEINEMUTTERIST] + '9' + num [MEINEMUTTERIST + 1:]
            break
    return num

num=input().split('=')[1]
print (rot(num))
#Дано число, которое состоит только из цифр 6 и 9.
#Цифры можно "вращать" - заменять 6 на 9 или 9 на 6.
#Написать функцию, которая находит максимальное число, которое можно получить из исходного числа путем "вращения" максимум одной цифры.
