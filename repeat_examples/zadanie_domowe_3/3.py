def play_game():
    # Wylosuj lub wprowadź pierwsze słowo
    first_word = input("Podaj pierwsze słowo: ")
    prev_words = [first_word]

    while True:
        # Wyświetl poprzednie słowa
        print("Poprzednie słowa:", end=" ")
        print(*prev_words, sep=", ")