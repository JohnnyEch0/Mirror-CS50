from tictactoe import player, actions, result, winner, terminal, utility

EMPTY = None

board = [[EMPTY, "O", "X"],
            ["X", "X", "X"],
            ["O", "O", EMPTY]]

move = (0,0)
# print(player(board))
# print(actions(board))
# print(result(board, move))
print(winner(board))
# print(terminal(board))
# print(utility(board))