import random

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

currentplayer = "X"
winner = True
gamerunning = True

#game board
def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

    
#player input
def playerinput(board):
    inp = int(input("enter num in a range 1,9 : "))
    if board[inp-1] ==  "-":
        board[inp-1] = currentplayer
    else:
        print("player is already at the spot : ")
        
#check for win and tie

def checkforwinhorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
        
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
        
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        

def checkforwinrow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
        
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
        
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True
    
    
def checkforwindiag(board):
    if board[0] == board[4] == board[8] and board[0] != "-":
        return True
    
    elif board[2] == board[4] == board[6] and board[2] != "-":
        return True
        

def checkifwin(board):
    global gamerunning 
    if checkforwinhorizontal(board):
        printboard(board)
        print(f"the winner is {winner}")
        gamerunning = False
     
    
    elif checkforwinrow(board):
        printboard(board)
        print(f"the winner is {winner}")
        gamerunning = False
            
    elif checkforwindiag(board):
        printboard(board)
        print(f"thewinner is {winner}")
        gamerunning = False
        
def checkiftie(board):
    global gamerunning
    if "-" not in board:
        print("it is tie")
        gamerunning = False
    
#switch player 

def switchplayer():
    global currentplayer
    if currentplayer == "X":
        currentplayer = "0"
    else:
        currentplayer = "X"
        
def computer(board):
    while currentplayer =="0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchplayer()
    
    
while gamerunning:
    printboard(board)
    playerinput(board)
    checkiftie(board)
    switchplayer()
    computer(board)
    checkifwin(board)
    checkiftie(board)
    
    