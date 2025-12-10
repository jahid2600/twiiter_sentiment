// script.js

const analyzeBtn = document.getElementById('analyze-btn');
const fetchBtn = document.getElementById('fetch-btn');
const textInput = document.getElementById('text-input');
const usernameInput = document.getElementById('username-input');
const resultDiv = document.getElementById('result');
const tweetsDiv = document.getElementById('tweets-result');

const API_BASE = 'http://127.0.0.1:5000';

// Analyze custom text
analyzeBtn.addEventListener('click', async () => {
    const text = textInput.value.trim();
    if (!text) {
        alert('Please enter some text');
        return;
    }
    resultDiv.innerHTML = 'Analyzing...';

    try {
        const response = await fetch(`${API_BASE}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text })
        });
        const data = await response.json();
        if (data.sentiment) {
            resultDiv.innerHTML = `<div class="card ${data.sentiment === 'Negative' ? 'negative' : ''}">${data.sentiment}</div>`;
        } else {
            resultDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (err) {
        resultDiv.innerHTML = `<p>Error connecting to backend</p>`;
    }
});

// Fetch tweets for a username
fetchBtn.addEventListener('click', async () => {
    const username = usernameInput.value.trim();
    if (!username) {
        alert('Please enter a Twitter username');
        return;
    }
    tweetsDiv.innerHTML = 'Fetching tweets...';

    try {
        const response = await fetch(`${API_BASE}/tweets?username=${username}&count=10`);
        const data = await response.json();
        if (data.tweets) {
            tweetsDiv.innerHTML = '';
            data.tweets.forEach(tweet => {
                const card = document.createElement('div');
                card.className = `card ${tweet.sentiment === 'Negative' ? 'negative' : ''}`;
                card.innerHTML = `<p>${tweet.text}</p><strong>${tweet.sentiment}</strong>`;
                tweetsDiv.appendChild(card);
            });
        } else {
            tweetsDiv.innerHTML = `<p>Error: ${data.error}</p>`;
        }
    } catch (err) {
        tweetsDiv.innerHTML = `<p>Error connecting to backend</p>`;
    }
});
