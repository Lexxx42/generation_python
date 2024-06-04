n = int(input())

i = 1

while n >= 2 ** i:
    i += 1

i = i - 1

power = 2 ** i

steps_to_point = n - power

res = steps_to_point * 2 + 1

print(res)
