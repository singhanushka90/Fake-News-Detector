<!-- 🔥 HERO BANNER --><p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:1e3a8a,100:7c3aed&height=200&section=header&text=Fake%20News%20Detection%20System&fontSize=35&fontColor=ffffff" />
</p><h1 align="center">📰 Fake News Detection System</h1>
<h3 align="center">AI-Powered News Authenticity Classification</h3><p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-1e3a8a?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF-7c3aed?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-Naive%20Bayes-4f46e5?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-06b6d4?style=for-the-badge" />
</p><hr/><!-- 🔥 OVERVIEW --><h2>🧠 Overview</h2><p>
A <b>machine learning-based NLP system</b> designed to classify news articles as <b>Real 🟢</b> or <b>Fake 🔴</b>.
The project focuses on tackling misinformation using text-based analysis.
</p><p>
<b>Goal:</b> Automatically detect whether a given news text is genuine or misleading using trained ML models.
</p>«🔍 <b>Use Case:</b> Helps reduce the spread of fake news and misinformation online.»

<hr/><!-- 🔥 PIPELINE --><h2>⚙️ System Pipeline</h2>┌─────────────────┐
│  Data Ingestion │
│ (Fake.csv/True) │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Text Cleaning   │
│ Lowercase, RegEx│
└────────┬────────┘
         ↓
┌─────────────────┐
│ Feature Extract │
│ TF-IDF Vector   │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Model Training  │
│ Naive Bayes     │
└────────┬────────┘
         ↓
┌─────────────────┐
│ Prediction      │
│ Real / Fake     │
└─────────────────┘

<hr/><!-- 🔥 FEATURES --><h2>✨ Key Features</h2>Feature| Description
🧠 NLP-Based Classification| Uses TF-IDF for text representation
⚡ Fast Prediction| Lightweight Naive Bayes model
📊 Clean Pipeline| End-to-end ML workflow
🔍 Text Processing| Noise removal and normalization
📈 High Accuracy| ~90%+ performance
🧪 Custom Input Testing| Test with real-world news

<hr/><!-- 🔥 TECH --><h2>⚙️ Technical Implementation</h2><ul>
  <li><b>Text preprocessing</b> using RegEx and normalization</li>
  <li><b>TF-IDF vectorization</b> for feature extraction</li>
  <li><b>Multinomial Naive Bayes</b> for classification</li>
  <li>Clean and modular pipeline (<code>nlp.py</code>)</li>
  <li>Model serialization using Pickle</li>
</ul><hr/><!-- 🔥 MODEL --><h2>🤖 Model Used</h2>Model| Type| Status
<b>Multinomial Naive Bayes</b>| Probabilistic| ✅ Final Model

«💡 Optimized for speed and performance on text classification tasks.»

<hr/><!-- 🔥 PERFORMANCE --><h2>📊 Performance</h2><ul>
  <li><b>Accuracy:</b> ~90%+</li>
  <li><b>Efficient on large text data</b></li>
  <li><b>Low computational cost</b></li>
</ul><hr/><!-- 🔥 DATASET --><h2>📂 Dataset</h2><p>Dataset contains real and fake news articles.</p>File| Description
<b>Fake.csv</b>| Fake news dataset
<b>true.csv</b>| Real news dataset

<p><b>Target:</b> Binary Classification → Real (1) / Fake (0)</p><hr/><!-- 🔥 FILES --><h2>📁 Project Files</h2>Fake_News_Detection/
├── 📓 True_f.ipynb
├── 📄 nlp.py
├── 🤖 nb_model.pkl
├── 🔤 tfidf.pkl
├── 📊 Fake.csv
├── 📊 true.csv
└── 📖 README.md

<hr/><!-- 🔥 FINAL --><h2 align="center">⚡ Final Insight</h2><p align="center">
<b>"Fighting misinformation with intelligent systems."</b>
</p><hr/><p align="center">
⭐ Star this repository if you found it useful!
</p>
