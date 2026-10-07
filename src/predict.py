"""
Emotion Detection Prediction Module

This module loads the trained TF-IDF vectorizer and final Linear SVM model
and provides a function for predicting the emotion of new text.

Model:
    Linear SVM
    C = 0.5
    class_weight = "balanced"

Emotion labels:
    0 -> sadness
    1 -> joy
    2 -> love
    3 -> anger
    4 -> fear
    5 -> surprise
"""



import os
import joblib


# --------------------------------------------------
# Paths
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VECTORIZER_PATH = os.path.join(
    BASE_DIR,
    "models",
    "tfidf_vectorizer.pkl"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "final_svm_model.pkl"
)


# --------------------------------------------------
# Emotion label mapping
# --------------------------------------------------

EMOTION_LABELS = {
    0: "sadness",
    1: "joy",
    2: "love",
    3: "anger",
    4: "fear",
    5: "surprise"
}


# --------------------------------------------------
# Load trained artifacts
# --------------------------------------------------

vectorizer = joblib.load(VECTORIZER_PATH)
model = joblib.load(MODEL_PATH)


# --------------------------------------------------
# Prediction function
# --------------------------------------------------

def predict_emotion(text):
    """
    Predict the emotion of a single text.

    Parameters
    ----------
    text : str
        Input text to classify.

    Returns
    -------
    str
        Predicted emotion label.
    """

    if not isinstance(text, str):
        raise TypeError("Input text must be a string.")

    if not text.strip():
        raise ValueError("Input text cannot be empty.")

    text_vectorized = vectorizer.transform([text])

    prediction = model.predict(text_vectorized)[0]

    emotion = EMOTION_LABELS[int(prediction)]

    return emotion