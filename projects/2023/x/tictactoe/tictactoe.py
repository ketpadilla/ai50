"""
Tic Tac Toe Player
"""

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
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    
    # Check if it is X's turn
    if xCount > oCount:
        return O

    # Else, it is O's turn
    return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """

    # Create a set of all possible actions
    possibleActions = set()

    # Check the board for empty places
    for i in range(0, len(board)):
        for j in range(0, len(board[0])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))

    # Return the set of possible actions
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    
    # Create a copy of the board
    newBoard = copy.deepcopy(board)

    # Make a move 
    newBoard[action[0]][action[1]] = player(board)

    # Return the new board
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Check rows
    for row in board:
        if all(i == row[0] for i in row):
            return row[0]
    # Check columns
    for col in range(3):
        if all(row[col] == board[0][col] for row in board):
            return board[0][col]

    # Check main diagonal
    if all(board[i][i] == board[0][0] for i in range(3)):
        return board[0][0]

    # Check reverse diagonal
    if all(board[i][2 - i] == board[0][2] for i in range(3)):
        return board[0][2]
    
    # If there is no winner, return None
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    # Check if there is a winner
    if winner(board) is not None:
        return True
    
    # Check if there are any empty places left
    if not any(EMPTY in sublist for sublist in board) and winner(board) is None:
        return True
        
    # Return False if the game is not over
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # Check if the game is not over
    if not terminal(board):
        return None
        
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
    
    # Check if it is X's turn
    if player(board) == X:
        value, move = maxValue(board)

    # Check if it is O's turn
    if player(board) == O:
        value, move = minValue(board)
        
    return move


def maxValue(board):
    """
    Returns the maximum value of the board
    """

    # Check if the game is over
    if terminal(board):
        return utility(board), None

    # Initialize the value and move
    value = float('-inf')
    move = None

    for action in actions(board):
        aux, act = minValue(result(board, action))
        # Check if the value is greater than the current value
        if aux > value:
            value = aux
            move = action
        # Check if "X" won
        if value == 1:
            return value, move

    return value, move


def minValue(board):
    """
    Returns the minimum value of the board
    """

    # Check if the game is over
    if terminal(board):
        return utility(board), None
    
    # Initialize the value and move
    value = float('inf')
    move = None

    for action in actions(board):
        aux, act = maxValue(result(board, action))
        # Check if the value is less than the current value
        if aux < value:
            value = aux
            move = action
        # Check if "O" won
        if value == -1:
            return value, move

    return value, move