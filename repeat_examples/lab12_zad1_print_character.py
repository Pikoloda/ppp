def print_char(character = "%", repeat = 10, vert = False):
    for i in range(repeat):
        if vert:
            print(character)
        else:
            print(character ,end=" ")
    if not vert:
        print()
    print()

print_char()
print_char("#",5,True)
print_char("j", 8)