from statistics import mean
nnn = []
numbers = list(map(int, input("Введите  5 чисел через пробел и нажммте Enter: ").split()))
var = mean(numbers)
print("Среднее значение массива: " + str(var))
for i in numbers:
    if var < i:
        nnn.append(i)
print("Числа из массива, которые больше среднего значения:  "+ str(nnn))