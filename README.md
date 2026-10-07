# Human Emotion Detection

### NLP-based emotion classification using TF-IDF and a class-balanced Linear SVM

A machine learning application that analyzes natural-language text and classifies it into one of six human emotion categories:

**Sadness · Joy · Love · Anger · Fear · Surprise**

The project implements an end-to-end NLP pipeline, from text preprocessing and TF-IDF feature engineering to model comparison, hyperparameter tuning, unseen test evaluation, and real-time prediction through a Streamlit web application.

## 🚀 Key Results

| Metric          | Final Test Score |
| --------------- | ---------------: |
| **Accuracy**    |       **89.25%** |
| **Macro F1**    |       **85.11%** |
| **Weighted F1** |       **89.40%** |

**Final model:** Linear SVM
**C:** 0.5
**Class weighting:** Balanced
**TF-IDF features:** 32,992
**Total samples:** 19,999

---

## 💡 Project Highlights

* Built an end-to-end **NLP classification pipeline**
* Engineered **32,992 TF-IDF features** using unigrams and bigrams
* Compared Logistic Regression, Linear SVM, and Multinomial Naive Bayes
* Performed systematic hyperparameter tuning
* Addressed class imbalance using `class_weight="balanced"`
* Evaluated the final model on a completely unseen test set
* Built a reusable prediction pipeline
* Developed a polished **Streamlit web application**
* Performed per-class error and confusion-matrix analysis

---

## 🧠 How It Works

The system follows this pipeline:

```text
User Text
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Class-Balanced Linear SVM
   ↓
Predicted Emotion
   ↓
Human-Friendly Result
```

For example:

```text
Input:
"I am feeling very happy today"

Output:
Joy
```

---

## 🎯 Emotion Classes

| Label | Emotion      | Description                                      |
| ----: | ------------ | ------------------------------------------------ |
|     0 | **Sadness**  | A sense of heaviness, loss, or low mood          |
|     1 | **Joy**      | A feeling of happiness, warmth, or excitement    |
|     2 | **Love**     | A feeling of affection, warmth, or connection    |
|     3 | **Anger**    | A strong feeling of frustration or displeasure   |
|     4 | **Fear**     | A feeling of worry, uncertainty, or apprehension |
|     5 | **Surprise** | A reaction to something unexpected or sudden     |

---

# 🔬 Model Development

## Dataset

The project uses **19,999 labeled text samples** divided into training, validation, and test sets.

| Split      |    Samples |
| ---------- | ---------: |
| Training   |     15,999 |
| Validation |      2,000 |
| Test       |      2,000 |
| **Total**  | **19,999** |

The dataset is imbalanced, with some emotions represented significantly more frequently than others.

### Training Distribution

| Emotion  | Samples |
| -------- | ------: |
| Joy      |   5,361 |
| Sadness  |   4,666 |
| Anger    |   2,159 |
| Fear     |   1,937 |
| Love     |   1,304 |
| Surprise |     572 |

This imbalance was considered during model development and addressed in the final Linear SVM using balanced class weights.

---

## 🧮 TF-IDF Feature Engineering

The text was transformed into numerical features using:

```python
TfidfVectorizer(
    max_df=0.95,
    min_df=2,
    ngram_range=(1, 2),
    sublinear_tf=True
)
```

The resulting representation contains:

```text
32,992 features
```

Both unigrams and bigrams were used to capture individual words as well as short phrases.

For example, a sentence can generate features such as:

```text
feel
humiliated
didnt
didnt feel
feel humiliated
```

The resulting TF-IDF matrices are stored as sparse CSR matrices, making them efficient for high-dimensional text classification.

---

# 🤖 Model Comparison

Three machine learning algorithms were evaluated on the validation set.

| Model                   |   Accuracy |   Macro F1 | Weighted F1 |
| ----------------------- | ---------: | ---------: | ----------: |
| Logistic Regression     |     87.55% |     84.88% |      87.65% |
| **Linear SVM**          | **90.30%** | **87.35%** |  **90.32%** |
| Multinomial Naive Bayes |     62.95% |     35.27% |      54.01% |

Linear SVM produced the strongest overall validation performance and was selected for further tuning.

---

# ⚙️ Hyperparameter Tuning

The Linear SVM was evaluated using different values of `C` and class-weight strategies.

The selected configuration was:

```text
C = 0.5
class_weight = balanced
```

### Best Validation Performance

```text
Accuracy:     90.35%
Macro F1:     87.73%
Weighted F1:  90.41%
```

The use of balanced class weights improved the model's ability to account for less-represented emotion categories.

---

# 📊 Final Test Evaluation

After model selection and hyperparameter tuning, the final model was evaluated on the held-out test set.

### Overall Performance

| Metric          |      Score |
| --------------- | ---------: |
| **Accuracy**    | **89.25%** |
| **Macro F1**    | **85.11%** |
| **Weighted F1** | **89.40%** |

### Per-Class Performance

| Emotion  | Precision | Recall | F1 Score |
| -------- | --------: | -----: | -------: |
| Sadness  |      0.94 |   0.92 | **0.93** |
| Joy      |      0.93 |   0.90 | **0.92** |
| Love     |      0.72 |   0.85 | **0.78** |
| Anger    |      0.88 |   0.90 | **0.89** |
| Fear     |      0.88 |   0.85 | **0.87** |
| Surprise |      0.67 |   0.79 | **0.72** |

The model performs particularly well on **sadness, joy, and anger**.

The lower performance on **surprise** reflects both its smaller representation in the dataset and the natural linguistic overlap between emotions such as surprise and fear.

---

# 🔍 Error Analysis

The final test-set recall shows where the model performs most reliably:

| Emotion  |     Recall |
| -------- | ---------: |
| Sadness  | **91.74%** |
| Joy      | **90.22%** |
| Anger    | **90.18%** |
| Love     |     84.91% |
| Fear     |     84.82% |
| Surprise |     78.79% |

Common areas of semantic overlap include:

```text
Love ↔ Joy
Fear ↔ Surprise
Sadness ↔ Anger
```

This demonstrates an important characteristic of emotion classification: emotional categories are not always linguistically independent.

---

# 🖥️ Streamlit Application

The trained model is integrated into a Streamlit web application.

The interface allows users to:

* Enter natural-language text
* Submit the text for classification
* View the detected emotion
* Read a human-friendly description
* Explore the six supported emotions
* View model performance
* Learn about responsible use

The interface was designed with a clean, dark, human-centered aesthetic so that the prediction remains the primary focus.

---

# 🗂️ Project Structure

```text
text-emotion-detection/
│
├── app/
│   └── app.py
│
├── data/
│   └── ...
│
├── models/
│   ├── final_svm_model.pkl
│   ├── tfidf_vectorizer.pkl
│   └── final_evaluation_results.csv
│
├── src/
│   ├── predict.py
│   └── ...
│
├── notebooks/
│   └── ...
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# 🚀 Installation

## Prerequisites

* Python 3.10+
* Git

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/text-emotion-detection.git
cd text-emotion-detection
```

Replace `YOUR_USERNAME` with your GitHub username.

## 2. Create a virtual environment

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Run the application

```bash
streamlit run app/app.py
```

The application will open through the local Streamlit server.

---

# 🧪 Python Prediction

The trained model can also be used directly through the prediction pipeline.

```python
from src.predict import predict_emotion

text = "I am feeling wonderful today"

emotion = predict_emotion(text)

print(emotion)
```

Example output:

```text
joy
```

The prediction pipeline uses the saved TF-IDF vectorizer and trained Linear SVM model, allowing predictions without retraining.

---

# 💾 Saved Model Artifacts

The trained components are included in the repository:

```text
models/
├── final_svm_model.pkl
├── tfidf_vectorizer.pkl
└── final_evaluation_results.csv
```

### `final_svm_model.pkl`

The final class-balanced Linear SVM used for emotion prediction.

### `tfidf_vectorizer.pkl`

The fitted TF-IDF vectorizer containing the learned vocabulary and feature configuration.

### `final_evaluation_results.csv`

The final test-set evaluation results.

---

# 🛠️ Technologies Used

### Programming

* Python

### Machine Learning

* scikit-learn
* Linear SVM
* Logistic Regression
* Multinomial Naive Bayes

### NLP

* TF-IDF
* Unigrams
* Bigrams
* Sparse matrix representation

### Data Processing

* pandas
* NumPy
* SciPy

### Application

* Streamlit

---

# 🧠 Why Linear SVM?

The final TF-IDF representation contains **32,992 dimensions** and is highly sparse.

Linear SVM is well suited to this type of high-dimensional text representation because it can efficiently learn linear decision boundaries without requiring the computational cost of nonlinear kernels.

The experimental comparison also showed that Linear SVM provided the strongest validation performance among the evaluated baseline models.

---

# ⚠️ Limitations

This project is a **text classification system**, not a psychological assessment system.

The model cannot reliably determine a person's actual emotional or psychological state.

Important limitations include:

* Text may express multiple emotions simultaneously
* Emotional meaning can depend strongly on context
* Sarcasm and irony are difficult to interpret
* Very short text may contain insufficient information
* Similar emotions can share vocabulary
* Model performance depends on the characteristics of the training dataset
* The model may make incorrect predictions on unfamiliar language patterns

Therefore, predictions should be interpreted as **machine-learning classifications of text**, not definitive statements about a person's feelings.

---

# 🔐 Responsible Use

This project is intended for:

* Educational purposes
* NLP experimentation
* Machine learning demonstrations
* Research and prototyping

It should not be used for:

* Medical diagnosis
* Psychological diagnosis
* Mental-health assessment
* High-stakes decisions about individuals

Human emotion is complex and contextual. A classifier can identify patterns in language, but it cannot directly observe a person's internal emotional state.

---

# 🔮 Future Improvements

The current TF-IDF + Linear SVM approach provides a strong and efficient baseline.

Potential improvements include:

### Contextual NLP

Evaluate transformer-based approaches such as:

* BERT
* RoBERTa
* DistilBERT

### Data Improvement

* Increase minority-class samples
* Apply targeted data augmentation
* Explore additional emotion datasets
* Improve handling of ambiguous examples

### Explainability

Investigate:

* SHAP
* LIME
* Feature-level explanations

### Confidence Estimation

The current model uses Linear SVM decision scores rather than calibrated probabilities.

Future versions could investigate probability calibration to provide more interpretable prediction confidence.

---

# 🏆 Final Takeaway

This project demonstrates that a carefully engineered traditional NLP pipeline can achieve strong performance on multi-class emotion classification without requiring a large neural network.

The final system combines:

```text
TF-IDF
   +
Class-Balanced Linear SVM
   +
Streamlit
```

to achieve:

```text
89.25% Test Accuracy
85.11% Macro F1
89.40% Weighted F1
```

More importantly, the project covers the complete machine-learning workflow:

**data preparation → feature engineering → model comparison → hyperparameter tuning → evaluation → error analysis → deployment**

---

## 👨‍💻 Author

**Sinan PS**

Machine Learning · Natural Language Processing · Python

---

> **Note:** Emotion classification is inherently subjective. A model prediction describes a pattern identified in the supplied text; it does not establish the actual emotional or psychological state of the person who wrote it.
