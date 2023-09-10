from decimal import Decimal
from math import floor

theta = Decimal(2)
decimal_places = 0
while decimal_places < 25:
    b = [theta]
    decimals = ""
    while len(decimals) <= decimal_places:
        b.append(floor(b[-1]) * (b[-1] - floor(b[-1]) + 1))
        decimals += str(floor(b[-1]))
    theta = Decimal(f"{floor(theta)}.{decimals}")
    decimal_places = -theta.as_tuple().exponent
print(round(theta, 24))
