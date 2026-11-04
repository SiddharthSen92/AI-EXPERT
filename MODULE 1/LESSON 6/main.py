import time, pandas as pd
from textblob import TextBlob
from colorama import Fore, init
init(autoreset=True)
try:
    df=pd.read_csv("imdb_top_1000_movies.csv")
except FileNotFoundError:
    print(Fore.RED + "Error: The file 'imdb_top_1000_movies.csv' was not found." + Fore.RESET)
    raise SystemExit
genres = sorted({g.strip() for xs in df['Genre'].dropna().str.split(', ') for g in xs})
def recommend(genre=None, mood=None, rating=None, n=5):
    filtered_df = df.copy()
    if genre:
        filtered_df = filtered_df[filtered_df['Genre'].str.contains(genre, case=False, na=False)]
    if rating is not None:
        filtered_df = filtered_df[filtered_df['Rating'] >= rating]
    if filtered_df.empty:
        print(Fore.YELLOW + "No movies found matching the criteria." + Fore.RESET)
        return pd.DataFrame(columns=['Title', 'Genre', 'Mood', 'Rating'])
    filtered_df, need_nonneg, out = filtered_df.sample(frac=1).reset_index(drop=True),bool(mood),[]
    for _, row in filtered_df.iterrows():
        ov = row.get('Description', '')
        if pd.isna(ov):
            continue
        pol = TextBlob(ov).sentiment.polarity
        if (not need_nonneg) or pol >= 0:
            out.append((row['Title'], pol))
            if len(out) == n:
                break
    return out if out else "No movies found matching the criteria."

def senti(p):
    if p > 0:
        return "Positive"
    elif p < 0:
        return "Negative"
    else:
        return "Neutral"

def show(recs, name):
    print(Fore.CYAN + f"\n{name}, here are your movie recommendations:\n" + Fore.RESET)
    for i, (t.p) in enumerate(recs, 1):
        print(Fore.GREEN + f"{i}. {t} (Sentiment: {senti(p):<8}, Polarity: {p:.2f})" + Fore.RESET)

def dots():
    for _ in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)
    print()

def handle_ai():
    mood=input(Fore.CYAN + "Enter your mood (Describe your mood): " + Fore.RESET).strip()
    print(Fore.MAGENTA + "Analyzing your mood" + Fore.RESET, end="")
    dots()
    mp = TextBlob(mood).sentiment.polarity
    if mp > 0:
        print(Fore.GREEN + "Your mood is positive! Here are some uplifting movie recommendations." + Fore.RESET)
        recs = recommend(mood="positive", n=5)
    elif mp < 0:
        print(Fore.RED + "Your mood is negative. Here are some movies that might help you feel better." + Fore.RESET)
        recs = recommend(mood="negative", n=5)
    else:
        print(Fore.YELLOW + "Your mood is neutral. Here are some general movie recommendations." + Fore.RESET)
        recs = recommend(mood="neutral", n=5)

if __name__ == "__main__":
    print(Fore.YELLOW + "Welcome to the Movie Recommendation System!" + Fore.RESET)
    name = input(Fore.CYAN + "Please enter your name: " + Fore.RESET).strip()
    while True:
        print(Fore.CYAN + "\nMenu:" + Fore.RESET)
        print(Fore.GREEN + "1. Get movie recommendations based on mood" + Fore.RESET)
        print(Fore.GREEN + "2. Get movie recommendations based on genre and rating" + Fore.RESET)
        print(Fore.GREEN + "3. Exit" + Fore.RESET)
        choice = input(Fore.CYAN + "Enter your choice (1/2/3): " + Fore.RESET).strip()
        if choice == '1':
            handle_ai()
        elif choice == '2':
            genre = input(Fore.CYAN + f"Enter a genre from the following list {genres}: " + Fore.RESET).strip()
            rating_input = input(Fore.CYAN + "Enter minimum IMDB rating (0-10): " + Fore.RESET).strip()
            try:
                rating = float(rating_input)
                if not (0 <= rating <= 10):
                    raise ValueError
            except ValueError:
                print(Fore.RED + "Invalid rating! Please enter a number between 0 and 10." + Fore.RESET)
                continue
            recs = recommend(genre=genre, rating=rating, n=5)
            show(recs, name)
        elif choice == '3':
            print(Fore.YELLOW + f"Goodbye, {name}! Enjoy your movies!" + Fore.RESET)
            break
        else:
            print(Fore.RED + "Invalid choice! Please select 1, 2, or 3." + Fore.RESET)