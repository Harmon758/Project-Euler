from math import copysign

m = 15  # cost
s = 10 ** 9  # initial fortune

games = 40
tolerance = 10 ** -20

root = step = 0.5
probabilities = [2 ** -(game + 1) for game in range(games)]
payoffs = [2 ** game - m for game in range(games)]
while (
    abs(
        difference := (
            sum(
                probabilities[game] * root ** payoffs[game]
                for game in range(games)
            ) - 1
        )
    ) > tolerance
):
    root += copysign(step, difference)
    step /= 2

print(round(1 - (root ** s), 7))
