import random

r = [random.randint(1, 100) for _ in range(10)]
s = sum(r)
p = 1
for n in r:
    p *= n

print(f"Список: {r}")
print(f"Сумма: {s}")
print(f"Произведение: {p}")
