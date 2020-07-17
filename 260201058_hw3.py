# 260201058
#Eray Okutay

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Ball Crush

# -*- coding: utf-8 -*-

print("Welcome to the Ball Crush game!")
print()
from random import randint
import time
#It is a shortcut for the define inputs type.
def integer(x):
   
    try:
        
        int(x)
        return True
    
    except ValueError:
        return False 


def display_ball_positions(ball_positions):
    A = ball_positions
    #I created a matris for not changing ball positions but showing Its' values one more bigger.
    B = [[0 for col in range(2)] for row in range(len(A))]
    #I assigned A's values +1 to B.
    for i in range(len(A)):
        A[i] = list(A[i])
        
        
            
        B[i][0] = A[i][0] + 1
        B[i][1] = A[i][1] + 1
        
        A[i] = tuple(A[i])
    
        
    
   
    for i in range(len(B)):
        B[i] = tuple(B[i])
        
      
    
    
    print(B)
    print()
    
    
    


def display_board(board):
    # I printed board puting space instead of commas.
    for i in board:
        
        print(*i, sep=' ')
    print()
        
        





def choose_ball(board):
    g = input("which ball ? ")
    
    
    
    #Checking the input whether it is correct or not.
    while not (integer(g[0]) and integer(g[-1])):
        print("It is not a ball position!")
        g = input("which ball ? ")
    
    while int(g[0]) > 5  or int(g[0]) < 0 or int(g[-1]) > 5  or int(g[-1]) < 0 :
        print("It is not a ball position!")
        g = input("which ball ? ")
    while  board[(int(g[0])-1)][(int(g[-1])-1)] != 1 :
        print("It is not a ball position!")
        g = input("which ball ? ")
        while not (integer(g[0]) and integer(g[-1])):
            print("It is not a ball position!")
            g = input("which ball ? ")
        while int(g[0]) > 5  or int(g[0]) < 0 or int(g[-1]) > 5  or int(g[-1]) < 0 :
            print("It is not a ball position!")
            g = input("which ball ? ")

                
            
    return g 

def get_valid_moves(pos, len_board):
     
    x = pos
    valid_moves = []
    # I am sure that, there is an easier way to do this.
    if x[-1] == str(len_board) and x[0] == "1" :  #(1,5)
        
        valid_moves.append("a")
        valid_moves.append("s")
        
    elif x[-1] == str(len_board) and x[0] == str(len_board): #(5,5)
        
        valid_moves.append("w")
        valid_moves.append("a")
    elif x[-1] == "1" and x[0] == "1" : #(1,1)
        
        valid_moves.append("d")
        valid_moves.append("s")
    elif x[-1] == "1" and x[0] == str(len_board) :     #(5,1)
        
        valid_moves.append("w")
        valid_moves.append("d")
    elif x[-1] == str(len_board) and (x[0] != "1" or x[0] != str(len_board)) : #(x,5)
        
        
            
        valid_moves.append("w")
        valid_moves.append("a")
        valid_moves.append("s")
    elif x[-1] == "1" and (x[0] != "1" or x[0] != str(len_board)):   #(x,1)
        
            
        valid_moves.append("w")
        valid_moves.append("s")
        valid_moves.append("d")
    elif x[0] == str(len_board) and (x[-1] != "1" or x[-1] != str(len_board)): #(5,x)
        
        valid_moves.append("a")
        valid_moves.append("d")
        valid_moves.append("w")
    elif x[0] == "1" and (x[-1] != "1" or x[-1] != str(len_board)): #(1,x)
        
        valid_moves.append("a")
        valid_moves.append("s")
        valid_moves.append("d")
    else :
        valid_moves.append("w")
        valid_moves.append("a")
        valid_moves.append("s")
        valid_moves.append("d")
    
    return valid_moves
    
    
            
def make_move(board, pos, valid_moves, ball_positions):     
    a = valid_moves
    b = ball_positions
    c = pos
    
    val = input()
    
    #Checking whether a contains the input or not.
    while val not in a:
        print("Enter a valid direction! ")
        print("Valid moves:",a,"")
        val =  input()    
    
    #Program finds index of the chosen position.
    for i in range(len(b)):
        
        
        
        if str(int(c[0])-1) == str(b[i][0]) and str(int(c[-1])-1) == str(b[i][-1]):
            
            g = i
    #it turns 0 of previous 1's value.       
    board[b[g][0]][b[g][-1]] = 0
    #It turns b to list for change it
    for i in range(len(b)):
        b[i] = list(b[i])
    #It changes the positions of 1's.
    if val == "w":
        
        b[g][0] = int(b[g][0]) -1 
        
    elif val == "s" :
        b[g][0] = int(b[g][0]) + 1
    elif val == "a" :
        b[g][-1] = int(b[g][-1]) - 1 
    elif val == "d" :
        b[g][-1] = int(b[g][-1]) + 1
    
    board[b[g][0]][b[g][-1]] = 1
    
    delete_ball(board, pos, ball_positions)
    
    
    

#I could use this on delete_ball function but by the time I see that we should write a check_collision function I was already finished delete ball function.                 
def check_collision(board, pos):
    c = pos
    b= board
    for i in range(len(b)):
        
        
        
        if str(int(c[0])-1) == str(b[i][0]) and str(int(c[-1])-1) == str(b[i][-1]):
            
            g = i
    if g != 0:
        return True
    else: 
        return False
    
    

def delete_ball(board, pos, ball_positions):
    B = ball_positions
    #Finds whether it is a collision is exist or not and deletes it from the ball positions.
    try:
        if B[0]==B[1] or B[0] == B[2] :
            del B[0]
        elif B[1] == B[2] :
            del B[1]
    except IndexError :
        if B[0]==B[1]:
            del B[0]
        
    

def main():
    len_board = 5
    board = [[0 for col in range(len_board)] for row in range(len_board)]  
 
    while True:
        ball_positions = [(randint(0, len_board-1), randint(0, len_board-1)) for i in range(3)]
        if len(ball_positions) == len(set(ball_positions)):
            break
    
    for pos in ball_positions:
        board[pos[0]][pos[1]] = 1

    start_time = time.time()
    
    while True:
        display_ball_positions(ball_positions)
        display_board(board)
        
        if len(ball_positions) == 1:
            break
        
        ball_pos = choose_ball(board)
        
        valid_moves = get_valid_moves(ball_pos, len(board))
        print("Valid moves:", valid_moves)
        
        make_move(board, ball_pos, valid_moves, ball_positions)
        
    end_time = time.time()

    minutes, seconds = divmod(end_time-start_time, 60)
    hours, minutes = divmod(minutes, 60)
    print("Game Over!")
    print("Passed time= {:02d}:{:02d}:{:02d}".format(int(hours), int(minutes),int(seconds)))
    
main()

x = input("Press Enter to quit: ")
