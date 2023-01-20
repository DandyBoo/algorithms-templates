def is_power_of_four(number: int) -> bool:
    if number == 0 or number == 1:
        return True
    count = 1
    while count < number:
        count *= 4
        if count == number:
            return True

    return False


print(is_power_of_four(int(input())))
