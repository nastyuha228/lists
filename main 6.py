import random

r = [random.randint(1, 50) for _ in range(10)]
d = []

for n in r:
    if r.count(n) > 1 and n not in d:
        d.append(n)

if d:
    print(f"Список содержит повторяющиеся элементы: {d}")
else:
    print("Список не содержит повторяющихся элементов")
