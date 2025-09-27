import math

def calculate_factorial(n):
    """
    Вычисляет факториал числа n с оптимизацией для больших чисел
    """
    return math.factorial(n)

def main():
    """
    Основная функция программы
    """
    print("Программа для вычисления факториала числа")
    print("=" * 40)
    
    try:
        # Запрос ввода от пользователя
        user_input = input("Введите положительное целое число: ")
        
        # Преобразование ввода в целое число
        number = int(user_input)
        
        # Проверка на отрицательное число
        if number < 0:
            raise ValueError("Число должно быть положительным!")
        
        # Вычисление факториала
        result = calculate_factorial(number)
        
        # Вывод результата
        print(f"\nФакториал числа {number} равен: {result}")
        print(f"({number}! = {result})")
        
    except ValueError as e:
        if "invalid literal" in str(e):
            print("Ошибка: Введены нечисловые данные! Пожалуйста, введите целое число.")
        else:
            print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")

# Дополнительная функция для демонстрации работы с большими числами
def demonstrate_large_numbers():
    """
    Демонстрация работы с большими числами
    """
    print("\n" + "=" * 40)
    print("Демонстрация работы с большими числами:")
    
    test_numbers = [5, 10, 20, 50, 100]
    
    for num in test_numbers:
        try:
            result = calculate_factorial(num)
            print(f"{num}! = {result}")
        except Exception as e:
            print(f"Ошибка при вычислении {num}!: {e}")

if __name__ == "__main__":
    main()
    
    # Дополнительная демонстрация
    demonstrate_large_numbers()
