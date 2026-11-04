
import time
import random
import pandas as pd

from textblob import TextBlob
from colorama import Fore, init
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Initialize Colorama
init(autoreset=True)


# --------------------------------------------------
# 1. LOAD MOVIE DATASET
# --------------------------------------------------

try:
    df = pd.read_csv("imdb_top_1000_movies.csv")

except FileNotFoundError:
    print(
        Fore.RED +
        "Error: The file 'imdb_top_1000_movies.csv' was not found."
    )
    raise SystemExit

# Check required dataset columns
required_columns = [
    "Title",
    "Genre",
    "Description",
    "Rating"
]

if not all(column in df.columns for column in required_columns):
    print(Fore.RED + "Error: Required columns are missing from the dataset.")
    raise SystemExit

# Clean missing values
df["Genre"] = df["Genre"].fillna("")
df["Description"] = df["Description"].fillna("")
df["Title"] = df["Title"].fillna("Unknown Title")
df["Rating"] = pd.to_numeric(
    df["Rating"], errors="coerce"
)

df = df.dropna(subset=["Rating"]).reset_index(drop=True)

# Extract all available genres
genres = sorted({
    genre.strip()
    for genre_list in df["Genre"]
    for genre in genre_list.split(",")
    if genre.strip()
})


# --------------------------------------------------
# 2. PREPARE MOVIE FEATURES FOR AI RECOMMENDATION
# --------------------------------------------------

# Combine genre and description to create movie features
movie_features = (
    df["Genre"] + " " + df["Description"]
)

# Convert text into numerical TF-IDF vectors
vectorizer = TfidfVectorizer(
    stop_words="english",
    ngram_range=(1, 2)
)

movie_matrix = vectorizer.fit_transform(movie_features)


# --------------------------------------------------
# 3. NORMALIZE USER INPUT
# --------------------------------------------------

def normalize_input(user_input):

    return user_input.strip().lower()


# --------------------------------------------------
# 4. DISPLAY LOADING ANIMATION
# --------------------------------------------------

def dots():

    for i in range(3):

        print(".", end="", flush=True)
        time.sleep(0.5)

    print()


# --------------------------------------------------
# 5. ANALYZE SENTIMENT
# --------------------------------------------------

def senti(polarity):

    if polarity > 0:
        return "Positive", "😊"

    elif polarity < 0:
        return "Negative", "😞"

    else:
        return "Neutral", "😐"


# --------------------------------------------------
# 6. GET USER'S PREFERRED GENRE
# --------------------------------------------------

def get_genre():

    while True:

        print(
            Fore.CYAN +
            "\nAvailable genres:"
        )

        print(", ".join(genres))

        genre = input(
            Fore.GREEN +
            "\nEnter your preferred genre (or type 'Any'): "
        ).strip()

        if normalize_input(genre) == "any":
            return None

        matching_genre = next(
            (
                g for g in genres
                if g.lower() == genre.lower()
            ),
            None
        )

        if matching_genre:
            return matching_genre

        print(
            Fore.RED +
            "Invalid genre! Please select a genre from the list."
        )


# --------------------------------------------------
# 7. GET OPTIONAL IMDB RATING
# --------------------------------------------------

def get_rating():

    while True:

        rating_input = input(
            Fore.GREEN +
            "\nEnter minimum IMDB rating (0-10) "
            "or press Enter to skip: "
        ).strip()

        if rating_input == "":
            return None

        try:

            rating = float(rating_input)

            if 0 <= rating <= 10:
                return rating

            else:
                print(
                    Fore.RED +
                    "Rating must be between 0 and 10."
                )

        except ValueError:

            print(
                Fore.RED +
                "Invalid rating! Please enter a number between 0 and 10."
            )


# --------------------------------------------------
# 8. AI-BASED MOVIE RECOMMENDATION
# --------------------------------------------------

def ai_recommendation(genre, mood, rating):

    filtered_df = df.copy()

    # Filter by selected genre
    if genre:

        filtered_df = filtered_df[
            filtered_df["Genre"].apply(
                lambda x: genre.lower() in [
                    g.strip().lower() for g in x.split(",")
                ]
            )
        ]

    # Filter by minimum IMDB rating
    if rating is not None:

        filtered_df = filtered_df[
            filtered_df["IMDB_Rating"] >= rating
        ]

    if filtered_df.empty:

        print(
            Fore.YELLOW +
            "\nNo movies found matching your genre and rating preferences."
        )

        return None

    # Create a search query using genre and mood
    search_query = ""

    if genre:
        search_query += genre + " "

    search_query += mood

    # Convert user preferences into a TF-IDF vector
    query_vector = vectorizer.transform([search_query])

    # Calculate cosine similarity
    similarity_scores = cosine_similarity(
        query_vector,
        movie_matrix
    ).flatten()

    # Get the indices of filtered movies
    candidate_indices = filtered_df.index.tolist()

    # Rank movies based on similarity scores
    ranked_indices = sorted(
        candidate_indices,
        key=lambda i: similarity_scores[i],
        reverse=True
    )

    # If there is no textual similarity, select randomly
    if similarity_scores[ranked_indices[0]] == 0:

        print(
            Fore.YELLOW +
            "No close text match found. Selecting from your filtered preferences."
        )

        selected_index = random.choice(candidate_indices)

    else:

        selected_index = ranked_indices[0]

    return df.iloc[selected_index]


# --------------------------------------------------
# 9. RANDOM MOVIE RECOMMENDATION
# --------------------------------------------------

def random_recommendation():

    print(
        Fore.MAGENTA +
        "\nFinding a random movie for you"
    )

    dots()

    movie = df.sample(n=1).iloc[0]

    return movie


# --------------------------------------------------
# 10. DISPLAY MOVIE DETAILS
# --------------------------------------------------

def show_movie(movie, name):

    if movie is None:
        return

    title = movie["Title"]
    genre = movie["Genre"]
    description = movie["Description"]
    rating = movie["Rating"]

    # Analyze sentiment of movie description
    polarity = TextBlob(description).sentiment.polarity

    sentiment, emoji = senti(polarity)

    print(
        Fore.CYAN +
        "\n=============================================="
    )

    print(
        Fore.YELLOW +
        f"       MOVIE RECOMMENDATION FOR {name.upper()}"
    )

    print(
        Fore.CYAN +
        "=============================================="
    )

    print(
        Fore.GREEN +
        f"\n🎬 Movie Title: {title}"
    )

    print(
        Fore.MAGENTA +
        f"\n🎭 Genre: {genre}"
    )

    print(
        Fore.WHITE +
        f"\n📖 Description: {description}"
    )

    print(
        Fore.YELLOW +
        f"\n⭐ IMDB Rating: {rating}/10"
    )

    print(
        Fore.CYAN +
        "\n========== SENTIMENT ANALYSIS =========="
    )

    print(
        f"{emoji} Sentiment: {sentiment}"
    )

    print(
        f"Polarity Score: {polarity:.2f}"
    )

    print(
        Fore.CYAN +
        "========================================"
    )


# --------------------------------------------------
# 11. HANDLE AI-BASED RECOMMENDATION
# --------------------------------------------------

def handle_ai(name):

    print(
        Fore.CYAN +
        "\n========== AI MOVIE RECOMMENDATION =========="
    )

    # Ask for preferred genre
    genre = get_genre()

    # Ask for user's mood
    mood = input(
        Fore.GREEN +
        "\nDescribe your current mood: "
    ).strip()

    while not mood:

        print(Fore.RED + "Please describe your mood.")

        mood = input(
            Fore.GREEN + "Describe your current mood: "
        ).strip()

    # Analyze user's mood
    mood_polarity = TextBlob(mood).sentiment.polarity

    mood_sentiment, emoji = senti(mood_polarity)

    print(
        Fore.MAGENTA +
        "\nAnalyzing your mood and preferences"
    )

    dots()

    print(
        f"{emoji} Your mood appears to be {mood_sentiment.lower()}."
    )

    # Ask for optional IMDB rating
    rating = get_rating()

    print(
        Fore.MAGENTA +
        "\nSearching for the best movie recommendation"
    )

    dots()

    # Generate AI-based recommendation
    movie = ai_recommendation(
        genre=genre,
        mood=mood,
        rating=rating
    )

    # Display movie details
    show_movie(movie, name)


# --------------------------------------------------
# 12. HANDLE RANDOM RECOMMENDATION
# --------------------------------------------------

def handle_random(name):

    movie = random_recommendation()

    show_movie(movie, name)


# --------------------------------------------------
# 13. MAIN PROGRAM
# --------------------------------------------------

if __name__ == "__main__":

    print(
        Fore.YELLOW +
        "\n🎬 WELCOME TO THE MOVIE RECOMMENDATION SYSTEM! 🎬"
    )

    # Ask for user's name
    name = input(
        Fore.CYAN +
        "\nPlease enter your name: "
    ).strip()

    if not name:
        name = "Movie Lover"

    print(
        Fore.GREEN +
        f"\nHello, {name}! Welcome to your personal movie assistant."
    )

    print(
        Fore.CYAN +
        "I can recommend movies based on your preferences "
        "or surprise you with a random movie!"
    )

    # Main interaction loop
    while True:

        print(
            Fore.CYAN +
            "\n========== MAIN MENU =========="
        )

        print(
            Fore.GREEN +
            "1. AI-based Movie Recommendation"
        )

        print(
            Fore.GREEN +
            "2. Random Movie Recommendation"
        )

        print(
            Fore.GREEN +
            "3. Exit"
        )

        print(
            Fore.CYAN +
            "================================"
        )

        choice = input(
            Fore.YELLOW +
            "\nEnter your choice (1/2/3): "
        ).strip()

        if choice == "1":

            handle_ai(name)

        elif choice == "2":

            handle_random(name)

        elif choice == "3":

            print(
                Fore.YELLOW +
                f"\nGoodbye, {name}! Enjoy your movies!"
            )

            break

        else:

            print(
                Fore.RED +
                "\nInvalid choice! Please select 1, 2, or 3."
            )

            continue

        # Ask whether the user wants another recommendation
        play_again = input(
            Fore.CYAN +
            "\nWould you like another recommendation? (yes/no): "
        ).strip().lower()

        if play_again != "yes":

            print(
                Fore.YELLOW +
                f"\nThank you for using the Movie Recommendation System, {name}!"
            )

            print(
                Fore.CYAN +
                "Happy watching! Goodbye!"
            )

            break
