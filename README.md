# Twitter Sentiment Analysis

A machine learning-powered web application for analyzing sentiment in text and Twitter tweets. This project uses a Logistic Regression model trained on 1.6 million tweets to classify text as either positive or negative sentiment.

## 🚀 Features

- **Text Sentiment Analysis**: Analyze sentiment of any text input
- **Twitter Integration**: Fetch and analyze tweets from any Twitter user
- **Real-time Analysis**: Get instant sentiment predictions with visual feedback
- **Web Interface**: User-friendly Streamlit-based web application
- **High Accuracy**: Model trained on 1.6 million tweets with ~77.6% accuracy

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package manager)
- Twitter API Bearer Token (for fetching tweets)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sentiment-analysis.git
   cd sentiment-analysis
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv myenv
   
   # On Windows
   myenv\Scripts\activate
   
   # On macOS/Linux
   source myenv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```
   BEARER_TOKEN=your_twitter_bearer_token_here
   ```
   
   To get a Twitter Bearer Token:
   - Go to [Twitter Developer Portal](https://developer.twitter.com/)
   - Create a new app
   - Generate a Bearer Token

5. **Download NLTK data** (if not already downloaded)
   ```python
   import nltk
   nltk.download('stopwords')
   ```

## 🎯 Usage

### Running the Application

1. **Start the Streamlit app**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   - The app will automatically open at `http://localhost:8501`
   - If not, navigate to the URL shown in the terminal

### Using the Application

#### Option 1: Input Text Analysis
1. Select "Input text" from the dropdown
2. Enter any text you want to analyze
3. Click "Analyze" to get the sentiment prediction

#### Option 2: Twitter User Analysis
1. Select "Get tweets from user" from the dropdown
2. Enter a Twitter username (without @)
3. Click "Fetch Tweets" to retrieve and analyze the user's latest tweets
4. View sentiment results with color-coded cards:
   - 🟢 Green: Positive sentiment
   - 🔴 Red: Negative sentiment

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Vectorization**: TF-IDF (Term Frequency-Inverse Document Frequency)
- **Text Preprocessing**:
  - Removal of special characters
  - Lowercasing
  - Stop word removal
  - Stemming using Porter Stemmer
- **Training Data**: 1.6 million processed tweets
- **Accuracy**: ~77.6%
- **Test Split**: 20% of the dataset

## 📁 Project Structure

```
sentiment-analysis/
│
├── app.py                              # Main Streamlit application
├── twitter_sentiment_analysis.ipynb    # Jupyter notebook for model training
├── model.pkl                           # Trained Logistic Regression model
├── vectorizer.pkl                      # TF-IDF vectorizer
├── requirements.txt                    # Python dependencies
├── training.1600000.processed.noemoticon.csv  # Training dataset
├── .env                                # Environment variables (create this)
└── README.md                           # This file
```

## 🔧 Technologies Used

- **Python**: Core programming language
- **Streamlit**: Web application framework
- **scikit-learn**: Machine learning library (Logistic Regression, TF-IDF)
- **NLTK**: Natural Language Toolkit for text preprocessing
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **pickle**: Model serialization
- **requests**: HTTP library for Twitter API calls
- **python-dotenv**: Environment variable management

## 📝 Training the Model

If you want to retrain the model:

1. Open `twitter_sentiment_analysis.ipynb` in Jupyter Notebook
2. Ensure the training dataset is in the same directory
3. Run all cells to train and save the model
4. The trained model and vectorizer will be saved as `model.pkl` and `vectorizer.pkl`

## ⚠️ Limitations

- The model is trained on Twitter data and may perform better on similar text styles
- Twitter API rate limits apply when fetching tweets
- The model classifies sentiment as binary (Positive/Negative) only
- Accuracy is ~77.6%, so predictions may not always be perfect

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

Your Name - [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- Training dataset: [Sentiment140 Dataset](http://help.sentiment140.com/for-students)
- Twitter API for tweet fetching capabilities
- Streamlit for the amazing web framework

---

⭐ If you found this project helpful, please consider giving it a star!

