#libraries download
import nltk
from nltk.tokenize import word_tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from textblob import TextBlob
#tokenizer download
nltk.download('punkt')
nltk.download('punkt_tab')

analyzer = SentimentIntensityAnalyzer()

def analyze_text(text):

#tone detection
    sentiment = analyzer.polarity_scores(text)

    if sentiment['compound'] >= 0.05:
        tone = "Positive"
    elif sentiment['compound'] <= -0.05:
        tone = "Negative"
    else:
        tone = "Neutral"

#mood detection
    mood_keywords = {
        "happy": ["happy", "joy", "excited", "great", "awesome", "love"],
        "sad": ["sad", "unhappy", "depressed", "cry", "lonely"],
        "angry": ["angry", "mad", "furious", "annoyed"],
        "fearful": ["afraid", "scared", "nervous", "worried"],
        "surprised": ["wow", "surprised", "shocked"]
    }

    tokens = word_tokenize(text.lower())

    mood = "neutral"
    for m, words in mood_keywords.items():
        if any(word in tokens for word in words):
            mood = m
            break

    return tone, mood

#test
text = input("Enter text: ")

tone, mood = analyze_text(text)

print("\nTone:", tone)
print("Mood:", mood)
