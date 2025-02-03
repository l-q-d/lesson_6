def is_very_long(user_password):
    return len(user_password) > 12


def has_digit(user_password):
    return any(char.isdigit() for char in user_password)


def has_upper_letters(user_password):
    return any(char.isupper() for char in user_password)


def has_lower_letters(user_password):
    return any(char.islower() for char in user_password)


def has_symbols(user_password):
    return any(not char.isdigit() and not char.isalpha() for char in user_password)


def main():
    user_password = input("Введите пароль: ")
    score = 0
    all_functions = [
        is_very_long,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    
    for check in all_functions:
        if check(user_password):
            score += 2
    
    print("Рейтинг пароля:", score)

if __name__ == "__main__":
    main()    