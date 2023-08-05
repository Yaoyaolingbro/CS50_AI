"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count, O_count = 0, 0
    for i in board:
        for cell in i:
            X_count += (cell == X)
            O_count += (cell == O)
    return X if X_count == O_count else O
    # python 中的三元运算符


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range (3):
        for j in range (3):
            if board[i][j] == EMPTY:
                actions.append((i,j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board) # python中建立深拷贝
    cell = player(board)
    i,j = action
    if board[i][j] != EMPTY:
        raise Exception("infeasible move")
    new_board[i][j] = cell
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2]) and board[i][0] != EMPTY:
            return board[i][0]
        if (board[0][i] == board[1][i] == board[2][i]) and board[0][i] != EMPTY:
            return board[0][i]
    
    if (board[0][0] == board[1][1] == board[2][2]) and board[0][0] != EMPTY:
        return board[0][0]

    if (board[0][2] == board[1][1] == board[2][0]) and board[0][2] != EMPTY:
        return board[0][2] 

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # 一定自习思考为什么是这个顺序，有bug
    if winner(board) != None:
        return True
    for h in board:
        for cell in h:
            if cell == EMPTY:
                return False 
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == X:
        return 1
    elif win == O:
        return -1
    else:
        return 0
    
def score(board, depth):
    win = winner(board)
    if win == X:
        return 10 - depth
    elif win == O:
        return depth - 10
    else:
        return 0

# 在我的参考资料中有设计depth的相关实现
def minimax(board, depth):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return score(board,depth), None
    
    depth += 1
    scores = []
    moves = []

    for move in actions(board):
        possible_game = result(board, move)
        move_score,_ = minimax(possible_game, depth)
        scores.append(move_score)
        moves.append(move)

    if player(board) == X:
        max_score_index = max(enumerate(scores), key=lambda x: x[1])[0]
        best_move = moves[max_score_index]
        return scores[max_score_index], best_move
    else:
        min_score_index = min(enumerate(scores), key=lambda x: x[1])[0]
        best_move = moves[min_score_index]
        return scores[min_score_index], best_move

    
    
