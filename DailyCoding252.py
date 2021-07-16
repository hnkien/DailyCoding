from math import ceil


def fraction(a, b):
    denominators = []
    total = 0

    while a != 0:
        denominators.append(ceil(b / a))
        a, b = (-b) % a, b * ceil(b / a)

    return denominators


print(fraction(4, 13))
print(fraction(5, 121))
