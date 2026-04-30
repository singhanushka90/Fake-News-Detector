<!-- 🔥 HERO BANNER -->

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:6366f1&height=220&section=header&text=Fake%20News%20Detection%20System&fontSize=38&fontColor=ffffff&animation=fadeIn" />
</p>

<h1 align="center">📰 Fake News Detection System</h1>
<h3 align="center">🚀 AI-Powered News Authenticity Classifier</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-0f172a?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/NLP-TF--IDF-6366f1?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Model-Naive%20Bayes-8b5cf6?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge"/>
</p>

---

## 🧠 Overview

This project is a **Machine Learning + NLP system** that classifies news articles as:

* 🟢 **Real News**
* 🔴 **Fake News**

🎯 **Goal:** Detect misinformation automatically using trained ML models.
🔍 **Use Case:** Helps reduce the spread of fake news online.

---

## ⚙️ System Pipeline

```
Data Ingestion (Fake.csv / True.csv)
        ↓
Text Cleaning (Lowercase + Regex)
        ↓
TF-IDF Vectorization
        ↓
Naive Bayes Model Training
        ↓
Prediction (Real / Fake)
```

---

## ✨ Key Features

| Feature            | Description                    |
| ------------------ | ------------------------------ |
| 🧠 NLP-Based       | TF-IDF for text representation |
| ⚡ Fast             | Lightweight Naive Bayes model  |
| 📊 Clean Pipeline  | End-to-end ML workflow         |
| 🔍 Text Processing | Noise removal & normalization  |
| 📈 High Accuracy   | ~90%+                          |
| 🧪 Custom Testing  | Test real-world news           |

---

## ⚙️ Tech Stack

* 🐍 Python
* 📊 Pandas, NumPy
* 🔠 Scikit-learn
* 📉 TF-IDF Vectorizer
* 🤖 Naive Bayes

---

## 🤖 Model

| Model                   | Type          | Status  |
| ----------------------- | ------------- | ------- |
| Multinomial Naive Bayes | Probabilistic | ✅ Final |

💡 Optimized for **speed + efficiency** in text classification.

---

## 📊 Performance

* ✅ Accuracy: **~90%+**
* ⚡ Fast inference
* 💻 Low computational cost

---

## 📂 Dataset

| File     | Description |
| -------- | ----------- |
| Fake.csv | Fake news   |
| True.csv | Real news   |

🎯 **Target:**

* `1 → Real`
* `0 → Fake`

---

## 📁 Project Structure

```
Fake_News_Detection/
│
├── 📓 True_f.ipynb        # Training notebook
├── 📄 nlp.py              # Preprocessing pipeline
├── 🤖 nb_model.pkl        # Trained model
├── 🔤 tfidf.pkl           # Vectorizer
├── 📊 Fake.csv            # Fake dataset
├── 📊 True.csv            # Real dataset
└── 📖 README.md
```

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

## 🚀 Future Improvements

* 🌐 Web App (Streamlit)
* 📊 Visualization Dashboard
* 🧠 Explainable AI (word importance)
* 🔗 News URL detection

---

## ⚡ Final Insight

<p align="center">
<b>“Fighting misinformation with intelligent systems.”</b>
</p>

---

<p align="center">
⭐ If you found this useful, don't forget to star the repo!
</p>
