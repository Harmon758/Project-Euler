from math import pi

initial_height = 100
initial_velocity = 20
g = 9.81

max_distance = initial_velocity ** 2 / g
max_height = initial_height + initial_velocity ** 2 / (2 * g)
volume = pi * max_distance * max_height ** 2

print(round(volume, 4))
