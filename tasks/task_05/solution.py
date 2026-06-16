paintings = [
    "Starry Night",
    "Mona Lisa",
    "Guernica",
    "The Scream",
    "The Persistence of Memory",
    "Girl with a Pearl Earring",
]

years = [1889, 1519, 1900, 1893, 1931, 1665]

styles = [
    "Post-Impressionism",
    "Renaissance",
    "Cubism",
    "Expressionism",
    "Surrealism",
    "Baroque",
]


def classifier():
    classic = []
    modern = []

    for i in range(len(paintings)):
        if years[i] < 1900:
            classic.append(paintings[i])
        else:
            modern.append(paintings[i])

    print("Classic paintings:", classic)
    print("Modern paintings:", modern)


def classify_by_style():
    renaissance_and_baroque = []
    modern_art_styles = []
    emotional_art = []
    dream_art = []

    for i in range(len(paintings)):
        if styles[i] == "Renaissance" or styles[i] == "Baroque":
            renaissance_and_baroque.append(paintings[i])
        elif styles[i] == "Cubism" or styles[i] == "Post-Impressionism":
            modern_art_styles.append(paintings[i])
        elif styles[i] == "Expressionism":
            emotional_art.append(paintings[i])
        elif styles[i] == "Surrealism":
            dream_art.append(paintings[i])

    print("Renaissance and Baroque:", renaissance_and_baroque)
    print("Modern art styles:", modern_art_styles)
    print("Emotional art:", emotional_art)
    print("Dream art:", dream_art)


def main():
    print("Task 5: Painting Classifier")
    classifier()
    classify_by_style()


if __name__ == "__main__":
    main()
