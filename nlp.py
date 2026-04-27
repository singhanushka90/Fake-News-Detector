import streamlit as st
import numpy as np
import pickle 
import re

model=pickle.load(open('nb_model.pkl','rb'))
tfidf=pickle.load(open('tfidf.pkl','rb'))

def transform(text):
    text=text.lower()
    text=re.sub('[^a-zA-Z]', ' ',text)
    text=text.split()
    return " ".join(text)

st.set_page_config(page_title='Fake News Detector',layout='centered')
st.title("Fake News Detection App")
st.write("Enter news text to check whether it is Real or Fake")

user_input=st.text_area("Enter News Here")

if st.button("Predict"):
            if user_input.strip() != "":
                processed=transform(user_input)
                vector=tfidf.transform([processed])
                prediction=model.predict(vector)
                if prediction[0]==1 :
                    st.success("Real News")
                else:
                    st.error("Fake News")

            else:
                st.warning("Please enter some text to predict!")

