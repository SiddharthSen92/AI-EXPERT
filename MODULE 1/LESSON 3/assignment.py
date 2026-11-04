
import re
import random
from colorama import Fore, Style, init
from datetime import datetime

# Initialize Colorama
init(autoreset=True)


# --------------------------------------------------
# DATA STORAGE
# --------------------------------------------------

destinations = {
    "beach": ["Maldives", "Bora Bora", "Maui", "Bahamas", "Seychelles"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Dolomites"],
    "city": ["New York", "Tokyo", "Paris", "London", "Dubai"]
}

jokes = [
    "Why don't oysters donate to charity? Because they are shellfish!",
    "What do you call a snowman on the beach? A puddle!",
    "Why did the mountain break up with the hill? It found someone more uplifting!",
    "What do you call a mountain that tells jokes? A hill-arious!",
    "Why did the city planner go broke? Because he lost his sense of direction!",
    "Why did the skyscraper go to therapy? It had too many high expectations!"
]

# Simulated weather information
weather_data = {
    "paris": "Sunny, 22°C",
    "london": "Cloudy, 17°C",
    "tokyo": "Light Rain, 19°C",
    "dubai": "Hot and Sunny, 35°C",
    "maldives": "Partly Cloudy, 29°C",
    "new york": "Clear Sky, 21°C",
    "swiss alps": "Cold and Snowy, 5°C",
    "guwahati": "Partly Cloudy, 26°C"
}

# Simulated local time information
city_times = {
    "london": "10:30 AM",
    "paris": "11:30 AM",
    "tokyo": "06:30 PM",
    "new york": "05:30 AM",
    "dubai": "02:30 PM",
    "guwahati": "03:00 PM"
}

# Sample travel news
travel_news = [
    "New international flight routes are opening this month!",
    "Several popular tourist destinations are introducing eco-tourism initiatives.",
    "Airlines are offering discounts on selected international routes.",
    "Adventure tourism is becoming increasingly popular among young travellers."
]

# Conversation memory
conversation_history = []


# --------------------------------------------------
# FUNCTION 1: NORMALIZE USER INPUT
# --------------------------------------------------

def normalize_input(user_input):

    user_input = user_input.lower().strip()

    # Replace multiple spaces with a single space
    user_input = re.sub(r"\s+", " ", user_input)

    return user_input


# --------------------------------------------------
# FUNCTION 2: CHECK KEYWORDS
# --------------------------------------------------

def contains_keyword(user_input, keywords):

    for keyword in keywords:

        pattern = r"\b" + re.escape(keyword) + r"\b"

        if re.search(pattern, user_input):
            return True

    return False


# --------------------------------------------------
# FUNCTION 3: DISPLAY HELP
# --------------------------------------------------

def show_help():

    print(Fore.CYAN + "\n========== TRAVEL ASSISTANT HELP ==========")

    print(Fore.GREEN + "1. recommend - Get a travel destination recommendation")
    print(Fore.GREEN + "2. joke      - Listen to a travel joke")
    print(Fore.GREEN + "3. packing   - Get packing tips")
    print(Fore.GREEN + "4. weather   - Check simulated weather information")
    print(Fore.GREEN + "5. time      - Check local time in a city")
    print(Fore.GREEN + "6. news      - Get travel news updates")
    print(Fore.GREEN + "7. budget    - Calculate your travel budget")
    print(Fore.GREEN + "8. memory    - View previous conversations")
    print(Fore.GREEN + "9. save      - Save conversation history")
    print(Fore.GREEN + "10. help     - Display available commands")
    print(Fore.GREEN + "11. exit     - End the conversation")

    print(Fore.CYAN + "===========================================\n")


# --------------------------------------------------
# FUNCTION 4: RECOMMEND DESTINATION
# --------------------------------------------------

def recommend():

    print(Fore.CYAN + "\nWhat type of destination are you interested in?")
    print("Options: beach, mountains, city")

    user_input = input(Fore.GREEN + "You: ")

    normalized_input = normalize_input(user_input)

    if normalized_input in destinations:

        destination = random.choice(destinations[normalized_input])

        print(
            Fore.YELLOW +
            f"\nBased on your preference, I recommend visiting {destination}!"
        )

        answer = input(
            Fore.MAGENTA + "Do you like this recommendation? (yes/no): "
        ).strip().lower()

        if answer == "yes":

            print(
                Fore.GREEN +
                "Great! I'm glad you like the recommendation!"
            )

        elif answer == "no":

            print(
                Fore.RED +
                "No worries! Let me suggest another destination."
            )

            recommend()

        else:

            print(Fore.YELLOW + "I will remember your recommendation preference!")

    else:

        print(
            Fore.RED +
            "Sorry, I don't have recommendations for that destination type."
        )


# --------------------------------------------------
# FUNCTION 5: TELL A RANDOM JOKE
# --------------------------------------------------

def tell_joke():

    joke = random.choice(jokes)

    print(Fore.YELLOW + "\n" + joke)


# --------------------------------------------------
# FUNCTION 6: PACKING TIPS
# --------------------------------------------------

def packing_tips():

    destination = input(
        Fore.GREEN + "\nWhere are you traveling to? "
    )

    days_input = input(
        Fore.GREEN + "How many days will you be traveling? "
    )

    if not days_input.isdigit() or int(days_input) <= 0:

        print(Fore.RED + "Please enter a valid number of days.")

        return

    days = int(days_input)

    print(
        Fore.YELLOW +
        f"\nPacking tips for your trip to {destination} for {days} days:"
    )

    print(Fore.MAGENTA + "- Make a packing list.")
    print(Fore.MAGENTA + "- Pack versatile clothing.")
    print(Fore.MAGENTA + "- Carry chargers and necessary medications.")
    print(Fore.MAGENTA + "- Check the weather forecast.")
    print(Fore.MAGENTA + "- Carry enough clothing for your trip.")


# --------------------------------------------------
# FUNCTION 7: WEATHER INFORMATION
# --------------------------------------------------

def check_weather():

    city = input(
        Fore.GREEN + "\nEnter the city to check its weather: "
    ).strip().lower()

    if city in weather_data:

        print(
            Fore.YELLOW +
            f"\nWeather in {city.title()}: {weather_data[city]}"
        )

        print(
            Fore.CYAN +
            "(Note: This is simulated weather information.)"
        )

    else:

        print(
            Fore.RED +
            "Sorry, weather information is unavailable for this city."
        )


# --------------------------------------------------
# FUNCTION 8: LOCAL TIME
# --------------------------------------------------

def check_local_time():

    city = input(
        Fore.GREEN + "\nEnter the city: "
    ).strip().lower()

    if city in city_times:

        print(
            Fore.YELLOW +
            f"\nLocal time in {city.title()}: {city_times[city]}"
        )

        print(
            Fore.CYAN +
            "(Note: This is sample time information.)"
        )

    else:

        print(
            Fore.RED +
            "Sorry, local time information is unavailable for this city."
        )


# --------------------------------------------------
# FUNCTION 9: TRAVEL NEWS
# --------------------------------------------------

def show_travel_news():

    print(Fore.CYAN + "\n========== LATEST TRAVEL UPDATES ==========")

    for index, news in enumerate(travel_news, start=1):

        print(Fore.YELLOW + f"{index}. {news}")

    print(Fore.CYAN + "\nThese are sample news updates, not live news.")


# --------------------------------------------------
# FUNCTION 10: TRAVEL BUDGET CALCULATOR
# --------------------------------------------------

def calculate_budget():

    try:

        days = int(input(Fore.GREEN + "\nNumber of travel days: "))

        if days <= 0:
            print(Fore.RED + "Please enter a positive number of days.")
            return

        accommodation = float(
            input(Fore.GREEN + "Accommodation cost per day (₹): ")
        )

        food = float(
            input(Fore.GREEN + "Food cost per day (₹): ")
        )

        transport = float(
            input(Fore.GREEN + "Total transport cost (₹): ")
        )

        if min(accommodation, food, transport) < 0:
            print(Fore.RED + "Costs cannot be negative.")
            return

        total_accommodation = accommodation * days
        total_food = food * days

        total_budget = (
            total_accommodation +
            total_food +
            transport
        )

        print(Fore.CYAN + "\n========== TRAVEL BUDGET ==========")

        print(f"Accommodation: ₹{total_accommodation:.2f}")
        print(f"Food: ₹{total_food:.2f}")
        print(f"Transport: ₹{transport:.2f}")

        print(Fore.GREEN + f"Total Estimated Budget: ₹{total_budget:.2f}")

        print(Fore.CYAN + "===================================\n")

    except ValueError:

        print(
            Fore.RED +
            "Invalid input! Please enter numbers only."
        )


# --------------------------------------------------
# FUNCTION 11: CONVERSATION MEMORY
# --------------------------------------------------

def show_memory():

    if not conversation_history:

        print(Fore.YELLOW + "\nNo previous conversations available.")

    else:

        print(Fore.CYAN + "\n========== CONVERSATION MEMORY ==========")

        for index, message in enumerate(conversation_history, start=1):

            print(Fore.YELLOW + f"{index}. {message}")

        print(Fore.CYAN + "=========================================")


# --------------------------------------------------
# FUNCTION 12: SAVE CONVERSATION TO FILE
# --------------------------------------------------

def save_conversation():

    try:

        with open(
            "travel_conversation.txt",
            "w",
            encoding="utf-8"
        ) as file:

            file.write("TRAVEL ASSISTANT CONVERSATION HISTORY\n")
            file.write("=" * 45 + "\n\n")

            for message in conversation_history:

                file.write(message + "\n")

        print(
            Fore.GREEN +
            "\nConversation history saved successfully!"
        )

    except OSError:

        print(Fore.RED + "Unable to save conversation history.")


# --------------------------------------------------
# FUNCTION 13: MAIN CHATBOT
# --------------------------------------------------

def chat():

    print(
        Fore.CYAN +
        "\n🌍 WELCOME TO YOUR TRAVEL ASSISTANT BOT! 🌍"
    )

    name = input(
        Fore.GREEN + "\nWhat is your name? "
    ).strip()

    if not name:
        name = "Traveller"

    print(
        Fore.YELLOW +
        f"\nNice to meet you, {name}!"
    )

    print(
        Fore.CYAN +
        "I can help you plan your next adventure!"
    )

    show_help()

    # Keyword lists for intent matching
    recommend_keywords = ["recommend", "suggest", "destination"]
    joke_keywords = ["joke", "funny", "laugh"]
    packing_keywords = ["packing", "pack", "tips"]
    weather_keywords = ["weather", "temperature", "forecast"]
    time_keywords = ["time", "clock"]
    news_keywords = ["news", "updates", "travel news"]
    budget_keywords = ["budget", "cost", "expenses"]
    memory_keywords = ["memory", "history", "previous"]
    save_keywords = ["save", "download"]

    while True:

        user_input = input(
            Fore.GREEN + f"\n{name}: "
        )

        normalized_input = normalize_input(user_input)

        if not normalized_input:
            print(Fore.RED + "Please enter something.")
            continue

        # Store user input in memory
        conversation_history.append(
            f"{name}: {user_input}"
        )

        # Check for exit command
        if normalized_input == "exit":

            print(
                Fore.YELLOW +
                "\nGoodbye! Have a wonderful journey. Safe travels!"
            )

            break

        # Match user intent using keyword lists

        elif contains_keyword(normalized_input, recommend_keywords):

            recommend()

        elif contains_keyword(normalized_input, joke_keywords):

            tell_joke()

        elif contains_keyword(normalized_input, packing_keywords):

            packing_tips()

        elif contains_keyword(normalized_input, weather_keywords):

            check_weather()

        elif contains_keyword(normalized_input, time_keywords):

            check_local_time()

        elif contains_keyword(normalized_input, news_keywords):

            show_travel_news()

        elif contains_keyword(normalized_input, budget_keywords):

            calculate_budget()

        elif contains_keyword(normalized_input, memory_keywords):

            show_memory()

        elif contains_keyword(normalized_input, save_keywords):

            save_conversation()

        elif contains_keyword(normalized_input, ["help", "commands"]):

            show_help()

        else:

            print(
                Fore.RED +
                "Sorry, I didn't understand that. Please try again."
            )

            show_help()



if __name__ == "__main__":

    chat()
