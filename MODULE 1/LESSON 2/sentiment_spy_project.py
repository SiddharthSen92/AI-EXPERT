
import colorama
from colorama import Fore, Style
from textblob import TextBlob
import time
import sys

# Initialize Colorama
colorama.init(autoreset=True)

# Global variables to store conversation data
conversation_history = []

sentiment_counts = {
    "Positive": 0,
    "Negative": 0,
    "Neutral": 0
}

user_name = ""


# --------------------------------------------------
# FUNCTION 1: Display Processing Animation
# --------------------------------------------------

def show_processing_animation():
    print(Fore.CYAN + "\n🕵️ Agent Spy is analyzing your message", end="")

    for i in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)

    print("\n")


# --------------------------------------------------
# FUNCTION 2: Analyze Sentiment
# --------------------------------------------------

def analyze_sentiment(text):

    polarity = TextBlob(text).sentiment.polarity

    if polarity > 0.25:
        sentiment = "Positive"
        color = Fore.GREEN
        emoji = "😊"

    elif polarity < -0.25:
        sentiment = "Negative"
        color = Fore.RED
        emoji = "😞"

    else:
        sentiment = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Determine sentiment strength
    if abs(polarity) >= 0.75:
        strength = "Strong"

    elif abs(polarity) >= 0.25:
        strength = "Moderate"

    else:
        strength = "Mild"

    # Update sentiment counter
    sentiment_counts[sentiment] += 1

    # Store conversation details
    conversation_history.append(
        (text, polarity, sentiment, strength)
    )

    print(
        color + f"{emoji} {sentiment} Sentiment Detected!"
    )

    print(
        color + f"Polarity Score: {polarity:.2f}"
    )

    print(
        color + f"Sentiment Strength: {strength}"
    )

    return polarity, sentiment


# --------------------------------------------------
# FUNCTION 3: Display Sentiment Summary
# --------------------------------------------------

def display_summary():

    total = len(conversation_history)

    print(Fore.CYAN + "\n========== SENTIMENT SUMMARY ==========")

    print(f"Total Messages Analyzed: {total}")

    print(
        Fore.GREEN +
        f"Positive Messages: {sentiment_counts['Positive']}"
    )

    print(
        Fore.RED +
        f"Negative Messages: {sentiment_counts['Negative']}"
    )

    print(
        Fore.YELLOW +
        f"Neutral Messages: {sentiment_counts['Neutral']}"
    )

    print(Fore.CYAN + "=======================================\n")


# --------------------------------------------------
# FUNCTION 4: Execute Commands
# --------------------------------------------------

def execute_command(command):

    command = command.lower().strip()

    if command == "summary":

        display_summary()

    elif command == "reset":

        conversation_history.clear()

        for sentiment in sentiment_counts:
            sentiment_counts[sentiment] = 0

        print(
            Fore.CYAN +
            "All conversation history and statistics have been reset!"
        )

    elif command == "history":

        if not conversation_history:

            print(
                Fore.YELLOW +
                "No conversation history available."
            )

        else:

            print(
                Fore.CYAN +
                "\n========== CONVERSATION HISTORY =========="
            )

            for index, (text, polarity, sentiment, strength) in enumerate(
                conversation_history, start=1
            ):

                if sentiment == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"

                elif sentiment == "Negative":
                    color = Fore.RED
                    emoji = "😞"

                else:
                    color = Fore.YELLOW
                    emoji = "😐"

                print(
                    color +
                    f"{index}. {emoji} {text}"
                )

                print(
                    f"   Polarity: {polarity:.2f} | "
                    f"Sentiment: {sentiment} | "
                    f"Strength: {strength}"
                )

            print(
                Fore.CYAN +
                "===========================================\n"
            )

    elif command == "help":

        print(Fore.CYAN + "\nAvailable Commands:")

        print("1. summary - Display sentiment statistics")

        print("2. reset   - Clear conversation history and counters")

        print("3. history - Display previous messages")

        print("4. help    - Display available commands")

        print("5. exit    - End chatbot and generate final report\n")

    else:

        print(
            Fore.RED +
            "Unknown command. Type 'help' to see available commands."
        )


# --------------------------------------------------
# FUNCTION 5: Validate User Name
# --------------------------------------------------

def get_valid_name():

    while True:

        name = input(
            Fore.MAGENTA +
            "Please enter your name (letters only): "
        ).strip()

        if name.isalpha():

            return name

        else:

            print(
                Fore.RED +
                "Invalid name! Please use alphabetic characters only."
            )


# --------------------------------------------------
# FUNCTION 6: Generate and Save Final Report
# --------------------------------------------------

def generate_final_report():

    total = len(conversation_history)

    report = []

    report.append("SENTIMENT SPY - FINAL MISSION REPORT")
    report.append("=" * 45)

    report.append(f"Agent Name: {user_name}")
    report.append(f"Total Messages Analyzed: {total}")

    report.append("")

    report.append(
        f"Positive Messages: {sentiment_counts['Positive']}"
    )

    report.append(
        f"Negative Messages: {sentiment_counts['Negative']}"
    )

    report.append(
        f"Neutral Messages: {sentiment_counts['Neutral']}"
    )

    report.append("")
    report.append("CONVERSATION DETAILS")
    report.append("-" * 45)

    for index, (text, polarity, sentiment, strength) in enumerate(
        conversation_history, start=1
    ):

        report.append(
            f"{index}. Message: {text}"
        )

        report.append(
            f"   Polarity: {polarity:.2f}"
        )

        report.append(
            f"   Sentiment: {sentiment}"
        )

        report.append(
            f"   Strength: {strength}"
        )

        report.append("")

    report.append("=" * 45)
    report.append("Mission Completed Successfully!")

    # Display report
    print(Fore.CYAN + "\n" + "\n".join(report))

    # Save report to text file
    file_name = f"{user_name}_sentiment_analysis.txt"

    with open(file_name, "w", encoding="utf-8") as file:

        file.write("\n".join(report))

    print(
        Fore.GREEN +
        f"\nFinal report successfully saved as: {file_name}"
    )


# --------------------------------------------------
# MAIN CHATBOT PROGRAM
# --------------------------------------------------

print(
    Fore.CYAN +
    "\n🐍 WELCOME TO SENTIMENT SPY! 🐍"
)

print(
    Fore.YELLOW +
    "Your mission is to investigate the emotions behind text."
)

user_name = get_valid_name()

print(
    Fore.GREEN +
    f"\nHello, Agent {user_name}! Your mission starts now."
)

print(
    Fore.CYAN +
    "\nEnter any sentence to analyze its sentiment."
)

print(
    "Type 'help' to see commands or 'exit' to finish your mission.\n"
)


# Main chatbot loop

while True:

    user_input = input(
        Fore.GREEN + ">> "
    ).strip()

    if not user_input:

        print(
            Fore.RED +
            "Please enter a sentence or a valid command."
        )

        continue

    command = user_input.lower()

    # Exit command
    if command == "exit":

        print(
            Fore.BLUE +
            f"\nMission ending. Farewell, Agent {user_name}!"
        )

        generate_final_report()

        break

    # Handle chatbot commands
    elif command in ["summary", "reset", "history", "help"]:

        execute_command(command)

    # Analyze user sentence
    else:

        show_processing_animation()

        analyze_sentiment(user_input)


# End of program
colorama.deinit()
