import pickle
import re
from nltk.stem import WordNetLemmatizer
#txt=input()
def clean_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text)  # Remove special characters and punctuation
    text = text.lower()  # Convert text to lowercase
    return text
def lemmatize_text(text):
    lemmatizer = WordNetLemmatizer()
    tokens = text.split()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)

def vectorizing(lemmatized_txt):
    fname='vectorizer'
    vec_model=pickle.load(open(fname,'rb'))
    vec_txt=vec_model.transform([lemmatized_txt])
    return vec_txt
def sentiment(vec_txt):
    file_name='sentiment analyzer'
    sent=pickle.load(open(file_name,'rb'))
    l_pred=sent.predict(vec_txt)
    for i in l_pred:
        return i