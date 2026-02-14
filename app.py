from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    disease = random.choice(["Healthy", "Leaf Blight", "Powdery Mildew"])
    risk = random.choice(["Low", "Moderate", "High"])
    return render_template('result.html', disease=disease, risk=risk)

if __name__ == '__main__':
    app.run(debug=True)
