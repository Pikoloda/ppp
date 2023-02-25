def count_down(wishes = True):
    print("Trzy...")
    print("Dwa...")
    print("Jeden...")

    if not wishes:
        return

    print("Szczęśliwego Nowego Roku!")

# count_down()


print(type(count_down(wishes=False)))
