import os
import sys

import pandas as pd


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


CSV_FILE = os.path.join(
    os.path.dirname(__file__), "..", "..", "materials", "task_09", "book_ratings.csv"
)


def load_ratings():
    """Read the book ratings table and return readers with their ratings."""
    dataframe = pd.read_csv(CSV_FILE)
    dataframe.set_index("Name", inplace=True)
    return dataframe


def get_new_user_ratings(book_list):
    print("Rate each book: V = like, X = dislike, 0 = I do not know it.")
    user_name = input("Your name: ").strip() or "New reader"
    ratings = []

    for book in book_list:
        while True:
            rating = input(f"{book}: ").strip().upper()
            if rating in ["V", "X", "0"]:
                ratings.append(rating)
                break
            print("Please enter only V, X, or 0.")

    return user_name, ratings


def digital_twin(user_ratings, other_ratings):
    """Count matching opinions about books both readers know."""
    matches = 0

    for user_rating, other_rating in zip(user_ratings, other_ratings):
        if user_rating != "0" and user_rating == other_rating:
            matches += 1

    return matches


def recommendation(user_ratings, twin_ratings):
    """Find a book the twin likes but the new reader does not know."""
    for index, (user_rating, twin_rating) in enumerate(zip(user_ratings, twin_ratings)):
        if user_rating == "0" and twin_rating == "V":
            return index

    return None


def find_digital_twin(dataframe, user_ratings):
    best_name = None
    best_ratings = None
    best_score = -1

    for reader_name, reader_ratings in dataframe.iterrows():
        score = digital_twin(user_ratings, reader_ratings.tolist())

        if score > best_score:
            best_name = reader_name
            best_ratings = reader_ratings.tolist()
            best_score = score

    return best_name, best_ratings, best_score


def main():
    dataframe = load_ratings()
    book_list = dataframe.columns.tolist()

    print("Book recommendation system")
    print("-" * 40)
    user_name, user_ratings = get_new_user_ratings(book_list)

    twin_name, twin_ratings, similarity = find_digital_twin(dataframe, user_ratings)
    recommendation_index = recommendation(user_ratings, twin_ratings)

    print("-" * 40)
    print(f"Digital twin: {twin_name}")
    print(f"Matching ratings: {similarity}")

    if recommendation_index is None:
        print("There is no new book to recommend from this reader.")
    else:
        print(f"Recommendation for {user_name}: {book_list[recommendation_index]}")


if __name__ == "__main__":
    main()
