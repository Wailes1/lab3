from datetime import datetime, date
from decimal import Decimal
from fractions import Fraction

def task1():
    """1. List comprehension (простое преобразование)"""
    squares = [x**2 for x in range(1, 11)]
    print("Квадраты чисел от 1 до 10:", squares)
    
def task2():
    """2. List comprehension (фильтрация)"""
    evens = [x for x in range(1, 20) if x % 2 == 0]
    print("Четные числа от 1 до 20:", evens)

def task3():
    """3. List comprehension (работа со строками)"""
    words = ["python", "Java", "c++", "Rust", "go"]
    result = [word.upper() for word in words if len(word) > 3]
    print("Слова в верхнем регистре (длина > 3):", result)

class Countdown:
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        return iter(range(self.n, 0, -1))

def task4():
    """4. Демонстрация итератора"""
    print("Countdown(5):", end=" ")
    for x in Countdown(5):
        print(x, end=" ")
    print()

def fibonacci(n):
    """5. Собственный генератор"""
    x1 = 0
    x2 = 1
    for _ in range(n):
        yield x1
        x1, x2 = x2, x1 + x2

def task5():
    """5. Демонстрация генератора"""
    print("Первые 5 чисел Фибоначчи:", end=" ")
    for num in fibonacci(5):
        print(num, end=" ")
    print()

def task6():
    """6. Финансовый калькулятор"""
    try:
        P = Decimal(input("Начальная сумма (руб): "))
        r = Decimal(input("Процентная ставка (%): "))
        t = Decimal(input("Срок (лет): "))
        
        S = P * (1 + r / (12 * 100)) ** (12 * t)
        profit = S - P
        
        print(f"Итоговая сумма: {S:.2f} руб")
        print(f"Прибыль: {profit:.2f} руб")
    except:
        print("Ошибка ввода!")

def task7():
    """7. Работа с дробями"""
    a = Fraction(3, 4)
    b = Fraction(5, 6)
    
    print(f"3/4 + 5/6 = {a + b}")
    print(f"3/4 - 5/6 = {a - b}")
    print(f"3/4 × 5/6 = {a * b}")
    print(f"3/4 ÷ 5/6 = {a / b}")
