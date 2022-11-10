weight = int(input("Введите свой вес в килограммах: "))
height = float(input("Введите свой рост в метрах: "))
bmi = float(weight/(height**2))
print("Индекс массы тела: " + str(bmi))