import streamlit as st
import numpy as np
import pickle
import re

# Load model
model = pickle.load(open('nb_model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))

# Text preprocessing
def transform(text):
    text = text.lower()
    text = re.sub('[^a-zA-Z]', ' ', text)
    text = text.split()
    return " ".join(text)

# Page config
st.set_page_config(page_title='Fake News Detector', layout='centered')

# UI
st.title("📰 Fake News Detection System")
st.markdown("Detect whether a news article is **Real or Fake** using Machine Learning")

# Input box
user_input = st.text_area("✍️ Enter News Content")

# Predict button
if st.button("🔍 Analyze News"):
    if user_input.strip() != "":

        # Preprocess
        processed = transform(user_input)
        vector = tfidf.transform([processed])

        # Prediction
        prediction = model.predict(vector)[0]
        prob = model.predict_proba(vector)[0]

        # Confidence
        confidence = round(max(prob) * 100, 2)

        st.subheader("📊 Result")

        if prediction == 1:
            st.success(f"✅ Real News ({confidence}% confidence)")
        else:
            st.error(f"🚫 Fake News ({confidence}% confidence)")

        # Show probability breakdown
        st.subheader("🔎 Prediction Details")
        st.write(f"Real News Probability: {round(prob[1]*100,2)}%")
        st.write(f"Fake News Probability: {round(prob[0]*100,2)}%")

        # Extra feature: show processed text (optional)
        with st.expander("🔧 Processed Text"):
            st.write(processed)

    else:
        st.warning("⚠️ Please news text!")
