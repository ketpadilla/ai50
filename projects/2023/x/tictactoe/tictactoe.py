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
    
    # Count the number of X's and O's on the board
    xCount, oCount = 0, 0

    # Check the board for the number of X's and O's
    for row in board:
        for cell in row:
            if cell == X:
                xCount += 1
            elif cell == O:
                oCount += 1
    
    # Determine who's turn it is
    return X if not terminal(board) and xCount == oCount else O if xCount > oCount else None


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create a set of all possible actions
    possibleActions = set()

    # Check the board for empty places
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """

    # Check if the action is valid
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Check if the game is over
    if terminal(board):
        raise Exception("Game over")

    # Create a copy of the board
    newBoard = copy.deepcopy(board)

    # Make a move 
    newBoard[action[0]][action[1]] = player(board)
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check if X won
    if checkRows(board, X) or checkCols(board, X) or checkDiagonals(board, X):
        return X
    
    # Check if O won
    if checkRows(board, O) or checkCols(board, O) or checkDiagonals(board, O):
        return O

    # If no winner is found, return None
    return None


def checkRows(board, player):
    """
    Returns True if the player has won in any row, False otherwise.
    """

    # Iterate over the rows
    for row in range(len(board)):
        count = 0
        for col in range(len(board[0])):
            if board[row][col] == player:
                count += 1
        if count == len(board):
            return True
    return False


def checkCols(board, player):
    """
    Returns True if the player has won in any column, False otherwise.
    """

    # Iterate over the columns
    for col in range(len(board[0])):
        count = 0
        for row in range(len(board)):
            if board[row][col] == player:
                count += 1
        if count == len(board):
            return True
    return False


def checkDiagonals(board, player):
    """
    Returns True if the player has won in any diagonal, False otherwise.
    """

    # Check the main diagonal
    count = 0
    for i in range(len(board)):
        if board[i][i] == player:
            count += 1
    if count == len(board):
        return True

    # Check the other diagonal
    count = 0
    for i in range(len(board)):
        if board[i][len(board) - i - 1] == player:
            count += 1
    if count == len(board):
        return True

    # If no diagonal is found, return False
    return False


def tie(board):
    """
    Returns 0 if the game is a tie
    """

    # Initialize the count
    count = (len(board * len(board[0])))
    
    # Iterate over rows and columns
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] is not EMPTY:
                count -= 1
    
    # Return tie
    return count == 0


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if the game is over
    if winner(board) or tie(board):
        return True
        
    # Return False if the game is not over
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Check ir X won
    if winner(board) == X:
        return 1
    
    # Check if O won
    if winner(board) == O:
        return -1
    
    # If there is no winner, return 0 (tie)
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    # Check if the game is over
    if terminal(board):
        return None
    
    # Initialize value
    value = float("-inf")

    # Check if it is X's turn
    if player(board) == X:
        for action in actions(board):
            minResult = minValue(result(board, action))
            if minResult > value:
                value = minResult
                selectedAction = action
        
        return selectedAction
    
    # Check if it is O's turn
    if player(board) == O:
        for action in actions(board):
            maxResult = maxValue(result(board, action))
            if maxResult < value:
                value = maxResult
                selectedAction = action
        
        return selectedAction


def maxValue(board):
    """
    Returns the maximum value of the board
    """

    # Check if the game is over
    if terminal(board):
        return utility(board)
    
    # Initialize the value
    value = -math.inf

    # Iterate over the actions
    for action in actions(board):
        value = max(value, minValue(result(board, action)))
    
    # Return the value
    return value


def minValue(board):
    """
    Returns the minimum value of the board
    """

    # Check if the game is over
    if terminal(board):
        return utility(board)
    
    # Initialize the value
    value = math.inf

    # Iterate over the actions
    for action in actions(board):
        value = min(value, maxValue(result(board, action)))
    
    # Return the value
    return value