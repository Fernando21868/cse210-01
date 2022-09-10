# Constants for string values.
ALL_SPACES = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
X, O = 'X', 'O'


def main():
    # Create a board dictionary.
    game_board = get_board()
    # X goes first, O goes next.
    current_player, next_player = X, O

    # Main game loop.
    while True:
        # Display the board on the screen:
        print(get_board_str(game_board))

        # Keep asking the player until they enter a number 1-9:
        move = None
        while not is_valid_space(game_board, move):
            print(f"{current_player}'s turn to choose a square (1-9):")
            move = input('> ')
        # Make the move.
        update_board(game_board, move, current_player)

        # Check if the game is over:
        # Check for a winner.
        if is_winner(game_board, current_player):
            print(get_board_str(game_board))
            print(current_player + ' has won the game!')
            break
        # Check for a tie.
        elif is_board_full(game_board):
            print(get_board_str(game_board))
            print('The game is a tie!')
            break
        # Switch turns to the next player:
        current_player, next_player = next_player, current_player
    print('Thanks for playing!')


def get_board():
    """Create a new, tic-tac-toe board.
    Parameters
        None
    Return
        Tic-tac-toe dictionary board.
    """
    board = {}
    for space in ALL_SPACES:
        # All spaces start as ordered numbers.
        board[space] = space
    return board


def get_board_str(board):
    """Return a text-representation of the board.
    Parameters
        board: Tic-tac-toe dictionary board.
    Return
        A string representation of the board.
    """
    return f'''
{board['1']}|{board['2']}|{board['3']}
-+-+-
{board['4']}|{board['5']}|{board['6']}
-+-+-
{board['7']}|{board['8']}|{board['9']}'''


def is_valid_space(board, space):
    """Returns True if the space on the board is a valid space number and the space is available.
    Parameters
        board: Tic-tac-toe board.
        space: The current player's movement.
    Return
        True if the space on the board is a valid space number and the space is available.
    """
    return space in ALL_SPACES and board[space] in ALL_SPACES


def is_winner(board, player):
    """Return True if player is a winner.
    Parameters
        board: Tic-tac-toe board.
        player: The current player.
    Return
        True if player is a winner
    """
    b, p = board, player
    # Check for 3 marks across 3 rows, 3 columns, and 2 diagonals.
    return ((b['1'] == b['2'] == b['3'] == p) or
            (b['4'] == b['5'] == b['6'] == p) or
            (b['7'] == b['8'] == b['9'] == p) or
            (b['1'] == b['4'] == b['7'] == p) or
            (b['2'] == b['5'] == b['8'] == p) or
            (b['3'] == b['6'] == b['9'] == p) or
            (b['3'] == b['5'] == b['7'] == p) or
            (b['1'] == b['5'] == b['9'] == p))


def is_board_full(board):
    """Return True if every space on the board has been taken.
    Parameters
        board: Tic-tac-toe board.
    Return
        True if every space on the board has been taken.
    """
    for space in ALL_SPACES:
        if board[space] in ALL_SPACES:
            # If any space is available, return False.
            return False
    # No spaces are available, so return True.
    return True


def update_board(board, space, mark):
    """Sets the space on the board to mark.
    Parameters
        board: Tic-tac-toe board.
        space: The current player's movement.
        mark: The mark (X or O) of the current player.
    Return
    """
    board[space] = mark


if __name__ == '__main__':
    main()
