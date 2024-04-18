"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None
count = 0


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
    empty_tiles = 0
    for i, row in enumerate(board):
        for tile in row:
            if tile == EMPTY:
                empty_tiles +=1

    if empty_tiles % 2 == 0:
        # number is even
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()

    for i, row in enumerate(board):
        for j, tile in enumerate(row):
            if tile == EMPTY:
                actions.add((i, j))

    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    if not -1 < i < 3 or -1 < j < 3:
        raise ValueError
    board_copy = copy.deepcopy(board)
    if board_copy[i][j] is not None:
        raise Exception
    else:
        char = player(board)
        board_copy[i][j] = char
    return board_copy



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i, row in enumerate(board):
        row_string = ""
        column_string = ""

        for j, tile in enumerate(row):
            try:
                row_string += tile
            except TypeError:
                pass
            try:
                column_string += board[j][i]
            except TypeError:
                pass




        if row_string == "OOO" or column_string=="OOO":
            return O
        elif row_string == "XXX" or column_string == "XXX":
            return X

    try:
        diag_string = board[0][0] + board[1][1] + board[2][2]
    except TypeError:
        diag_string = None
    try:
        diag_string2 = board[0][2] + board[1][1] + board[2][0]
    except TypeError:
        diag_string2 = None

    if diag_string == "OOO" or diag_string2 == "OOO":
        return O
    elif diag_string == "XXX" or diag_string2 == "XXX":
        return X

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if actions(board) == set():
        return True
    if winner(board):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if not terminal(board):
        raise BufferError
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    player_ = player(board)

    move_evaluations = []
    actions_ = []

    for i, act in enumerate(actions(board)):
        # move_eval = 0
        result_ = result(board=board, action=act)
        actions_.append(act)
        if terminal(result_):
                move_evaluations.append(utility(result_))
        else:
            while not terminal(result_):
                result_ = result(result_, minimax(result_))
            print("terminal found")
            points = utility(result_)
            move_evaluations.append(points)


    if player_ == X:
        indx = move_evaluations.index(max(move_evaluations))
    elif player_ == O:

        indx = move_evaluations.index(min(move_evaluations))
    best_act = actions_[indx]

    global count
    count += 1
    # print(count)
    if count > 2000000:
        raise MemoryError

    return best_act

