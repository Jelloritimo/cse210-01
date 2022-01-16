'''CSE210 - Week-1
Tic-Tac-Toe
Bryce Williams'''

import random

def main():
    turn = turns("")
    board_fun = board()
    while not (game_draw(board_fun) or game_set(board_fun)):
        print_board(board_fun)
        moves(board_fun, turn)
        turn = turns(turn)
    print("Good game. Thanks for playing!")

def board():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    return board

def print_board(board):
    row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
    print(row1)
    row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
    print(row2)
    row3 = (f"{board[6]}|{board[7]}|{board[8]}")
    print(row3)

def turns(turn_now):
    if turn_now == "" or turn_now == "o":
        return "x"
    elif turn_now == "x":
        return "o"

def moves(board, turn):
    player_move = int(input(f"{turn}'s turn to choose a square(1-9): "))
    board[player_move - 1] = turn
        

def game_draw(board):
    for i in board:
        if i != "x" or i != "o":
            return False
        return True

def game_set(board):
    ###Inspiration from course###
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6])
    

main()
