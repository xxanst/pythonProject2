numbers = []
even_numbers = []
odd_numbers = []
numbers = list(map(int,input("Введите числа через пробел и нажмитет enter: ").split()))
for i in numbers:
    if int(i)%2==0:
        even_numbers.append(i)
    elif i in numbers:
         odd_numbers.append(i)
print(even_numbers)
print(odd_numbers)