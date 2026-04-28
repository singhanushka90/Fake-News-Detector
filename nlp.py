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
