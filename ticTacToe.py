theBoard = {
    'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
    'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
    'low-L': ' ', 'low-M': ' ', 'low-R': ' '
}

def clearBoard(board):
    for key in board: board[key] = ' '
    
def printBoard(board):
    for pos, key in enumerate(list(board)):
        if (pos != 0 and (pos + 1) % 3 == 1):
            print('\n-+-+-')
            print(f"\n{board[key]}|", end="")
        elif ((pos + 1) % 3 == 0):
            print(f"{board[key]}")
        else:
            print(f"{board[key]}|", end="")


def checkBoard(board, token):
    
    return any(
                all(
                    (board[f"{pos_x}-{pos_y}"] == token)  pos_y in ['L', 'M', 'R']
                )
            for all pos_x in ['top', 'mid', 'low']
        )




def game():
    player = 0
    moves = {1:[], 2:[]}

    for i in range(9):
        
        printBoard(theBoard)
        move, token = input(f'Turn for Player {player + 1}. Enter position and token: ').strip().split()
        moves[player].append(token)
        theBoard[move] = token
        
        print(f"Player {player + 1}'s turn:")
        printBoard(theBoard)
        print()
        
        if checkBoard(theBoard, moves): 
            print(f"Player {player + 1} wins!")
            print("Game Over!")
            return

        player += 1
        player %= 2
    
    print("It's a stalemate. No one wins!")

if __name__ == "__main__":
    while True:
        if (input("Start game? (Y/n)").lower() == 'y'):
            game()
        else:
            break
    

