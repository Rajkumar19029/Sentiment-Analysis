from flask import Flask, render_template, request
from utilites import clean_text, lemmatize_text, vectorizing, sentiment



app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        corpus = request.form['text']

        # Text preprocessing
        cleaned_txt = clean_text(corpus)
        lem_txt=lemmatize_text(cleaned_txt)
        # Vectorization
        vectorized_text = vectorizing(lem_txt)

        # Prediction of Sentiment
        sentiment1 = sentiment(vectorized_text)

        # Convert sentiment to human-readable format
        #sentiment_result = "Positive :)" if sentiment == 1 else "Negative :("
    
        return render_template('result.html', sentiment=sentiment1)

@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')