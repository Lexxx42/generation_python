# На вход программе подаются два целых числа
# �
# a и
# �
# b. Напишите программу, которая выводит:
#
# сумму чисел
# �
# a и
# �
# b;
# разность чисел
# �
# a и
# �
# b;
# произведение чисел
# �
# a и
# �
# b;
# частное чисел
# �
# a и
# �
# b;
# целую часть от деления числа
# �
# a на
# �
# b;
# остаток от деления числа
# �
# a на
# �
# b;
# корень квадратный из суммы их
# 10
# 10-х степеней:
# �
# 10
# +
# �
# 10
# a
# 10
#  +b
# 10
#
# ​
#  .
# Формат входных данных
# На вход программе подаются два целых числа
# �
# a и
# �
# (
# �
# ≠
# 0
# )
# b(b
# 
# =0), каждое на отдельной строке.
#
# Формат выходных данных
# Программа должна вывести результаты математических операций в соответствии с условием задачи.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 3
# 8
# Sample Output 1:
#
# 11
# -5
# 24
# 0.375
# 0
# 3
# 32768.90100384814
# Sample Input 2:
#
# 123
# 2
# Sample Output 2:
#
# 125
# 121
# 246
# 61.5
# 61
# 1
# 28153056843.0
# Sample Input 3:
#
# 454
# 322
# Sample Output 3:
#
# 776
# 132
# 146188
# 1.4099378881987579
# 1
# 132
# 19595820067580.043

a = int(input())
b = int(input())

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print((a ** 10 + b ** 10) ** 0.5)
