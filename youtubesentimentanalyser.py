import requests
import matplotlib.pyplot as plt
from textblob import TextBlob
from deep_translator import GoogleTranslator
import emoji
 
API_KEY = "YOUR_YOUTUBE_API_KEY"  # Replace with API key
VIDEO_ID = "dQw4w9WgXcQ"          # Replace with YouTube video ID
MAX_COMMENTS = 50
 
emoji_sentiment = {
    '😊': 1, '😄': 1, '😍': 1, '😂': 1, '👍': 1, '🔥': 1,
    '😐': 0, '🤔': 0, '😶': 0,
    '😠': -1, '😡': -1, '👎': -1, '💔': -1, '😭': -1
}
 
def fetch_comments(video_id, api_key, max_comments=50):
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        'part': 'snippet',
        'videoId': video_id,
        'key': api_key,
        'maxResults': 100,
        'textFormat': 'plainText'
    }
    response = requests.get(url, params=params).json()
    comments = []

    for item in response.get('items', [])[:max_comments]:
        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
        comments.append(comment)

    return comments
 
def translate_comment(comment):
    try:
        return GoogleTranslator(source='auto', target='en').translate(comment)
    except:
        return None

# === EMOJI SCORE ===
def get_emoji_sentiment(comment):
    score = 0
    for char in comment:
        score += emoji_sentiment.get(char, 0)
    return score
 
def analyze_sentiments_advanced(comments):
    sentiments = {"positive": 0, "neutral": 0, "negative": 0}

    for comment in comments:
        translated = translate_comment(comment)

        if not translated or translated.strip() == "":
            continue

        try:
            text_polarity = TextBlob(translated).sentiment.polarity
        except Exception:
            continue

        emoji_score = get_emoji_sentiment(comment)
        final_score = text_polarity + (emoji_score * 0.5)

        if final_score > 0.1:
            sentiments["positive"] += 1
        elif final_score < -0.1:
            sentiments["negative"] += 1
        else:
            sentiments["neutral"] += 1

    return sentiments

 
def visualize_sentiments(sentiment_counts):
    labels = ['Positive 😊', 'Neutral 😐', 'Negative 😠']
    sizes = [
        sentiment_counts['positive'],
        sentiment_counts['neutral'],
        sentiment_counts['negative']
    ]
    colors = ['green', 'gray', 'red']
    plt.figure(figsize=(6,6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=140)
    plt.title('YouTube Comment Sentiment (Text + Emoji)')
    plt.axis('equal')
    plt.show()

    print("\n🎯 Emoji-Aware Summary:")
    print(f"😊 Positive: {sentiment_counts['positive']}")
    print(f"😐 Neutral : {sentiment_counts['neutral']}")
    print(f"😠 Negative: {sentiment_counts['negative']}")

 
if __name__ == "__main__":
    print(f"📥 Fetching comments for video ID: {VIDEO_ID}")
    comments = fetch_comments(VIDEO_ID, API_KEY, MAX_COMMENTS)
    print(f"✅ Fetched {len(comments)} comments.")

    print("🧠 Analyzing sentiments...")
    sentiment_result = analyze_sentiments_advanced(comments)

    print("📊 Visualizing results...")
    visualize_sentiments(sentiment_result)
