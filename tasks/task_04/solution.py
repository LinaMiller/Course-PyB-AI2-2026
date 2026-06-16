try:
    from sentence_transformers import SentenceTransformer, util
except ImportError:
    SentenceTransformer = None
    util = None


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
model = None


def load_model():
    if SentenceTransformer is None:
        return None

    try:
        return SentenceTransformer(MODEL_NAME, local_files_only=True)
    except Exception:
        pass

    try:
        return SentenceTransformer(MODEL_NAME)
    except Exception:
        return None


def calculate_similarity(word1, word2):
    meaning_pos1 = model.encode([word1])
    meaning_pos2 = model.encode([word2])
    score_distance = util.cos_sim(meaning_pos1, meaning_pos2).item()
    return score_distance


def print_similarity_meter(score):
    percent = round(score * 100)
    filled_count = round(percent / 5)
    empty_count = 20 - filled_count
    meter = "#" * filled_count + "-" * empty_count
    print(f"Similarity meter: [{meter}] {percent}%")


def play_semantel():
    secret_word = "наука"
    guess = ""
    attempts = 0

    print("-" * 50)
    print("Welcome to Semantel!")
    print("Try to guess the secret word.")
    print("After each guess, you will see how close it is in meaning.")
    print("-" * 50)

    while guess != secret_word:
        attempts += 1
        guess = input(f"Enter guess number {attempts}: ")

        score = calculate_similarity(guess, secret_word)
        print_similarity_meter(score)

    print(f"Well done! You found the secret word '{secret_word}' in {attempts} attempts!")


def main():
    global model

    model = load_model()

    if model is None:
        print("sentence-transformers is not installed in this Python environment.")
        print("Or the semantic model could not be loaded.")
        print("Install the library with: pip install sentence-transformers")
        print("On the first run, PyCharm may need internet access to download the model.")
        return

    play_semantel()


if __name__ == "__main__":
    main()
