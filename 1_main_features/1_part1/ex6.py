# Переворот числа
# Дано пятизначное или шестизначное натуральное число. Напишите программу, которая изменит порядок его последних пяти цифр на обратный.
#
# Формат входных данных
# На вход программе подается одно натуральное пятизначное или шестизначное число.
#
# Формат выходных данных
# Программа должна вывести число, которое получится в результате разворота, указанного в условии задачи. Число нужно выводить без незначащих нулей.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 12345
# Sample Output 1:
#
# 54321
# Sample Input 2:
#
# 987654
# Sample Output 2:
#
# 945678
# Sample Input 3:
#
# 25000
# Sample Output 3:
#
# 52
# Sample Input 4:
#
# 560000
# Sample Output 4:
#
# 500006


print(int(number[0] + number[::-1][:-1]) if len(number := input()) == 6 else int(number[::-1]))