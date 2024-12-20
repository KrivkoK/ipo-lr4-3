# Запрашиваем у пользователя ввод числа
number = int(input("Введите число для вычисления факториала: "))

# Проверка на неотрицательное число
if number < 0:
    print("Факториал не определен для отрицательных чисел.")
else:
    factorial = 1
    count = 1
    
    # Вычисление факториала с помощью цикла while
    while count <= number:
        factorial *= count
        count += 1
    
    print(f"Факториал числа {number} равен {factorial}.")
