
import streamlit as st
import nltk
from nltk.stem import PorterStemmer
import pickle
nltk.download('punkt')
nltk.download('stopwords')
import string
from nltk.corpus import stopwords
tf=pickle.load(open('vectorizer.pkl','rb'))
model=pickle.load(open('model.pkl','rb'))

st.title("Email/SMS Spam Classisfier")
input=st.text_input("Enter the message")

def transform_text(text):
  text=text.lower()
  text=nltk.word_tokenize(text)
  y=[]
  for i in text:
    if i.isalnum():
      y.append(i)
  text=y[:]
  y.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      y.append(i)
  text=y[:]
  y.clear()
  ps = PorterStemmer()
  for i in text:
    y.append(ps.stem(i))

  return " ".join(y)

text=transform_text(input)

if st.button("Predict"):
  vector_input=tf.transform([text])
  result=model.predict(vector_input)[0]

  if result==1:
    st.header("Spam")
  else:
    st.header("Not Spam")

