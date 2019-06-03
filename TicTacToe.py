import random

def printboard(board):
    print()
    print(board[0]+" | "+board[1]+" | "+board[2])
    print("---------")
    print(board[3]+" | "+board[4]+" | "+board[5])
    print("---------")
    print(board[6]+" | "+board[7]+" | "+board[8])
    print()

def checkboard(board):
    if board[0]+board[1]+board[2]=="xxx":
        return 1
    elif board[3]+board[4]+board[5]=="xxx":
        return 1
    elif board[6]+board[7]+board[8]=="xxx":
        return 1
    elif board[0]+board[3]+board[6]=="xxx":
        return 1
    elif board[1]+board[4]+board[7]=="xxx":
        return 1
    elif board[2]+board[5]+board[8]=="xxx":
        return 1
    elif board[0]+board[4]+board[8]=="xxx":
        return 1
    elif board[2]+board[4]+board[6]=="xxx":
        return 1
    elif board[0]+board[1]+board[2]=="ooo":
        return -1
    elif board[3]+board[4]+board[5]=="ooo":
        return -1
    elif board[6]+board[7]+board[8]=="ooo":
        return -1
    elif board[0]+board[3]+board[6]=="ooo":
        return -1
    elif board[1]+board[4]+board[7]=="ooo":
        return -1
    elif board[2]+board[5]+board[8]=="ooo":
        return -1
    elif board[0]+board[4]+board[8]=="ooo":
        return -1
    elif board[2]+board[4]+board[6]=="ooo":
        return -1
    else:
        return 0        

def checkmoves(board):
    moves=[]
    for field in board:
        if field !="x" and field !="o":
            moves.append(field)            
    return(moves)

def possibleMoves(board, maximizingPlayer):
    moves=[]
    move=board.copy()
    if maximizingPlayer:
        player = "x"
    else:
        player = "o"
    i=0
    while i < len(board):
        move=board.copy()
        if move[i]!="x" and move[i] !="o":
            move[int(i)]=player
            moves.append(move)
        i+=1
    random.shuffle(moves)
    return moves
def possibleMovesCount(board):
    count = 0
    for field in board:
        if field !="x" and field !="o":
            count += 1           
    return(count)

def minimax(board, maximizingPlayer):
    if checkboard(board) !=0:
        return checkboard(board)
    if possibleMovesCount(board) == 0:
        return checkboard(board)
    if maximizingPlayer:
        maxEval = -100
        for move in possibleMoves(board, True):
            eval = minimax(move, False)
            maxEval = max(maxEval, eval)
        return maxEval
    else:
        minEval = 100
        for move in possibleMoves(board, False):
            eval = minimax(move, True)
            minEval = min(minEval, eval)
        return minEval

def compMove (board,maximizingPlayer):
    if maximizingPlayer:
        maxEval = -100
        bestMove = []
        for move in possibleMoves(board, True):
            eval = minimax(move, False)
            if eval > maxEval:
                bestMove = move
                maxEval = eval
        return bestMove
    else:
        minEval = 100
        bestMove = []
        for move in possibleMoves(board, False):
            eval = minimax(move, True)
            if eval < minEval:
                bestMove = move
                minEval = eval
        return bestMove
    
def runGame():
    try:
        playerName = input("Let's play a round of Tic Tac Toe! What's your name? ")
        playerName2 = playerName+" 2.0"
        computerName = ["Triple X", playerName2]
        computerName = random.choice(computerName)

        print("Nice to meet you "+str(playerName)+"! You're playing against "+str(computerName)+".")
       
        print()
        board = ["1","2","3","4","5","6","7","8","9"]
        printboard(board)

        startingPlayer = input("Do you want to start? (Y/N)")
        if startingPlayer == "y" or "Y":
            print()
            print("Good luck!")
            print()
        else:
            print()
            print("Ok. I will start then.")
            print()

        player="x"
        maximizingPlayer = True
        
        round=0
        for i in range(10):
            if round%2 == 0:
                player = "x"
                maximizingPlayer = True
            else:
                player = "o"
                maximizingPlayer = False

            if checkboard(board)==1:
                print("X wins!")
                break
            if checkboard(board)==-1:
                print("O wins!")
                break
            if possibleMovesCount(board)==0:
                print("Draw!")
                break
            print("Round: "+str(round)+" - possible moves: "+str(checkmoves(board)))
            if round!= 0:
                forecast=(minimax(board,maximizingPlayer))
                if forecast == 1:
                    print("Forecast: X wins.")
                if forecast == -1:
                    print("Forecast: O wins.")
                if forecast == 0:
                    print("Forecast: Draw.")
            
            if startingPlayer == "y":
                if player == "x":
                    playerMove = int(input())
                    board[playerMove-1]=player
                if player == "o":
                    board = compMove(board,False)
            else:
                if player == "x":
                    board = compMove(board, True)
                if player == "o":
                    playerMove = int(input())
                    board[playerMove-1]=player
            round +=1
            printboard(board)
    finally:
        if input("New game? (Y/N)")=="y" or "Y":
            runGame()           
runGame()
