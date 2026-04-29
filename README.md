<!-- 🔥 HERO BANNER --><p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=yellow,yellow&height=200&section=header&text=Fake%20News%20Detection%20System&fontSize=35&fontColor=yellow" />
</p><h1 align="center">📰 Fake News Detection System</h1>
<h3 align="center">AI-Powered News Authenticity Classification</h3><p align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NLP-TF--IDF-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-Naive%20Bayes-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p><hr/><!-- 🔥 OVERVIEW --><h2>🧠 Overview</h2><p>
A <b>machine learning-based NLP system</b> designed to classify news articles as <b>Real 🟢</b> or <b>Fake 🔴</b>.
The project focuses on tackling misinformation using text-based analysis.
</p><p>
<b>Goal:</b> AutomATICALLYYYYYYYY detect whether a given news text is genuine or misleading using trained ML models.
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
├── 📓 True_f.ipynb     # Model training notebook
├── 📄 nlp.py           # NLP pipeline script
├── 🤖 nb_model.pkl     # Trained model
├── 🔤 tfidf.pkl        # TF-IDF vectorizer
├── 📊 Fake.csv         # Fake news dataset
├── 📊 true.csv         # Real news dataset
└── 📖 README.md        # Documentation

<hr/><!-- 🔥 INSTALL --><h2>🚀 Installation</h2>git clone https://github.com/yourusername/Fake_News_Detection.git
cd Fake_News_Detection

pip install -r requirements.txt

<hr/><!-- 🔥 USAGE --><h2>💻 Usage</h2>import pickle

model = pickle.load(open("nb_model.pkl", "rb"))
tfidf = pickle.load(open("tfidf.pkl", "rb"))

text = ["Breaking news: Government announces new policy"]

vector = tfidf.transform(text)
prediction = model.predict(vector)

print("Real News" if prediction[0] == 1 else "Fake News")

<hr/><!-- 🔥 HIGHLIGHTS --><h2>📊 Engineering Highlights</h2><ul>
  <li>⚡ Lightweight and fast NLP pipeline</li>
  <li>🧠 Efficient probabilistic model</li>
  <li>📈 High accuracy with minimal resources</li>
  <li>🧩 Modular code structure</li>
</ul><hr/><!-- 🔥 FUTURE --><h2>🔮 Future Enhancements</h2>Enhancement| Description
🤖 Deep Learning| LSTM / BERT integration
🌐 Web App| Streamlit deployment
📡 API| Real-time news checking
📊 Visualization| Dashboard analytics

<hr/><!-- 🔥 AUTHOR --><h2>👨‍💻 Author</h2><p align="center">
  <b>Anushka Singh</b><br/>
  AI Engineer | NLP | Machine Learning<br/>
</p><hr/><h2 align="center">⚡ Final Insight</h2><p align="center">
<b>"Fighting misinformation with intelligent systems."</b>
</p><hr/><p align="center">
⭐ Star this repository if you found it useful!
</p>
