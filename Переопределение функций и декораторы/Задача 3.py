def check_password(password):
    def decorator(func):
        def wrapper(*args, **kwargs):
            entered_password = input("Введите пароль: ")
            if entered_password == password:
                return func(*args, **kwargs)
            else:
                print("В доступе отказано")
                return None
        return wrapper
    return decorator

@check_password("password")
def make_burger(type_of_meat, with_onion=False, with_tomato=True):
    print("Бургер готов!")

make_burger("говядина", with_onion=True, with_tomato=False)