# Task 3: Similarity Meter

## Goal

Build a small similarity meter using `sentence-transformers`.

The program compares words by meaning, not by spelling. It uses a multilingual
AI model to calculate how close two words are on a semantic map.

## Requirements

The program should:

- load the `paraphrase-multilingual-MiniLM-L12-v2` model;
- define `calculate_similarity(word1, word2)`;
- ask the user for two words and print their similarity score;
- explain whether the words are close, somewhat connected, or far apart.

## Files

- `solution.py` - solution for the task.

## Materials

Related course files can be placed in:

```text
materials/task_03/
```

## Dependency

Install the required package before running:

```powershell
pip install sentence-transformers
```
