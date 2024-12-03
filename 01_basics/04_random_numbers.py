import random

# Solution to get a random number print(random.randinit(1, 100))
MIN_NUMBER: int = 1
MAX_NUMBER: int = 100
N_RANDOM_NUMBER: int = 10

# Function
# 1. Use For Loop
number_list = []
for i in range(N_RANDOM_NUMBER):
    rand_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    number_list.append(rand_number)

print(*number_list)