F = float(input())
C = (F - 32) * 5 / 9
K = C + 273.15

from decimal import *
getcontext().prec = 6
print(Decimal(C).normalize(), Decimal(K).normalize())
