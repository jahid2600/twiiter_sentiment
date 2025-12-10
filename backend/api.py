# backend/api.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re
import nltk
from nltk.corpus import stopwords
import os
import requests
from dotenv import load_dotenv

# Import database
from db_setup import Session, Tweet
import time

# Load environment variables from .env
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '.env'))

app = Flask(__name__)
CORS(app)

# Download stopwords (only first time)
nltk.download('stopwords', quiet=True)
stop_words = stopwords.words('english')

# Paths to your model files
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model', 'model.pkl')
VECT_PATH  = os.path.join(os.path.dirname(__file__), 'model', 'vectorizer.pkl')

# Lazy-load model
_model = None
_vectorizer = None

def load_model_and_vectorizer():
    global _model, _vectorizer
    if _model is None or _vectorizer is None:
        if not os.path.exists(MODEL_PATH) or not os.path.exists(VECT_PATH):
            raise FileNotFoundError("model files not found. Place model.pkl and vectorizer.pkl in backend/model/")
        with open(MODEL_PATH, 'rb') as f:
            _model = pickle.load(f)
        with open(VECT_PATH, 'rb') as f:
            _vectorizer = pickle.load(f)
    return _model, _vectorizer

def predict_text(text):
    model, vectorizer = load_model_and_vectorizer()
    clean = re.sub('[^a-zA-Z]', ' ', text)
    clean = clean.lower().split()
    clean = [w for w in clean if w not in stop_words]
    clean = ' '.join(clean)
    vec = vectorizer.transform([clean])
    pred = model.predict(vec)[0]
    return "Positive" if (str(pred).lower() in ['1','positive','pos']) else "Negative"

# Optional: Twitter API token
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

@app.route('/')
def index():
    return jsonify({"message": "Sentiment API ready"}), 200

@app.route('/predict', methods=['POST'])
def predict_route():
    data = request.get_json(silent=True) or {}
    text = data.get('text', '')
    if not text.strip():
        return jsonify({"error": "text is required"}), 400
    try:
        label = predict_text(text)
        return jsonify({"sentiment": label}), 200
    except FileNotFoundError as e:
        return jsonify({"error": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/tweets', methods=['GET'])
def tweets_route():
    username = request.args.get('username', '').strip()
    count = request.args.get('count', 10)
    try:
        count = int(count)
        if count < 1: count = 10
        if count > 100: count = 100
    except:
        count = 10

    if not username:
        return jsonify({"error": "username query param is required"}), 400
    if not BEARER_TOKEN:
        return jsonify({"error": "BEARER_TOKEN not set in backend/.env"}), 500

    session = Session()

    # Check DB first
    cached_tweets = session.query(Tweet).filter(Tweet.username == username)\
        .order_by(Tweet.fetched_at.desc()).limit(count).all()
    if cached_tweets:
        tweets = [{"text": t.text, "sentiment": t.sentiment} for t in cached_tweets]
        session.close()
        return jsonify({"tweets": tweets, "cached": True}), 200

    # Fetch from Twitter API
    headers = {"Authorization": f"Bearer {BEARER_TOKEN}"}
    url = f"https://api.twitter.com/2/tweets/search/recent?query=from:{username}&tweet.fields=text&max_results={count}"

    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code != 200:
            session.close()
            return jsonify({"error": f"Twitter API error {resp.status_code}", "body": resp.text}), 502

        data = resp.json()
        tweets = []
        for t in data.get('data', []):
            tweet_text = t.get('text', '')
            sentiment = predict_text(tweet_text)
            tweets.append({"text": tweet_text, "sentiment": sentiment})

            # Store in DB
            db_tweet = Tweet(username=username, text=tweet_text, sentiment=sentiment)
            session.add(db_tweet)

        session.commit()
        session.close()
        return jsonify({"tweets": tweets, "cached": False}), 200

    except requests.exceptions.RequestException as e:
        session.close()
        return jsonify({"error": f"Connection error: {str(e)}"}), 500
    except Exception as e:
        session.close()
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
