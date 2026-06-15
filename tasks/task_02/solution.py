try:
    from sentence_transformers import SentenceTransformer
except ImportError:
    SentenceTransformer = None


MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"
tokenizer = None


def load_tokenizer():
    if SentenceTransformer is None:
        return None

    try:
        model = SentenceTransformer(MODEL_NAME)
        return model.tokenizer
    except Exception:
        return None


def print_sentence_info(sentence):
    print(f"Sentence: {sentence}")
    print(f"Length including spaces: {len(sentence)}")
    print(f"Number of spaces: {sentence.count(' ')}")


def tokens_sentence(sentence):
    tokens = tokenizer.tokenize(sentence)
    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    print(f"Tokens: {tokens}")
    print(f"Token IDs: {token_ids}")
    print(f"Number of tokens: {len(tokens)}")

    return tokens, token_ids


def check_sentence(sentence):
    print("-" * 50)
    print_sentence_info(sentence)
    tokens_sentence(sentence)


def main():
    global tokenizer

    if tokenizer is None:
        tokenizer = load_tokenizer()

    if tokenizer is None:
        print("sentence-transformers is not installed in this Python environment.")
        print("Or the tokenizer model could not be loaded.")
        print("Install the library with: pip install sentence-transformers")
        print("On the first run, PyCharm may need internet access to download the model.")
        return

    sentence = "I love learning Python"

    print("Tokenizer")
    check_sentence(sentence)

    print("-" * 50)
    print("Playground")

    my_name = "Lina"
    hebrew_sentence = "אני אוהבת ללמוד פייתון"
    english_sentence = "I love learning Python"
    five_letter_word = "queue"

    check_sentence(my_name)
    check_sentence(hebrew_sentence)
    check_sentence(english_sentence)
    check_sentence(five_letter_word)
    check_sentence("apple")
    check_sentence("APPLE")


if __name__ == "__main__":
    main()
