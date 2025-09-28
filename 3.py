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
