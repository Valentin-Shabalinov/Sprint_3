def binary(number: int):
    bin_number = ''
    while True:
        if number == 0:
            break
        elif (number % 2) == 0:
            number = number // 2
            bin_number += '0'
        else:
            number = number // 2
            bin_number += '1'
    return bin_number


print(binary(int(input())))
