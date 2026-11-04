import colorama
from colorama import Fore, Style
from textblob import TextBlob
colorama.init()
print(Fore.YELLOW + "Welcome to Sentiment Spy!" + Style.RESET_ALL)
user_name=input(f"{Fore.CYAN}What's your name?{Style.RESET_ALL}\n").strip()
if not user_name:
    user_name="Mystery Agent"
conversation_history=[]
print(f"{Fore.GREEN}Nice to meet you, {user_name}! Let's chat and I'll analyze your sentiments.{Style.RESET_ALL}")
print(f"{Fore.MAGENTA}Type 'exit' to end the conversation.{Style.RESET_ALL}")
print(f"Type {Fore.YELLOW} 'reset', {Fore.CYAN} 'history' to end the conversation.{Style.RESET_ALL}")
while True:
    user_input=input(f"{Fore.CYAN}You: {Style.RESET_ALL}").strip()

    if not user_input:
        print(f"{Fore.RED}Please enter a message to analyze.{Style.RESET_ALL}")
        continue

    if user_input.lower() == "exit":
        print(f"{Fore.YELLOW}Goodbye, {user_name}! It was nice chatting with you!{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.YELLOW}Conversation history has been reset.{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if conversation_history:
            print(f"{Fore.BLUE}Conversation History:{Style.RESET_ALL}")
            for idx, (text,polarity,sentiment_type) in enumerate(conversation_history, start=1):
                print(f"{idx}. {sentiment_type} (Polarity: {polarity:.2f}): {text}")
                polarity = TextBlob(user_input).sentiment.polarity
        else:
            print(f"{Fore.BLUE}No conversation history available.{Style.RESET_ALL}")
        continue
    conversation_history.append((user_input, polarity, sentiment))
    analysis=TextBlob(user_input)
    sentiment_score=analysis.sentiment.polarity
    if sentiment_score > 0.25:
        sentiment="positive"
        print(f"{Fore.GREEN}Sentiment Analysis: Your message has a positive sentiment!{Style.RESET_ALL}")
    elif sentiment_score < -0.25:
        sentiment="negative"
        print(f"{Fore.RED}Sentiment Analysis: Your message has a negative sentiment.{Style.RESET_ALL}")
    else:
        sentiment="neutral"
        print(f"{Fore.BLUE}Sentiment Analysis: Your message is neutral.{Style.RESET_ALL}")