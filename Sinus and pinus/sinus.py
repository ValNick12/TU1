import math
from re import X

def sine(x, tavan):
    x = x % 360 * math.pi / 180
    sum = 0
    for i in range(tavan):
        sum += (-1)**i * x**(2 * i + 1) / math.factorial(2 * i + 1)
    return sum

x = int(input('Pi6i tuka gradusi we: '))
tavan = int(input('Pi6i tuka za tavana we: '))

print(sine(x, tavan))