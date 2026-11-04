
import random
from colorama import init, Fore, Style

init(autoreset=True)


# 1. DISPLAY THE GAME BOARD
def display_board(board):

    print()

    def colored_cell(cell):
        if cell == "X":
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == "O":
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return cell

    print(f" {colored_cell(board[0])} | {colored_cell(board[1])} | {colored_cell(board[2])} ")
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(f" {colored_cell(board[3])} | {colored_cell(board[4])} | {colored_cell(board[5])} ")
    print(Fore.CYAN + "---+---+---" + Style.RESET_ALL)
    print(f" {colored_cell(board[6])} | {colored_cell(board[7])} | {colored_cell(board[8])} ")

    print()


# 2. PLAYER CHOOSES SYMBOL
def player_choice():

    symbol = ""

    while symbol not in ["X", "O"]:

        symbol = input(
            Fore.CYAN + "Choose your symbol (X/O): " + Style.RESET_ALL
        ).upper().strip()

        if symbol not in ["X", "O"]:
            print(
                Fore.RED + "Invalid choice. Please choose 'X' or 'O'."
                + Style.RESET_ALL
            )

    # AI gets the opposite symbol
    ai_symbol = "O" if symbol == "X" else "X"

    return symbol, ai_symbol


# 3. PLAYER MAKES A MOVE
def player_move(board, symbol):

    move = -1

    while True:

        try:

            move = int(input(
                Fore.CYAN +
                f"Player {symbol}, enter your move (1-9): "
                + Style.RESET_ALL
            ))

            if move not in range(1, 10):

                print(
                    Fore.RED +
                    "Invalid input. Please enter a number between 1 and 9."
                    + Style.RESET_ALL
                )

            elif not board[move - 1].isdigit():

                print(
                    Fore.RED +
                    "That position is already taken. Choose another."
                    + Style.RESET_ALL
                )

            else:

                board[move - 1] = symbol
                break

        except ValueError:

            print(
                Fore.RED +
                "Invalid input. Please enter a number between 1 and 9."
                + Style.RESET_ALL
            )


# 4. AI MAKES A MOVE
def ai_move(board, ai_symbol, player_symbol):

    # First priority: AI tries to win
    for i in range(9):

        if board[i].isdigit():

            board_copy = board[:]
            board_copy[i] = ai_symbol

            if check_winner(board_copy, ai_symbol):

                board[i] = ai_symbol
                return

    # Second priority: AI blocks the player
    for i in range(9):

        if board[i].isdigit():

            board_copy = board[:]
            board_copy[i] = player_symbol

            if check_winner(board_copy, player_symbol):

                board[i] = ai_symbol
                return

    # Third priority: AI chooses a random available position
    available_moves = [
        i for i in range(9) if board[i].isdigit()
    ]

    if available_moves:

        move = random.choice(available_moves)
        board[move] = ai_symbol


# 5. CHECK WINNING CONDITION
def check_winner(board, symbol):

    win_conditions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for condition in win_conditions:

        if (
            board[condition[0]]
            == board[condition[1]]
            == board[condition[2]]
            == symbol
        ):

            return True

    return False


# 6. CHECK WHETHER THE BOARD IS FULL
def check_full(board):

    return all(not cell.isdigit() for cell in board)


# 7. MAIN GAME FUNCTION
def tic_tac_toe():

    print(
        Fore.CYAN +
        "Welcome to Tic-Tac-Toe!" +
        Style.RESET_ALL
    )

    player_name = input(
        Fore.CYAN + "Enter your name: " + Style.RESET_ALL
    )

    while True:

        board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        player_symbol, ai_symbol = player_choice()

        turn = "Player"
        game_on = True

        while game_on:

            display_board(board)

            if turn == "Player":

                player_move(board, player_symbol)

                if check_winner(board, player_symbol):

                    display_board(board)

                    print(
                        Fore.GREEN +
                        f"Congratulations {player_name}! "
                        "You have won the game!" +
                        Style.RESET_ALL
                    )

                    game_on = False

                elif check_full(board):

                    display_board(board)

                    print(
                        Fore.YELLOW +
                        "It's a tie!" +
                        Style.RESET_ALL
                    )

                    game_on = False

                else:

                    turn = "AI"

            else:

                print(Fore.MAGENTA + "AI is making its move...")

                ai_move(board, ai_symbol, player_symbol)

                if check_winner(board, ai_symbol):

                    display_board(board)

                    print(
                        Fore.RED +
                        "AI has won the game! Better luck next time."
                        + Style.RESET_ALL
                    )

                    game_on = False

                elif check_full(board):

                    display_board(board)

                    print(
                        Fore.YELLOW +
                        "It's a tie!" +
                        Style.RESET_ALL
                    )

                    game_on = False

                else:

                    turn = "Player"

        # Ask whether the player wants another game
        play_again = input(
            Fore.CYAN +
            "Do you want to play again? (yes/no): " +
            Style.RESET_ALL
        ).strip().lower()

        if play_again != "yes":

            print(
                Fore.CYAN +
                "Thank you for playing Tic-Tac-Toe! Goodbye!" +
                Style.RESET_ALL
            )

            break


# 8. PROGRAM ENTRY POINT
if __name__ == "__main__":

    tic_tac_toe()
