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
    num_of_x =0
    num_of_o = 0
    for i in board:
        for j in i:
            if j is None:
                pass
            elif j == "X":
                num_of_x+=1
            else:
                num_of_o+=1
    if num_of_x < num_of_o:
        return X
    elif num_of_x > num_of_o:
        return O
    else:
        return X



def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_move = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possible_move.add((i, j))
    return possible_move

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board = copy.deepcopy(board)
    current_player = player(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if i == action[0]:
                if j == action[1]:
                    if board[i][j] == EMPTY:
                        board[i][j] = current_player
                    else:
                        raise Exception
    return board


def winner(board):
    """ 
    Returns the winner of the game, if there is one.
    """ 
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == EMPTY:
                pass
            elif board[i][0] == X:
                return X
            elif board[i][0]== O:
                return O
            else:
                return None
            
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j]:
            if board[0][j] == EMPTY:
                pass
            elif board[0][j] == X:
                return X
            elif board[0][j] == O:
                return O
            else:
                return None
            

    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == EMPTY:
            pass
        elif board[0][0] == X:
            return X
        elif board[0][0] == O:
            return O
        else:
            return None
    
    if board[2][0] == board[1][1] == board[0][2]:
        if board[2][0] == EMPTY:
            pass
        elif board[0][2] == X:
            return X
        elif board[1][1] == O:
            return O
        else:
            return None
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    win = winner(board)
    if win == X:
        return True
    elif win == O:
        return True
    
    for i in range(3):
        for j in range(3):
            if  board[i][j] == None:
                return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    result = winner(board)

    if result == X:
        return 1
    elif result == O:
        return -1
    elif result == None:
        return 0

def max_value(board):
    v = float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    v = float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        best_action = []
        for action in actions(board):
            best_action.append([min_value(result(board, action)), action])
        return sorted(best_action, reverse = True)[0][1]
    elif player(board) ==O:
        best_action = []
        for action in actions(board):
            best_action.append([max_value(result(board, action)), action])

        return sorted(best_action)[0][1]
