"""
Tic Tac Toe Player
"""

import math

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
    count_X = sum(row.count(X) for row in board)
    count_O = sum(row.count(O) for row in board)

    #X is always the first player, hence it takes turns when
    #either count_X=count_O=0, at the start of the game
    #or after O has managed to make a move
    if count_X == count_O:
        return X
    #when it is not X's turn, it is O's
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    #unique actions
    #they can only be taken over empty cells
    action=set()
    for i in range(3):
        for j in range(3):
            if board[i][j]==EMPTY:
                action.add((i,j))
    return action



def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    #take the action as indexes for the board
    i, j = action

    #check for exception cases
    if 0>i or i>2 or j<0 or j>2:
        raise Exception
    if board[i][j]!=EMPTY:
        raise Exception
    # Make a deep copy of the board
    new_board = [row[:] for row in board]

    #change the board as indicated by the action
    new_board[i][j]=player(board)

    #return the resulted board
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #tests whther X or O won the game, using the rules of TicTacToe
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    for col in range(3):
        cX = 0
        cO = 0
        for row in board:
            if row[col] == X:
                cX += 1
            if row[col] == O:
                cO += 1
        if cX == 3:
            return X
        if cO == 3:
            return O

    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == X:
        return X
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == O:
        return O
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == X:
        return X
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == O:
        return O
    #cE = sum(row.count(EMPTY) for row in board)
    #if cE == 0:
    return None
    #return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    #checks if the boars is a terminal state

    #case we have a winner
    for row in board:
        if row.count(X)==3:
            return True
        if row.count(X)==3:
            return True

    for col in range(3):
        cX=0
        cO=0
        for row in board:
            if row[col]==X:
                cX+=1
            if row[col]==O:
                cO+=1
        if cX==3:
            return True
        if cO==3:
            return True

    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==X:
        return True
    if board[0][0]==board[1][1] and board[1][1]==board[2][2] and board[2][2]==O:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == X:
        return True
    if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[2][0] == O:
        return True

    #case we have a tie
    cE= sum(row.count(EMPTY) for row in board)
    if cE==0:
        return True

    #case the board is not a terminal state
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #X won
    if winner(board)==X:
        return 1
    #O won
    elif winner(board)==O:
        return -1
    #it's a tie
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board)==X:
        #maximum value from the choices O's possible moves give us
        t=float('-inf')
        for action in actions(board):
            if minval(result(board,action))>t:
                act=action
                t=minval(result(board,action))
    else:
        # minium value from the choices X's possible moves give us
        t = float('inf')
        for action in actions(board):
            if maxval(result(board, action)) < t:
                act = action
                t=maxval(result(board, action))
    if terminal(board)==False:
        return act
    else:
        return None


def maxval(board):

    """
    Returns the optimal value that can be obtained
    for the max player on the given board.
    """

    #helper method for choosing the maximum value of a possible terminal
    # state after both max and min choose their best values
    v=float('-inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=max(v,minval(result(board,action)))
    return v

def minval(board):
    """
       Returns the optimal value that can be obtained
       for the min player on the given board.
    """

    # helper method for choosing the minimum value of a possible terminal
    # state after both max and min choose their best values
    v=float('inf')
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v=min(v,maxval(result(board,action)))
    return v