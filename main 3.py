import random

r = [random.randint(1, 100) for _ in range(10)]
print(f"Список: {r}")

x = int(input("число: "))

if x in r:
    i = r.index(x)
    print(f"Число {x} найдено в списке на позиции {i}")
else:
    print(-1)
