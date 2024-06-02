def check_password(func):
    def wrapper():
        password = input("Введите пароль: ")
        if password == "password":
            return func()
        else:
            print("В доступе отказано")
            return None
    return wrapper

@check_password
def fibonacci():
    n = int(input("Введите число для вычисления числа Фибоначчи: "))
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b

result = fibonacci()
if result is not None:
    print("Результат:", result)