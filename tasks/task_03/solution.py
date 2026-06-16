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


def explain_similarity(score):
    if score > 0.5:
        print("These words are close in meaning!")
    elif score >= 0.3:
        print("There is some connection.")
    else:
        print("These words are from completely different worlds.")


def run_similarity_check():
    print("Similarity check")

    first_word = input("Enter the first word: ")
    second_word = input("Enter the second word: ")

    score = calculate_similarity(first_word, second_word)

    print(f"Similarity score: {score}")
    explain_similarity(score)


def main():
    global model

    model = load_model()

    if model is None:
        print("sentence-transformers is not installed in this Python environment.")
        print("Or the semantic model could not be loaded.")
        print("Install the library with: pip install sentence-transformers")
        print("On the first run, PyCharm may need internet access to download the model.")
        return

    run_similarity_check()


if __name__ == "__main__":
    main()
