
import random
from collections import Counter
from colorama import init, Fore, Style

# Initialize Colorama
init(autoreset=True)


# --------------------------------------------------
# SET UP THE GAME
# --------------------------------------------------

moves = ["rock", "paper", "scissors"]

player_score = 0
ai_score = 0
tie_score = 0

# Store player's previous moves
player_history = []


# --------------------------------------------------
# FUNCTION 1: NORMALIZE USER INPUT
# --------------------------------------------------

def normalize_input(user_input):

    return user_input.strip().lower()


# --------------------------------------------------
# FUNCTION 2: DISPLAY GAME RULES
# --------------------------------------------------

def show_rules():

    print(Fore.CYAN + "\n========== GAME RULES ==========")

    print(Fore.GREEN + "1. Rock beats Scissors.")
    print(Fore.GREEN + "2. Scissors beats Paper.")
    print(Fore.GREEN + "3. Paper beats Rock.")
    print(Fore.YELLOW + "4. Same moves result in a tie.")

    print(Fore.CYAN + "================================")


# --------------------------------------------------
# FUNCTION 3: GET PLAYER'S MOVE
# --------------------------------------------------

def player_move():

    while True:

        user_input = input(
            Fore.GREEN +
            "\nChoose your move (Rock/Paper/Scissors): " +
            Style.RESET_ALL
        )

        normalized_input = normalize_input(user_input)

        if normalized_input in moves:

            return normalized_input

        else:

            print(
                Fore.RED +
                "Invalid choice! Please choose Rock, Paper, or Scissors."
            )


# --------------------------------------------------
# FUNCTION 4: AI SELECTS ITS MOVE
# --------------------------------------------------

def ai_move():

    # Use frequency analysis after collecting enough moves
    if len(player_history) >= 3:

        move_frequency = Counter(player_history)

        most_common_move = move_frequency.most_common(1)[0][0]

        counter_moves = {
            "rock": "paper",
            "paper": "scissors",
            "scissors": "rock"
        }

        return counter_moves[most_common_move]

    # Initially, AI selects a random move
    return random.choice(moves)


# --------------------------------------------------
# FUNCTION 5: DETERMINE THE WINNER
# --------------------------------------------------

def determine_winner(player, ai):

    if player == ai:

        return "Tie"

    elif (
        (player == "rock" and ai == "scissors") or
        (player == "scissors" and ai == "paper") or
        (player == "paper" and ai == "rock")
    ):

        return "Player"

    else:

        return "AI"


# --------------------------------------------------
# FUNCTION 6: DISPLAY ROUND RESULT
# --------------------------------------------------

def display_result(player, ai, result, player_name):

    print(Fore.CYAN + "\n========== ROUND RESULT ==========")

    print(Fore.GREEN + f"{player_name} selected: {player.title()}")

    print(Fore.YELLOW + f"AI selected: {ai.title()}")

    if result == "Player":

        print(
            Fore.GREEN +
            f"Congratulations {player_name}! You won this round!"
        )

    elif result == "AI":

        print(
            Fore.RED +
            "AI wins this round! Better luck next time."
        )

    else:

        print(
            Fore.YELLOW +
            "It's a tie! Both selected the same move."
        )

    print(Fore.CYAN + "=================================")


# --------------------------------------------------
# FUNCTION 7: UPDATE SCORE
# --------------------------------------------------

def update_score(result):

    global player_score, ai_score, tie_score

    if result == "Player":

        player_score += 1

    elif result == "AI":

        ai_score += 1

    else:

        tie_score += 1


# --------------------------------------------------
# FUNCTION 8: DISPLAY SCOREBOARD
# --------------------------------------------------

def display_score():

    print(Fore.CYAN + "\n========== SCOREBOARD ==========")

    print(Fore.GREEN + f"Player: {player_score}")

    print(Fore.RED + f"AI: {ai_score}")

    print(Fore.YELLOW + f"Ties: {tie_score}")

    print(Fore.CYAN + "================================")


# --------------------------------------------------
# FUNCTION 9: DISPLAY FINAL RESULT
# --------------------------------------------------

def final_result(player_name):

    print(Fore.CYAN + "\n========== FINAL GAME REPORT ==========")

    print(f"Player Name: {player_name}")

    print(Fore.GREEN + f"Player Wins: {player_score}")

    print(Fore.RED + f"AI Wins: {ai_score}")

    print(Fore.YELLOW + f"Tied Rounds: {tie_score}")

    if player_score > ai_score:

        print(
            Fore.GREEN +
            f"\nCongratulations {player_name}! You are the overall winner!"
        )

    elif ai_score > player_score:

        print(
            Fore.RED +
            "\nAI is the overall winner! Better luck next time."
        )

    else:

        print(
            Fore.YELLOW +
            "\nThe game ended in an overall tie!"
        )

    print(Fore.CYAN + "======================================")


# --------------------------------------------------
# FUNCTION 10: MAIN GAME FUNCTION
# --------------------------------------------------

def play_game():

    global player_score, ai_score, tie_score

    print(
        Fore.CYAN +
        "\n======================================"
    )

    print(
        Fore.YELLOW +
        "       ROCK, PAPER, SCISSORS"
    )

    print(
        Fore.CYAN +
        "======================================"
    )

    print(
        Fore.GREEN +
        "\nWelcome to the Rock, Paper, Scissors Game!"
    )

    # Ask for player's name
    player_name = input(
        Fore.MAGENTA + "\nWhat is your name? "
    ).strip()

    if not player_name:

        player_name = "Player"

    print(
        Fore.CYAN +
        f"\nNice to meet you, {player_name}!"
    )

    print(
        Fore.YELLOW +
        "\nYou will be playing against the AI."
    )

    # Display game rules
    show_rules()

    print(
        Fore.CYAN +
        "\nLet's start the game!"
    )

    # Main game loop
    while True:

        # Get player's move
        player = player_move()

        # Get AI's move
        ai = ai_move()

        # Store player's move in history
        player_history.append(player)

        # Determine winner
        result = determine_winner(player, ai)

        # Display round result
        display_result(player, ai, result, player_name)

        # Update score
        update_score(result)

        # Display current scoreboard
        display_score()

        # Ask whether the player wants another round
        play_again = input(
            Fore.MAGENTA +
            "\nDo you want to play another round? (yes/no): "
        ).strip().lower()

        if play_again != "yes":

            print(
                Fore.YELLOW +
                f"\nThank you for playing, {player_name}!"
            )

            print(
                Fore.CYAN +
                "Hope you had fun. Goodbye!"
            )

            break

    # Display final game report
    final_result(player_name)


# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    play_game()
