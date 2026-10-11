class Calculator:
    """Базовый класс калькулятора с основными арифметическими операциями."""

    @staticmethod
    def add(a: float, b: float) -> float:
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно.")
        return a / b

    @staticmethod
    def power(a: float, b: float) -> float:
        return a ** b


def main():
    calc = Calculator()
    operations = {
        "+": calc.add,
        "-": calc.subtract,
        "*": calc.multiply,
        "/": calc.divide,
        "^": calc.power,
    }

    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /, ^")
    print("Для выхода введите 'q'\n")

    while True:
        raw_a = input("Первое число (или 'q' для выхода): ").strip()
        if raw_a.lower() == "q":
            print("Работа завершена.")
            break

        op = input("Операция (+, -, *, /, ^): ").strip()
        if op.lower() == "q":
            print("Работа завершена.")
            break

        if op not in operations:
            print("Ошибка: неподдерживаемая операция. Попробуйте снова.\n")
            continue

        raw_b = input("Второе число: ").strip()
        if raw_b.lower() == "q":
            print("Работа завершена.")
            break

        try:
            num1 = float(raw_a)
            num2 = float(raw_b)
            result = operations[op](num1, num2)
            # Убираем лишние нули после запятой, если число целое
            formatted = int(result) if result.is_integer() else result
            print(f"Результат: {formatted}\n")
        except ValueError:
            print("Ошибка: введены некорректные числа.\n")
        except ZeroDivisionError as err:
            print(f"Ошибка: {err}\n")


if __name__ == "__main__":
    main()