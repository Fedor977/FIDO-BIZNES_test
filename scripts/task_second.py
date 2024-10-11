numbers = []

for i in range(3):
    num = int(input(f"Введите число {i+1}: "))
    numbers.append(num)

numbers.sort(reverse=True)

print("Числа в порядке убывания:", numbers)
