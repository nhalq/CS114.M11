PSI = float(input())
kg_cm2 = PSI * 0.453592 / (2.54 ** 2)

from decimal import *
getcontext().prec = 6
print(Decimal(kg_cm2).normalize())
