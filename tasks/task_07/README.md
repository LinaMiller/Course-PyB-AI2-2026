# Task 7: Connect Trained Model To Python

## Goal

Connect a trained Teachable Machine image-classification model to Python.

The program should load the trained model, classify test images, print the
predicted category and confidence level, and add a custom message according to
the category.

The program asks the user which image to classify:

- `1` - `model-1.png`, chick without cap.
- `2` - `model-2.png`, chick with cap.

## Files

- `solution.py` - solution for the task.

## Current Materials

The folder `materials/task_07/` contains:

- `tm-my-image-model/`
- `model-1.png`
- `model-2.png`

The current model folder is a TensorFlow.js export (`model.json` and
`weights.bin`). The Python code from the lesson expects a TensorFlow/Keras
SavedModel export named `model.savedmodel`.

## Dependencies

```powershell
pip install tensorflow numpy pillow
```

## Materials

Related course files are in:

```text
materials/task_07/
```
