from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Dummy prediction (Render-safe version)
    disease = random.choice(["Healthy", "Leaf Blight", "Powdery Mildew"])
    risk = random.choice(["Low", "Moderate", "High"])
    return render_template('result.html', disease=disease, risk=risk)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 10000))  # Render uses PORT
    app.run(host="0.0.0.0", port=port)
