import json
from pathlib import Path

try:
    import numpy as np
    import tensorflow as tf
    from PIL import Image
except ImportError:
    np = None
    tf = None
    Image = None


PROJECT_ROOT = Path(__file__).resolve().parents[2]
TASK_MATERIALS = PROJECT_ROOT / "materials" / "task_07"

MODEL_DIR = TASK_MATERIALS / "converted_savedmodel"
SAVED_MODEL_PATH = MODEL_DIR / "model.savedmodel"
TFJS_MODEL_PATH = TASK_MATERIALS / "tm-my-image-model" / "model.json"

LABELS_PATH = MODEL_DIR / "labels.txt"
METADATA_PATH = MODEL_DIR / "metadata.json"

TEST_IMAGES = [
    TASK_MATERIALS / "model-1.png",
    TASK_MATERIALS / "model-2.png",
]

CLASS_NAMES = {
    "Class 1": "chick without cap",
    "Class 2": "chick with cap",
}


def load_labels():
    if LABELS_PATH.exists():
        with open(LABELS_PATH, "r", encoding="utf-8") as file:
            labels = []
            for line in file:
                line = line.strip()
                if line:
                    labels.append(line.split(" ", 1)[1])
            return labels

    if METADATA_PATH.exists():
        with open(METADATA_PATH, "r", encoding="utf-8") as file:
            metadata = json.load(file)
            return metadata["labels"]

    return []


def preprocess_image(image_path, target_size):
    img = Image.open(image_path).convert("RGB")
    img = img.resize(target_size)
    img_array = np.array(img) / 255.0
    return np.expand_dims(img_array, axis=0)


def choose_image():
    print("Choose an image to classify:")
    print("1 - model-1.png")
    print("2 - model-2.png")

    choice = input("Enter 1 or 2: ")

    if choice == "1":
        return TEST_IMAGES[0]
    elif choice == "2":
        return TEST_IMAGES[1]
    else:
        print("Unknown choice. I will use model-1.png.")
        return TEST_IMAGES[0]


def classify_image(model, labels, image_path):
    image = preprocess_image(image_path, (224, 224))
    predictions = model(image)
    predictions_tensor = list(predictions.values())[0]

    predicted_class_idx = tf.argmax(predictions_tensor[0]).numpy()
    predicted_label = labels[predicted_class_idx]
    friendly_label = CLASS_NAMES.get(predicted_label, predicted_label)
    confidence = predictions_tensor[0][predicted_class_idx].numpy()

    print("-" * 50)
    print("Image:", image_path.name)
    print("Predicted category:", friendly_label)
    print("Confidence:", round(confidence, 2))

    if friendly_label == "chick with cap":
        print("Custom message: I understood that this is a chick with a cap.")
    elif friendly_label == "chick without cap":
        print("Custom message: I understood that this is a chick without a cap.")
    else:
        print("Custom message: I understood the category:", friendly_label)


def main():
    print("Task 7: Connect Trained Model To Python")

    if tf is None or np is None or Image is None:
        print("Missing libraries.")
        print("Install them with: pip install tensorflow numpy pillow")
        return

    if not SAVED_MODEL_PATH.exists():
        print("Python SavedModel folder was not found:")
        print(SAVED_MODEL_PATH)

        if TFJS_MODEL_PATH.exists():
            print()
            print("I found a TensorFlow.js export instead:")
            print(TFJS_MODEL_PATH)
            print()
            print("For this Python code, export the model from Teachable Machine")
            print("as TensorFlow/Keras, or convert the TensorFlow.js model first.")

        return

    labels = load_labels()

    if not labels:
        print("No labels were found.")
        return

    model = tf.keras.layers.TFSMLayer(
        str(SAVED_MODEL_PATH),
        call_endpoint="serving_default",
    )

    image_path = choose_image()

    if image_path.exists():
        classify_image(model, labels, image_path)
    else:
        print("Image was not found:", image_path)


if __name__ == "__main__":
    main()
