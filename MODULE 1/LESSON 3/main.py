import re, random
from colorama import Fore, init
init(autoreset=True)
destinations={
    "beach":["Maldives","Bora Bora","Maui","Bahamas","Seychelles"],
    "mountains":["Swiss Alps","Rocky Mountains","Himalayas","Andes","Dolomites"],
    "city":["New York","Tokyo","Paris","London","Dubai"],
}
jokes={
    "Why don't oysters donate to charity? Because they are shellfish!","What do you call a snowman on the beach? A puddle!",
    
    "Why did the mountain break up with the hill? It found someone more uplifting!",

    "What do you call a mountain that tells jokes? A hill-arious!",

    "Why did the city planner go broke? Because he lost his sense of direction!","Why did the skyscraper go to therapy? It had too many high expectations!",
}
def normalize_input(user_input):
    user_input=user_input.lower()
    user_input=re.sub(r"\s+"," ",user_input)#remove one or more whitespaces with a single space
    return user_input
def recommend():
    print(Fore.CYAN+"What type of destination are you interested in? (beach/mountains/city)")
    user_input=input(Fore.GREEN+"You: ")
    normalized_input=normalize_input(user_input)
    if normalized_input in destinations:
        destination=random.choice(destinations[normalized_input])
        print(Fore.YELLOW+f"Based on your preference, I recommend visiting {destination}!")
        print(Fore.MAGENTA + "Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").strip().lower()
        if answer == "yes":
            print(Fore.GREEN + "Great! I'm glad you like the recommendation!")
        elif answer == "no":
            print(Fore.RED + "No worries! Let's try again.")
            recommend()
    else:
        print(Fore.RED+"Sorry, I don't have recommendations for that type of destination.")

    show_help()

def show_help():
    print(Fore.CYAN+"You can ask me to recommend a destination or tell you a joke.")
    print(Fore.CYAN+"Type 'recommend' for a destination recommendation.")
    print(Fore.CYAN+"Type 'joke' for a random joke.")
    print(Fore.CYAN+"Type 'packing' for a packing tips.")
    print(Fore.CYAN+"Type 'exit' to end the conversation.")

def packing_tips():
    print(Fore.CYAN + "Where are you traveling to?")
    user_input = input(Fore.GREEN + "You: ")
    print(Fore.CYAN + "How many days will you be traveling?")
    days_input = input(Fore.GREEN + "You: ")
    print(Fore.YELLOW + f"Packing tips for your trip to {user_input} for {days_input} days:")
    print(Fore.MAGENTA + "- Make a packing list to ensure you don't forget anything.")
    print(Fore.MAGENTA + "- Pack versatile clothing that can be mixed and matched." )
    print(Fore.MAGENTA + "- Don't forget essentials like chargers, and medications.")
    print(Fore.MAGENTA + "- Check the weather forecast for your destination and pack accordingly.")

def tell_joke():
    joke=random.choice(list(jokes))
    print(Fore.YELLOW+joke)

def chat():
    print(Fore.CYAN+"Hello! I am your Travel Assistant Bot. How can I help you today?")
    name=input(Fore.GREEN+"Your name?")
    print(Fore.CYAN+f"Nice to meet you, {name}! You can ask me for travel recommendations, jokes, or packing tips.")
    show_help()
    while True:
        user_input=input(Fore.GREEN+f"{name}: ")
        normalized_input=normalize_input(user_input)
        if "recommend" in normalized_input or "suggest" in normalized_input:
            recommend()
        elif "joke" in normalized_input or "funny" in normalized_input:
            tell_joke()
        elif "packing" in normalized_input or "tips" in normalized_input:
            packing_tips()
        elif "help" in normalized_input:
            show_help()
        elif normalized_input=="exit":
            print(Fore.YELLOW+"Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED+"Sorry, I didn't understand that. Please try again.")
            show_help()

if __name__=="__main__":
    chat()