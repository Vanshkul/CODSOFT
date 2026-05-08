import math

AI = 'X'
HUMAN = 'O'
EMPTY = ' '

def print_board(board):
    for i, row in enumerate(board):
        print(f" {row[0] } | {row[1]} | {row[2]} ")
        if i < 2:
            print("-----------")

def check_winner(b):
    win_states = [
        [b[0][0], b[0][1], b[0][2]], [b[1][0], b[1][1], b[1][2]], [b[2][0], b[2][1], b[2][2]],
        [b[0][0], b[1][0], b[2][0]], [b[0][1], b[1][1], b[2][1]], [b[0][2], b[1][2], b[2][2]],
        [b[0][0], b[1][1], b[2][2]], [b[2][0], b[1][1], b[0][2]]
    ]
    if [AI, AI, AI] in win_states: return 10
    if [HUMAN, HUMAN, HUMAN] in win_states: return -10
    return 0

def is_moves_left(board):
    for row in board:
        if EMPTY in row: return True
    return False

def minimax(board, depth, is_max, alpha, beta):
    score = check_winner(board)
    
    if score == 10: return score - depth
    if score == -10: return score + depth
    if not is_moves_left(board): return 0

    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = AI
                    best = max(best, minimax(board, depth + 1, False, alpha, beta))
                    board[i][j] = EMPTY
                    alpha = max(alpha, best)
                    if beta <= alpha: break
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = HUMAN
                    best = min(best, minimax(board, depth + 1, True, alpha, beta))
                    board[i][j] = EMPTY
                    beta = min(beta, best)
                    if beta <= alpha: break
        return best

def find_best_move(board):
    best_val = -math.inf
    move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = AI
                move_val = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_val > best_val:
                    move = (i, j)
                    best_val = move_val
    return move

board = [[EMPTY]*3 for _ in range(3)]
print("Tic-Tac-Toe: AI (X) vs Human (O)")

while is_moves_left(board) and check_winner(board) == 0:
    print_board(board)
    try:
        row, col = map(int, input("Enter row and col (0-2) separated by space: ").split())
        if board[row][col] != EMPTY: raise ValueError
        board[row][col] = HUMAN
    except:
        print("Invalid move! Try again."); continue

    if not is_moves_left(board) or check_winner(board) != 0: break

    print("\nAI is thinking...")
    ai_row, ai_col = find_best_move(board)
    board[ai_row][ai_col] = AI

print_board(board)
final_score = check_winner(board)
if final_score > 0: print("AI Wins!")
elif final_score < 0: print("You Win! ")
else: print("It's a Draw!")
