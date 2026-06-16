# Task 4: Semantel Game

## Goal

Build a semantic guessing game using `sentence-transformers`.

The program chooses a secret word. The user guesses words, and after each guess
the program shows how close the guess is to the secret word by meaning.

## Requirements

The program should:

- load the `paraphrase-multilingual-MiniLM-L12-v2` model;
- define `calculate_similarity(word1, word2)`;
- choose a secret word;
- keep asking for guesses until the user finds the secret word;
- count attempts;
- show the similarity score as a percentage meter.

## Dependency

Install the required package before running:

```powershell
pip install sentence-transformers
```
