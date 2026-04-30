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
