import random

# random_numbers = []
# counter = 3

# while counter: # counter >= 0
#     number = random.randint(1,10)
#     if number not in random_numbers:
#         random_numbers.append(number)
#         counter -= 1
#
# random_numbers.sort()
# print(random_numbers)

numbers = [ i for i in range(1,11)]
random_numbers = random.sample(numbers, 3)
random_numbers.sort()
print(random_numbers)

