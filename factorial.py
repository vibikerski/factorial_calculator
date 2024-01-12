def factorial(n):
    """
    Функція для обчислення факторіалу числа.

    Параметри:
    - n (int): Ціле число, для якого обчислюється факторіал.

    Повертає:
    int: Факторіал введеного числа.
    """
    if n == 0 or n == 1:
        return 1
    return n*factorial(n-1)

number = int(input("Введіть число: "))
print(f'Факторіал числа {number} - {factorial(number)}.')