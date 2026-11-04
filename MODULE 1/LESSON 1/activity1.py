print("Hello! I am an AI Bot. What's your name?")
name=input()
print(f"Nice to meet you, {name}! How are you feeling today?")
mood=input("Good or Bad?").lower()
if mood == "good":
    print("That's great to hear! Keep up the positive vibes!")
elif mood == "bad":
    print("I'm sorry to hear that. Remember, it's okay to have bad days. Take care of yourself!")
else:
    print("I didn't quite understand that. But I hope you have a wonderful day regardless!")

print(f"It was nice chatting with you, {name}. Have a great day!")