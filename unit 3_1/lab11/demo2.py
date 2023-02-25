#  zagnieżdżenie listy, to nie to samo co skopiowanie listy
numbers = [1, 2, 3]
# l2= [numbers,numbers]

# numbers[0] = 99

# print(l2)

matrix = [numbers[:], numbers[:]]
matrix[0][0] = 99
print(matrix)
