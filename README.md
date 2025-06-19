# youtubesentimentanalyser
This Python project analyzes YouTube video comments in any language by translating them to English and evaluating sentiment using both text and emojis
Sure, Yugandhar! Here's a clean and professional **`README.md`** file for your **Multilingual YouTube Comment Sentiment Analyzer** project:

---

````markdown
# 🎬 YouTube Comment Sentiment Analyzer (Multilingual + Emoji)

This Python project analyzes comments from any YouTube video by detecting their language, translating them to English, and evaluating sentiment using both text polarity and emoji emotion scoring. Results are visualized in a clean pie chart.

---

## 🚀 Features

- 🌍 Supports comments in **any language** (auto-detection + translation)
- 😃 Includes **emoji sentiment** to improve accuracy
- 📊 Visualizes sentiments as **Positive**, **Neutral**, and **Negative**
- 🧠 Uses `TextBlob` + `GoogleTranslator` + `emoji` libraries
- 🔑 Integrates with YouTube Data API v3

---

## 📦 Dependencies

Install the required Python libraries:

```bash
pip install requests matplotlib textblob deep-translator emoji
python -m textblob.download_corpora
````

---

## 🔧 Configuration

Open `youtube_sentiment_analyzer.py` and update the following variables:

```python
API_KEY = "YOUR_YOUTUBE_API_KEY"
VIDEO_ID = "YOUR_YOUTUBE_VIDEO_ID"
```

---

## ▶️ How to Run

```bash
python youtube_sentiment_analyzer.py
```

You’ll see:

* Console summary of sentiment counts
* Pie chart showing sentiment distribution

---

## 📌 Example Output

```
📥 Fetching comments for video ID: dQw4w9WgXcQ
✅ Fetched 50 comments.
🧠 Analyzing sentiments...
📊 Visualizing results...

🎯 Emoji-Aware Summary:
😊 Positive: 33
😐 Neutral : 10
😠 Negative: 7
```

---

## 💡 Future Improvements

* 🌐 Gradio Web UI
* 📁 Export to CSV
* 📈 Emoji trend graph
* 💬 Show top positive/negative comments

---
## 👨‍💻 Author

[Yugandhar]((https://github.com/yugandhar-2003)) – B.Tech CSE, BVRIT

```
