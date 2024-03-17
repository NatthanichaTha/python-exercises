# At least 1 lower case [a - z]
# At least 1 number [0 - 9]
# At least 1 upper case [A - Z]
# At least 1 special character [!@#$%^&*]
# Minimum lenght: 6
# Maximum lenght: up to 12

def check_strenght(password):
    lower_case_count = 0
    upper_case_count = 0
    number_count = 0
    special_char_count = 0
    min_len = 6
    max_len = 12

    if len(password) < min_len or len(password) > max_len:
        return False
    
    for char in password:
        if char.islower():
            lower_case_count += 1
        elif char.isupper():
            upper_case_count += 1
        elif char.isnumeric():
            number_count += 1
        elif not char.isalpha() and not char.isnumeric():
            special_char_count += 1

    if lower_case_count == 0 or upper_case_count == 0 or number_count == 0 or special_char_count == 0:
        return False

    return True


password = input("Create a password: ")

while not check_strenght(password):
    print("The password is weak. Try again.")
    password = input("Create a password: ")
else:
    print("Password created.", password)

