# Zad3.
import random

def define_player(player_no):
    word = []
    player_name = input("Podaj imię " + str(player_no) + " gracza: ")
    return {player_name: word}

def define_players():
    players = {}
    players_total = int(input("Podaj liczbę graczy (1-8): "))
    for i in range(players_total):
        players.update(define_player(i + 1))
    return players

def get_first_word(players, word):
    random.simple(players[player_name].append(word))
    return


def get_new_word(prev_word):
    new_word = input("Podaj nowe słowo: ")

def game():


