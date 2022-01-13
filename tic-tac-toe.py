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
# def main():
#     rps_win = rps()
#     print("")
#     if rps_win == True:
#         o_tic_tac()
#     elif rps_win == False:
#         x_tic_tac()
# #
# ##
# ###ROCK PAPER SCISSORS TO DESCIDE WHO GOES FIRST###
# ##
# #
# def rps():
#     rps_settled = 0
#     rps_win = False
#     rps_moves = [1, 2, 3]
#     print("Let's decide who goes first.")
#     while rps_settled == False:
#         user_rps = int(input("1.Rock\n2.Paper\n3.Scissors\nPick your move!: "))
#         cpu_rps = random.choice(rps_moves)
#         print(f"The Computer chose: {cpu_rps}")
#         if user_rps == cpu_rps:
#             print("A tie! Let's try again!")
#         elif (user_rps == 2 and cpu_rps == 3) or (user_rps == 3 and cpu_rps == 1) or (user_rps == 1 and cpu_rps == 2):
#             print("You Lost! \nThe Computer goes first.")
#             rps_settled == True
#             break
#         elif (user_rps == 1 and cpu_rps == 3) or (user_rps == 2 and cpu_rps == 1) or (user_rps == 3 and cpu_rps == 2):
#             print("You Won! \nYou will go first.")
#             rps_settled == True
#             rps_win == True
#             break
#         else: print("Invalid input! Try again.")

#     return rps_win
# #
# ##
# ###YOU'RE GOING FIRST###
# ##
# #
# def x_tic_tac():
#     loop = True
#     game_set = False
#     draw = False
#     victory = False
#     row1 = ("1|2|3\n-+-+-")
#     print(row1)
#     row2 = (f"4|5|6\n-+-+-")
#     print(row2)
#     row3 = (f"7|8|9")
#     print(row3)
#     user = "x(YOU)"
#     cpu = "o(CPU)"
#     user_moves_used = []
#     cpu_moves_used = []
#     board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     cpu_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     while loop == True:
#         #
#         ##USER's move##
#         #
#         # moves_used.append(cpu_choice)
#         if len(user_moves_used) + len(cpu_moves_used) > 6:
#             for i in cpu_moves_used:
#                 if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                     game_set == True
#                     victory == False
#                     break
#             game_set == True
#             draw == True
#             break
#         user_choice = int(input(f"{user}'s turn to choose a square (1-9): "))
#         for i in range(len(board)):
#             if board[i] == user_choice:
#                 board[i] = "x"
#         user_moves_used.append(user_choice)
#         row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
#         print(row1)
#         row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
#         print(row2)
#         row3 = (f"{board[6]}|{board[7]}|{board[8]}")
#         print(row3)
#         print("")
#         for i in user_moves_used:
#             if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                 game_set == True
#                 victory == True
#                 break
#         #
#         ##CPU's move##
#         #
#         # moves_used.append(user_choice)
#         if len(user_moves_used) + len(cpu_moves_used) > 6:
#             for i in user_moves_used:
#                 if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                     game_set == True
#                     victory == False
#                     break
#             game_set == True
#             draw == True
#             break
#         cpu_moves.remove(user_choice)
#         cpu_choice = random.choice(cpu_moves)
#         for i in range(len(board)):
#             if board[i] == cpu_choice:
#                 board[i] = "o"
#         cpu_moves.remove(cpu_choice)
#         cpu_moves_used.append(cpu_choice)
#         print(f"{cpu}'s turn to choose a square: {cpu_choice}")
#         row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
#         print(row1)
#         row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
#         print(row2)
#         row3 = (f"{board[6]}|{board[7]}|{board[8]}")
#         print(row3)
#         print("")
#         for i in cpu_moves_used:
#             if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                 game_set == True
#                 victory == False
#                 break
#     if game_set == True and victory == True:
#         print("YOU WIN!")
#     elif game_set == True and victory == False:
#         print("YOU LOSE...")
#     elif game_set == True and draw == True:
#         print("DRAW")
# #
# ##
# ###CPU'S GOING FIRST###
# ##
# #
# def o_tic_tac():
#     game_set = False
#     victory = False
#     cpu = "x(CPU)"
#     user = "o(YOU)"
#     board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     moves_used = []
#     user_moves_used = []
#     cpu_moves_used = []
#     cpu_moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
#     print(row1)
#     row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
#     print(row2)
#     row3 = (f"{board[6]}|{board[7]}|{board[8]}")
#     print(row3)
#     while game_set == False:
#         #
#         ##CPU's move##
#         #
#         # moves_used.append(user_choice)
#         cpu_moves.remove(user_choice)
#         cpu_choice = random.choice(cpu_moves)
#         board[cpu_choice - 1] == "x"
#         cpu_moves.remove(cpu_choice)
#         cpu_moves_used.append(cpu_choice)
#         print(f"{cpu}'s turn to choose a square: {cpu_choice}")
#         row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
#         print(row1)
#         row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
#         print(row2)
#         row3 = (f"{board[6]}|{board[7]}|{board[8]}")
#         print(row3)
#         print("")
#         for i in cpu_moves_used:
#             if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                 game_set == True
#                 victory == False
#                 break
#         #
#         ##USER's move##
#         #
#         # moves_used.append(cpu_choice)
#         user_choice = int(input(f"{user}'s turn to choose a square (1-9): "))
#         board[user_choice - 1] == "o"
#         user_moves_used.append(user_choice)
#         row1 = (f"{board[0]}|{board[1]}|{board[2]}\n-+-+-")
#         print(row1)
#         row2 = (f"{board[3]}|{board[4]}|{board[5]}\n-+-+-")
#         print(row2)
#         row3 = (f"{board[6]}|{board[7]}|{board[8]}")
#         print(row3)
#         print("")
#         for i in user_moves_used:
#             if i == (1 and 2 and 3) or (4 and 5 and 6) or (7 and 8 and 9) or (1 and 4 and 7) or (2 and 5 and 8) or (3 and 6 and 9) or (1 and 5 and 9) or (3 and 5 and 7):
#                 game_set == True
#                 victory == True
#                 break
#     if victory == True:
#         print("YOU WIN!")
#     elif victory == False:
#         print("YOU LOSE...")

# main()