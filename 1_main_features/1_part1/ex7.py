# Standard American Convention
# На вход программе подаётся натуральное число. Напишите программу, которая вставляет в заданное число запятые в соответствии со стандартным американским соглашением о запятых в больших числах.
#
# Формат входных данных
# На вход программе подается натуральное число
# 𝑛
# n
# (
# 0
# <
# 𝑛
# <
# 1
# 0
# 100
# )
# (0<n<10
# 100
#  ).
#
# Формат выходных данных
# Программа должна вывести число с запятыми в соответствии с условием задачи.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# 1000000
# Sample Output 1:
#
# 1,000,000
# Sample Input 2:
#
# 100
# Sample Output 2:
#
# 100
# Sample Input 3:
#
# 12345
# Sample Output 3:
#
# 12,345

number = '121'


#
# result = ''
#
# print(number[-3:])
#
# number_cur = ',' + number[-3:]
# print(number_cur)
# number = number[:-3]
# print(number)
#
#


def americanize(number: str):
    number_cur = []

    def inner(n):
        nonlocal number_cur

        if len(n) <= 3:
            number_cur.append(n)

        else:
            number_cur.append(n[-3:])
            return inner(n[:-3])

    inner(number)
    return ','.join(number_cur[::-1])


print(americanize(number))

# cool

num = input()

for idx in range(len(num) - 3, 0, -3):
    num = num[:idx] + ',' + num[idx:]

print(num)
