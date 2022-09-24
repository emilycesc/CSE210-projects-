## Tic Tac Toe
## Author: Emily Case
    
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']    
player = 1    
   
##defining 
Win = 1    
Draw = -1    
Running = 0    
Stop = 1       
Game = Running    
Mark = 'X'    
   
#Draw the board   
def DrawBoard():    
    print(" %c | %c | %c " % (board[1],board[2],board[3]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[4],board[5],board[6]))    
    print("___|___|___")    
    print(" %c | %c | %c " % (board[7],board[8],board[9]))    
    print("   |   |   ")    
   
#Check if the board spot is empty or not    
def CheckSpot(x):    
    if(board[x] == ' '):    
        return True    
    else:    
        return False    
   
#Check if a player has won or if it's ended in a tie
def main():    
    global Game    
    #Across   
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        Game = Win    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        Game = Win    
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        Game = Win    
    #Vertical    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        Game = Win    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        Game = Win    
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        Game=Win    
    #Diagonal   
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        Game = Win    
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        Game=Win    
    #Declares a tie once no further moves are available and if no win has already occured    
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        Game=Draw    
    else:            
        Game=Running    
    
print("Tic-Tac-Toe Game")    
print("Player 1 [X] --- Player 2 [O]\n")    
while(Game == Running):       
    DrawBoard()    
    if(player % 2 != 0):    
        print("Go Player 1")    
        Mark = 'X'    
    else:    
        print("Go Player 2")    
        Mark = 'O'    
    choice = int(input("Enter the square you wish to mark by selecting a number from [1-9]: "))    
    if(CheckSpot(choice)):    
        board[choice] = Mark    
        player+=1    
        main()    
    
    
DrawBoard()    
if(Game==Draw):    
    print("This game has ended in a draw.")    
elif(Game==Win):    
    player-=1    
    if(player%2!=0):    
        print("Congratulations on winning, Player 1!")    
    else:    
        print("Congratulations on winning, Player 2!")    
