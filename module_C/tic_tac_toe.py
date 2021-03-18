# -*- coding: utf-8 -*-
"""
Крестики-нолики. Играют 2 человека по очереди, начинают крестики.
Есть возможность выбора размера поля.
"""

def field_size_choice():
    """ The function prompts you to select the dimension of the field.
    Returns int N """
    while True:
        while True:
            N = input("Выберите размер стороны поля (число): ")
            if not (N.isdigit()):
                print("Нужно ввести число!")
                continue
            break
        N = int(N)
        if N <= 1:
            print("Неверный размер поля. Внимательнее!")
            continue
        if N == 2:
            print("Уверены? Скучно будет. Лучше - больше!\nВведите число больше 2: ")
            continue
        break
    return N


def users_input(f):
    """The function retrieves data from the player.
    str("1 2") --> (x, y)
    """
    while True:
        place = input("Введите 2 координаты: ").split()
        if len(place) != 2:
            print("Не правильный ввод. Введите 2 координаты")
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print("Неверно введены координаты: нужно ввести 2 числа!")
            continue
        x, y = map(int, place)
        if not (0 <= x <= (N - 1) and 0 <= y <= (N - 1)):
            print("Ошибка. Координаты не в диапазоне поля!")
            continue
        if f[x][y] != "-":
            print("Такой ход уже был, клетка занята!")
            continue
        break
    return x, y


def show_field(f):
    """Drawing a field after a new move"""
    print("  " + " ".join(map(str,[i for i in range(N)]))) # 0 1 2 3 N
    cnt = 0
    for row in f:
        print(str(cnt) + " " + " ".join(row), sep="\n")
        cnt += 1


def winers(field):
    """The calculation of the winner.
    Returns True if one of the players wins.
    """
    # In the horizontals
    for row in range(N):
        if field[row].count("x") == len(field) or\
            field[row].count("o") == len(field):
            return True

    # In the diagonals
    def count_in_diag(field, row, col):
        cnt_x, cnt_o = 0, 0
        if field[row][col] == "x":
            cnt_x += 1
        elif field[row][col] == "o":
            cnt_o += 1
        return cnt_x, cnt_o

    for row in range(N):
        for col in range(N):
            if row == col:  # first condition In the diagonals
                cnt_x, cnt_o = count_in_diag(field, row, col)
            elif col + row == N - 1:  # second condition In the diagonals
                cnt_x, cnt_o = count_in_diag(field, row, col)
        if cnt_x == N or cnt_o == N:
           return True

    # In the verticals
    s = []; s_vert = []
    for row in field:
        for col in row:
            s.append(col)
    for i in range(N):
        row = s[i::N]
        s_vert.append(row)
    cnt = 0
    while cnt < N:
        cnt_x = 0; cnt_o = 0
        for row in s_vert[cnt]:
            for i in row:
                if i == "x":
                    cnt_x += 1
                if i == "o":
                    cnt_o += 1
            if cnt_x == N or cnt_o == N:
                return True
        cnt += 1


def lets_go():
    """The main body of the program.Start of game"""
    field = [["-" for r in range(N)] for k in range(N)]
    print("  " + " ".join(map(str,[i for i in range(N)]))) # 0 1 2 3 N
    cnt = 0
    for row in field:
        print(str(cnt) + " " + " ".join(row), sep="\n")
        cnt += 1
    print(f"\nНачинает игрок 'X'.\nКоординаты клетки необходимо вводить в диапазоне 0 - {N-1}.")

    cnt = 0
    while True:
        if cnt % 2 == 0:
            print("\nХод игрока Х.", end = " ")
            player = "x"
        else:
            print("\nХод игрока 0.", end = " ")
            player = "o"
        if cnt < N**2:
            x, y = users_input(field)
            field[x][y] = player
            show_field(field)
        if winers(field):
            if cnt % 2 == 0:
                print("Выиграл игрок 'Х'")
            else:
                print("Выиграл игрок '0'")
            break
        if cnt == N**2:
            print("Ничья!")
            break
        cnt += 1


def new_game():
    while True:
        new = input("Хотите сыграть еще? (Y/N): ")
        if new in ["Y","N"]:
            if new == "Y":
                lets_go()
            if new == "N":
                print("Спасибо за игру!")
                break
        else:
            print("Пожалуйста, Y или N")
            continue


print("Игра Крестики-нолики\nИграют 2 человека, ходы по очереди, начинают крестики.")
N = field_size_choice()

lets_go()
new_game()