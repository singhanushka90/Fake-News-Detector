import streamlit as st
import numpy as np
import pickle
import re


model = pickle.load(open('nb_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


def transform(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    return " ".join(text)


st.set_page_config(page_title='Fake News Detector', layout='centered')


st.title("📰 Fake News Detection System")
st.markdown("Detect whether a news article is **Real or Fake** using Machine Learning")


user_input = st.text_area("✍️ Enter News Content")


if st.button("🔍 Analyze News"):
    if user_input.strip() != "":

        
        processed = transform(user_input)
        vector = tfidf.transform([processed])

        
        prediction = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0]

       
        confidence = round(max(prob) * 100, 2)

        st.subheader("📊 Result")

        if prediction == 1:
            st.success(f"✅ Real News ({confidence}% confidence)")
        else:
            st.error(f"🚫 Fake News ({confidence}% confidence)")

       
        st.subheader("🔎 Prediction Details")
        st.write(f"Real News Probability: {round(prob[1]*100,2)}%")
        st.write(f"Fake News Probability: {round(prob[0]*100,2)}%")

        
        with st.expander("🔧 Processed Text"):
            st.write(processed)

    else:
        st.warning("⚠️ Please enter some news text!")



---
# =========================================================
# 🔍 WHY WE USE TF-IDF + NAIVE BAYES MODEL
# =========================================================

# This project is a text classification problem where the goal
# is to classify news as REAL or FAKE based on textual content.

# -------------------------------
# 📌 WHY TF-IDF (Feature Extraction)?
# -------------------------------

# TF-IDF (Term Frequency - Inverse Document Frequency) is used
# to convert textual data into numerical format so that it can
# be understood by machine learning models.

# Why TF-IDF?
# 1. It gives importance to meaningful words in a document.
# 2. It reduces the impact of common words like "the", "is", "and".
# 3. It highlights rare but important words that help in classification.
# 4. It works very well for NLP tasks like spam detection, sentiment analysis, and fake news detection.

# Example:
# If a word appears frequently in one article but not in others,
# TF-IDF assigns it a higher weight → making it useful for prediction.

# -------------------------------
# 📌 WHY NAIVE BAYES (Model)?
# -------------------------------

# Naive Bayes is a probabilistic machine learning algorithm
# based on Bayes' Theorem.

# Why Naive Bayes for this project?
# 1. It performs extremely well on text classification problems.
# 2. It is fast and efficient even with large text data.
# 3. Works well with high-dimensional data (like TF-IDF vectors).
# 4. Requires less training time compared to complex models.
# 5. Provides good accuracy for baseline models (~90%+ in this case).

# -------------------------------
# 📌 WHY MULTINOMIAL NAIVE BAYES?
# -------------------------------

# Multinomial Naive Bayes is specifically designed for:
# → Discrete data like word counts and frequencies

# Since TF-IDF generates frequency-based features,
# Multinomial NB is the best fit.

# -------------------------------
# 📌 WHY NOT COMPLEX MODELS?
# -------------------------------

# We could use Deep Learning models (LSTM, BERT),
# but:

# ❌ They require large datasets
# ❌ More computational power
# ❌ Longer training time

# ✅ Naive Bayes gives a perfect balance of:
#    - Speed
#    - Simplicity
#    - Good performance

# -------------------------------
# 📌 FINAL DECISION
# -------------------------------

# We use TF-IDF + Multinomial Naive Bayes because:
# → It is fast, simple, and highly effective for text classification tasks
# → It provides strong baseline performance for fake news detection
