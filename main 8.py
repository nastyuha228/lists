n = int(input("Введите количество чисел: "))
nu = []
i = 1

while i <= n:
    num = int(input(f"Введите число {i}: "))
    nu.append(num)
    i += 1

r = nu[::2]

print(r)
