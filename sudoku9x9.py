
def check_row_len(row):
    return len(set(row)) == 9

def check_board(board):
    if len(board) !=9:
        return False 
    for i in range(len(board)):
        if not check_row_len(board[i]):
            return False
        else: 
            continue
    return True

def check_squares(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            square = []
            for x in range(0, 3):
                for y in range(0, 3):
                    square.append(board[i+y][j+x])
            if square and len(set(square)) != 9:
                return False
    return True

def check_sudoku(board):
    return check_board(board) and check_squares(board)
    
