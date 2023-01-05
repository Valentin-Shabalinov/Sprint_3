# Cпринт №3
## 1-Двоичная система счисления
Реализуйте функцию, которая переводит число из десятичной системы счисления в двоичную. **Встроенные методы языка программирования использовать нельзя!**
### Решение
```
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
```

## 2-Палиндром
Определите, является ли строка палиндромом. Учитываются только буквы и цифры, заглавные и строчные буквы считаются одинаковыми.Буквы могут быть только латинские. Фраза может состоять из строчных и прописных латинских букв, цифр, знаков препинания. 
Функция возвращает **True**, если фраза является палиндромом, иначе - **False**
### Решение
```
import re


def palindrome(string: str) -> bool:
    reg = re.sub('[^a-zA-Z]', '', string)
    lower_case = str(reg.lower())
    return lower_case[::-1].startswith(lower_case)


print(palindrome(input()))
```