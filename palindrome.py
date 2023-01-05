import re


def palindrome(string: str) -> bool:
    reg = re.sub('[^a-zA-Z]', '', string)
    lower_case = str(reg.lower())
    return lower_case[::-1].startswith(lower_case)


print(palindrome(input()))
