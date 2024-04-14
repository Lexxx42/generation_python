# Стоимость строки
# Дана строка текста. Напишите программу для подсчета стоимости строки, исходя из того, что один любой символ (в том числе пробел) стоит
# 60
# 60 копеек. Ответ дайте в рублях и копейках в соответствии с примерами.
#
# Формат входных данных
# На вход программе подается строка текста.
#
# Формат выходных данных
# Программа должна вывести стоимость строки.
#
# Тестовые данные 🟢
# Sample Input 1:
#
# Привет, как дела?!
# Sample Output 1:
#
# 10 р. 80 коп.
# Sample Input 2:
#
# Тимур - лучший математик на свете!!
# Sample Output 2:
#
# 21 р. 0 коп.
# Sample Input 3:
#
# Я собираюсь сделать ему предложение, от которого он не сможет отказаться.
# Sample Output 3:
#
# 43 р. 80 коп.
# Sample Input 4:
#
# w
# Sample Output 4:
#
# 0 р. 60 коп.

COST = 60


def count_cost(phrase: str) -> str:
    cost = len(phrase) * COST
    r = cost // 100
    c = cost % 100

    return f'{r} р. {c} коп.'


print(count_cost(phrase=input()))
