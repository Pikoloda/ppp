# Napisz program wyświetlający na ekranie poniższy prostokąt o wymiarach 50 x 5 gwiazdek.

char = "*"
columns = 50
rows = 5
print(char * columns, char + " " * 48 + char, char + " " * 48 + char, char + " " * 48 + char, char * columns, sep="\n",
      end=" ")
