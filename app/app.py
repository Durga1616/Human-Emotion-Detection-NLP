import os
import sys

import streamlit as st


# ============================================================
# PROJECT PATH
# ============================================================

PROJECT_ROOT = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# MODEL
# ============================================================

from src.predict import predict_emotion


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Human Emotion Detection",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# EMOTION DATA
# ============================================================

EMOTION_INFO = {
    "sadness": {
        "icon": "◒",
        "label": "Sadness",
        "short": "A sense of heaviness, loss, or low mood.",
        "description": (
            "The language contains patterns commonly associated "
            "with sadness, disappointment, loss, or emotional heaviness."
        ),
        "gradient": "linear-gradient(135deg, #172554 0%, #3730a3 100%)",
        "glow": "rgba(79, 70, 229, 0.35)",
    },
    "joy": {
        "icon": "☀",
        "label": "Joy",
        "short": "A feeling of happiness, warmth, or excitement.",
        "description": (
            "The language contains patterns commonly associated "
            "with happiness, positivity, excitement, or enjoyment."
        ),
        "gradient": "linear-gradient(135deg, #78350f 0%, #d97706 100%)",
        "glow": "rgba(245, 158, 11, 0.38)",
    },
    "love": {
        "icon": "♡",
        "label": "Love",
        "short": "A feeling of affection, warmth, or connection.",
        "description": (
            "The language contains patterns commonly associated "
            "with affection, care, attachment, warmth, or connection."
        ),
        "gradient": "linear-gradient(135deg, #701a3b 0%, #db2777 100%)",
        "glow": "rgba(236, 72, 153, 0.38)",
    },
    "anger": {
        "icon": "△",
        "label": "Anger",
        "short": "A strong feeling of frustration or displeasure.",
        "description": (
            "The language contains patterns commonly associated "
            "with frustration, irritation, hostility, or displeasure."
        ),
        "gradient": "linear-gradient(135deg, #7f1d1d 0%, #dc2626 100%)",
        "glow": "rgba(239, 68, 68, 0.38)",
    },
    "fear": {
        "icon": "◐",
        "label": "Fear",
        "short": "A feeling of worry, uncertainty, or apprehension.",
        "description": (
            "The language contains patterns commonly associated "
            "with worry, uncertainty, threat, or apprehension."
        ),
        "gradient": "linear-gradient(135deg, #312e81 0%, #7c3aed 100%)",
        "glow": "rgba(124, 58, 237, 0.38)",
    },
    "surprise": {
        "icon": "✦",
        "label": "Surprise",
        "short": "A reaction to something unexpected or sudden.",
        "description": (
            "The language contains patterns commonly associated "
            "with unexpected events, astonishment, shock, or sudden reactions."
        ),
        "gradient": "linear-gradient(135deg, #164e63 0%, #0891b2 100%)",
        "glow": "rgba(6, 182, 212, 0.38)",
    },
}


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ---------- Global ---------- */

    .stApp {
        background:
            radial-gradient(
                circle at 8% 5%,
                rgba(99, 102, 241, 0.13),
                transparent 28%
            ),
            radial-gradient(
                circle at 92% 12%,
                rgba(236, 72, 153, 0.09),
                transparent 26%
            ),
            radial-gradient(
                circle at 50% 100%,
                rgba(124, 58, 237, 0.07),
                transparent 35%
            ),
            #08090d;
    }

    .main .block-container {
        max-width: 1120px;
        padding-top: 3.5rem;
        padding-bottom: 5rem;
    }

    /* ---------- Hero ---------- */

    .eyebrow {
        text-align: center;
        color: #a5b4fc;
        font-size: 0.72rem;
        font-weight: 800;
        letter-spacing: 0.28em;
        text-transform: uppercase;
        margin-bottom: 1.1rem;
    }

    .hero-title {
        text-align: center;
        margin: 0;

        font-size: clamp(3.4rem, 8vw, 6.5rem);
        line-height: 0.91;
        font-weight: 850;
        letter-spacing: -0.065em;

        background:
            linear-gradient(
                120deg,
                #ffffff 5%,
                #dbeafe 42%,
                #c4b5fd 67%,
                #fbcfe8 95%
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero-subtitle {
        max-width: 680px;
        margin: 1.6rem auto 3.4rem auto;

        color: #a1a1aa;
        text-align: center;

        font-size: 1.08rem;
        line-height: 1.8;
    }

    /* ---------- Input ---------- */

    .input-heading {
        color: #f4f4f5;
        font-size: 1rem;
        font-weight: 700;
        margin-bottom: 0.6rem;
    }

    div[data-testid="stTextArea"] textarea {
        background: rgba(18, 20, 28, 0.88) !important;
        color: #fafafa !important;

        border: 1px solid rgba(255, 255, 255, 0.09) !important;
        border-radius: 20px !important;

        padding: 1.25rem !important;

        font-size: 1.04rem !important;
        line-height: 1.75 !important;

        transition: all 0.25s ease !important;
    }

    div[data-testid="stTextArea"] textarea:focus {
        border-color: rgba(165, 180, 252, 0.60) !important;

        box-shadow:
            0 0 0 1px rgba(165, 180, 252, 0.16),
            0 20px 60px rgba(79, 70, 229, 0.10) !important;
    }

    /* ---------- Button ---------- */

    .stButton > button {
        width: 100%;
        height: 3.45rem;

        border: none;
        border-radius: 15px;

        color: #ffffff;

        font-size: 1rem;
        font-weight: 750;

        background:
            linear-gradient(
                105deg,
                #6366f1,
                #8b5cf6 52%,
                #ec4899
            );

        box-shadow:
            0 14px 40px rgba(99, 102, 241, 0.23);

        transition:
            transform 0.2s ease,
            box-shadow 0.2s ease;
    }

    .stButton > button:hover {
        transform: translateY(-2px);

        box-shadow:
            0 20px 52px rgba(99, 102, 241, 0.34);
    }

    /* ---------- Result ---------- */

    .result-shell {
        margin-top: 2rem;
        padding: 1px;

        border-radius: 32px;

        background:
            linear-gradient(
                135deg,
                rgba(255,255,255,0.22),
                rgba(255,255,255,0.04)
            );

        box-shadow:
            0 30px 100px var(--emotion-glow);

        animation: resultAppear 0.55s ease;
    }

    .result-card {
        padding: 4.5rem 2rem 4rem 2rem;

        border-radius: 31px;

        text-align: center;
        color: #ffffff;
    }

    @keyframes resultAppear {
        from {
            opacity: 0;
            transform: translateY(18px) scale(0.985);
        }

        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    .result-orb {
        width: 108px;
        height: 108px;

        margin: 0 auto 1.6rem auto;

        display: flex;
        align-items: center;
        justify-content: center;

        border-radius: 50%;

        background: rgba(255,255,255,0.13);

        border:
            1px solid rgba(255,255,255,0.28);

        box-shadow:
            inset 0 1px 15px rgba(255,255,255,0.12),
            0 15px 45px rgba(0,0,0,0.18);
    }

    .result-icon {
        font-size: 3.7rem;
        line-height: 1;
        text-shadow:
            0 0 18px rgba(255,255,255,0.35);
    }

    .result-caption {
        font-size: 0.70rem;
        font-weight: 800;

        letter-spacing: 0.25em;
        text-transform: uppercase;

        opacity: 0.72;
    }

    .result-title {
        margin-top: 0.45rem;

        font-size: clamp(3rem, 7vw, 5rem);
        line-height: 1;

        font-weight: 850;
        letter-spacing: -0.06em;
    }

    .result-description {
        max-width: 620px;

        margin: 1.2rem auto 0 auto;

        font-size: 1.08rem;
        line-height: 1.75;

        opacity: 0.86;
    }

    /* ---------- Sections ---------- */

    .section-title {
        margin-top: 4rem;

        color: #f4f4f5;

        font-size: 1.55rem;
        font-weight: 780;

        letter-spacing: -0.03em;
    }

    .section-description {
        color: #a1a1aa;

        margin-top: -0.45rem;
        margin-bottom: 1.5rem;

        line-height: 1.65;
    }

    /* ---------- Metric cards ---------- */

    .metric-card {
        padding: 1.4rem 1rem;

        min-height: 105px;

        border-radius: 18px;

        background:
            rgba(20, 21, 29, 0.70);

        border:
            1px solid rgba(255,255,255,0.075);

        box-shadow:
            inset 0 1px rgba(255,255,255,0.025);
    }

    .metric-value {
        color: #f4f4f5;

        font-size: 1.65rem;
        font-weight: 800;

        letter-spacing: -0.03em;
    }

    .metric-label {
        margin-top: 0.35rem;

        color: #71717a;

        font-size: 0.70rem;
        font-weight: 700;

        letter-spacing: 0.10em;
        text-transform: uppercase;
    }

    /* ---------- Emotion cards ---------- */

    .emotion-card {
        min-height: 170px;

        padding: 1.5rem;

        border-radius: 20px;

        background:
            rgba(20,21,29,0.68);

        border:
            1px solid rgba(255,255,255,0.07);

        transition:
            transform 0.2s ease,
            border-color 0.2s ease;
    }

    .emotion-icon-small {
        font-size: 2rem;

        text-shadow:
            0 0 18px rgba(255,255,255,0.18);
    }

    .emotion-name {
        margin-top: 0.55rem;

        color: #f4f4f5;

        font-size: 1.08rem;
        font-weight: 750;
    }

    .emotion-description-small {
        margin-top: 0.4rem;

        color: #a1a1aa;

        font-size: 0.84rem;
        line-height: 1.55;
    }

    /* ---------- Footer ---------- */

    .footer {
        margin-top: 4.5rem;
        padding-top: 2rem;

        border-top:
            1px solid rgba(255,255,255,0.07);

        color: #71717a;

        text-align: center;

        font-size: 0.78rem;
        line-height: 1.8;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HERO
# ============================================================

st.html(
    """
    <div class="eyebrow">
        Natural Language · Machine Learning
    </div>

    <h1 class="hero-title">
        Human Emotion<br>
        Detection
    </h1>

    <div class="hero-subtitle">
        Put your thoughts into words. The model analyzes the
        language in your message and identifies the emotion
        it most strongly associates with it.
    </div>
    """
)


# ============================================================
# INPUT
# ============================================================

st.html(
    """
    <div class="input-heading">
        Tell us what is on your mind
    </div>
    """
)

user_text = st.text_area(
    "Your thoughts",

    placeholder=(
        "For example: "
        "I cannot stop smiling because today has been wonderful."
    ),

    height=175,

    max_chars=2000,

    label_visibility="collapsed",
)

st.caption(
    f"{len(user_text)} / 2000 characters"
)


# ============================================================
# PREDICTION
# ============================================================

if st.button(
    "✦  Detect Emotion",
    use_container_width=True,
):

    if not user_text.strip():

        st.warning(
            "Write something first so the model can analyze it."
        )

    else:

        try:

            prediction = predict_emotion(user_text)

            info = EMOTION_INFO[prediction]

            # ------------------------------------------------
            # IMMERSIVE RESULT
            # ------------------------------------------------

            st.html(
                f"""
                <div
                    class="result-shell"

                    style="
                        --emotion-glow: {info["glow"]};
                    "
                >

                    <div
                        class="result-card"

                        style="
                            background: {info["gradient"]};
                        "
                    >

                        <div class="result-orb">

                            <div class="result-icon">
                                {info["icon"]}
                            </div>

                        </div>

                        <div class="result-caption">
                            Detected emotion
                        </div>

                        <div class="result-title">
                            {info["label"]}
                        </div>

                        <div class="result-description">
                            {info["short"]}
                        </div>

                    </div>

                </div>
                """
            )

            # ------------------------------------------------
            # INTERPRETATION
            # ------------------------------------------------

            st.html(
                f"""
                <div class="section-title">
                    What this means
                </div>

                <div class="section-description">
                    {info["description"]}
                </div>
                """
            )

        except Exception as error:

            st.error(
                f"Unable to analyze the text: {error}"
            )


# ============================================================
# MODEL PERFORMANCE
# ============================================================

st.html(
    """
    <div class="section-title">
        The model behind the experience
    </div>

    <div class="section-description">
        The interface is powered by a TF-IDF text representation
        and a Linear Support Vector Machine trained for six
        emotion categories.
    </div>
    """
)


metric1, metric2, metric3, metric4 = st.columns(4)


with metric1:

    st.html(
        """
        <div class="metric-card">

            <div class="metric-value">
                89.25%
            </div>

            <div class="metric-label">
                Test Accuracy
            </div>

        </div>
        """
    )


with metric2:

    st.html(
        """
        <div class="metric-card">

            <div class="metric-value">
                85.11%
            </div>

            <div class="metric-label">
                Macro F1
            </div>

        </div>
        """
    )


with metric3:

    st.html(
        """
        <div class="metric-card">

            <div class="metric-value">
                89.40%
            </div>

            <div class="metric-label">
                Weighted F1
            </div>

        </div>
        """
    )


with metric4:

    st.html(
        """
        <div class="metric-card">

            <div class="metric-value">
                32,992
            </div>

            <div class="metric-label">
                TF-IDF Features
            </div>

        </div>
        """
    )


# ============================================================
# EMOTION CATEGORIES
# ============================================================

st.html(
    """
    <div class="section-title">
        Six emotional dimensions
    </div>

    <div class="section-description">
        The model distinguishes between the following
        six emotion categories.
    </div>
    """
)


emotion_columns = st.columns(3)

for index, (_, info) in enumerate(
    EMOTION_INFO.items()
):

    with emotion_columns[index % 3]:

        st.html(
            f"""
            <div class="emotion-card">

                <div class="emotion-icon-small">
                    {info["icon"]}
                </div>

                <div class="emotion-name">
                    {info["label"]}
                </div>

                <div class="emotion-description-small">
                    {info["short"]}
                </div>

            </div>
            """
        )


# ============================================================
# TECHNICAL DETAILS
# ============================================================

with st.expander("Technical details"):

    st.markdown(
        """
### Natural Language Processing Pipeline

**Text representation**

TF-IDF with unigram and bigram features.

**Vectorizer configuration**

- `min_df = 2`
- `max_df = 0.95`
- `ngram_range = (1, 2)`
- `sublinear_tf = True`
- 32,992 learned features

**Final classifier**

Linear Support Vector Machine

- `C = 0.5`
- `class_weight = balanced`

**Dataset**

- Training samples: 15,999
- Validation samples: 2,000
- Test samples: 2,000
- Emotion classes: 6

**Final test performance**

- Accuracy: **89.25%**
- Macro F1: **85.11%**
- Weighted F1: **89.40%**

The test dataset was kept separate from model selection
and hyperparameter tuning.
"""
    )


# ============================================================
# RESPONSIBLE USE
# ============================================================

with st.expander("Responsible use"):

    st.markdown(
        """
This application performs automated emotion classification
from written language.

The detected emotion represents the category that the
machine-learning model associates most strongly with the
linguistic patterns in the supplied text.

It is **not** a psychological diagnosis, clinical assessment,
or measurement of a person's actual emotional state.

Human emotions are complex and context-dependent, and a text
classifier cannot fully understand a person's feelings.
"""
    )


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="footer">

        Human Emotion Detection · TF-IDF + Linear SVM

        <br>

        A Natural Language Processing project for
        six-class emotion classification.

    </div>
    """
)