def print_board(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end=" ")
            if j < 2:
                print("|", end=" ")
        print()
        if j < 2:
            print("-" * 9)

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    
    if all(board[i][i] == player for i in range(3)):
        return True
    
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    
    return False

def check_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    