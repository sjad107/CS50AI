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
    numofX = 0
    numofO = 0
    if terminal(board):
        return None
    else:
        for i in board:
            for j in i:
                if j == "X":
                    numofX+=1
                elif j == "O":
                    numofO+=1
        if numofX <= numofO:
            return "X"
        else:
            return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    moves = set()
    for i in range(len(board)):
        for j in range(3):
            if (board[i][j] == "X") or (board[i][j] == "O"):
                continue
            else:
                moves.add((i,j))
    
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result_board = copy.deepcopy(board)
    i, j = action
    if board[i][j] != None:
        raise Exception
    else:
        result_board[i][j] = player(board)
    
    return result_board




def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    r = ""
    for i in range(len(board)):
        for j in range(len(board)-2):
            if (board[i][j] ==board[i][j+1] ==board[i][j+2] == "X"):
                return "X"
            elif (board[i][j] ==board[i][j+1] ==board[i][j+2] == "O"):
                return "O"
    # Check columns
    for i in range(len(board)-2):
        for j in range(len(board)):
            if (board[i][j] ==board[i+1][j] ==board[i+2][j] == "X"):
                return "X"
            elif (board[i][j] ==board[i+1][j] ==board[i+2][j] == "O"):
                return "O"
    #Check diagonally
    for i in range(len(board)-2):
        for j in range(len(board)-2):
            if (board[i][j] ==board[i+1][j+1] ==board[i+2][j+2] == "X"):
                return "X"
            elif (board[i][j] ==board[i+1][j+1] ==board[i+2][j+2] == "O"):
                return "O"
            if (board[i][j+2] ==board[i+1][j+1] ==board[i+2][j] == "X"):
                return "X"
            elif (board[i][j+2] ==board[i+1][j+1] ==board[i+2][j] == "O"):
                return "O"
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    for i in board:
        if EMPTY in i:
            return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == "X":
        return 1
    elif winner(board) == "O":
        return (-1)
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    optimal_action = None
    p = player(board)

    if player(board) == "X":
        v = -100
        for action in actions(board):
            if v < (Min_Value(result(board,action))):
                v = (Min_Value(result(board,action)))
                optimal_action = action
    
    else:
        v = 100
        for action in actions(board):
            if v > (Max_Value(result(board,action))):
                v = (Max_Value(result(board,action)))
                optimal_action = action
    return optimal_action      



def Max_Value(board):
    if terminal(board):
        return utility(board)
    else:
        v = -100
        for action in actions(board):
            if v < (Min_Value(result(board,action))):
                v = (Min_Value(result(board,action)))
    return v

def Min_Value(board):
    if terminal(board):
        return utility(board)
    else:
        v = 100
        for action in actions(board):
            if v > (Max_Value(result(board,action))):
                v = (Max_Value(result(board,action)))
    return v