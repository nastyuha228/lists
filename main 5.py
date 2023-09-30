import random

r = [random.randint(1, 100) for _ in range(10)]
m = max(r)

print(f"Список: {r}")
print(f"Наибольший элемент: {m}")
