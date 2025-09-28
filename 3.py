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

def task8():
    """8. Текущая дата и время"""
    now = datetime.now()
    print("Текущая дата и время:", now)
    print("Только дата:", now.date())
    print("Только время:", now.time().strftime("%H:%M:%S"))

def task9():
    """9. Разница дат"""
    try:
        birthday_input = input("Ваш день рождения (ГГГГ-ММ-ДД): ")
        birthday = datetime.strptime(birthday_input, "%Y-%m-%d").date()
        today = date.today()
        
        days_passed = (today - birthday).days
        
        next_birthday = date(today.year, birthday.month, birthday.day)
        if next_birthday < today: 
            next_birthday = date(today.year + 1, birthday.month, birthday.day)
        
        days_to_next = (next_birthday - today).days

        if days_to_next == 0:
            print(f"С Днём Рождения!")
            print(f"Вам исполнилось: {days_passed // 365} лет")
        else:
            print(f"Дней прошло с рождения: {days_passed}")
            print(f"Дней до следующего дня рождения: {days_to_next}")
            
    except ValueError:
        print("Ошибка формата даты! Используйте формат ГГГГ-ММ-ДД (например: 1990-05-15)")

def task10():
    """10. Форматирование даты"""
    now = datetime.now()
    months = ["января", "февраля", "марта", "апреля", "мая", "июня",
              "июля", "августа", "сентября", "октября", "ноября", "декабря"]
    
    result = f"Сегодня {now.day} {months[now.month-1]} {now.year} года, время: {now.hour:02d}:{now.minute:02d}" # [now.month-1]} так как в списке счёт начинается с нуля (0), а не с единицы (1)
    print(result)
