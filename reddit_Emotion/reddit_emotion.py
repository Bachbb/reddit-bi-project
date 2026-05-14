import pandas as pd
from textblob import TextBlob


df = pd.read_csv("reddit_cleaned.csv")


df = df.dropna()  


def get_sentiment(text):
    polarity = TextBlob(str(text)).sentiment.polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

df["sentiment"] = df["text"].apply(get_sentiment)

def get_rating(sentiment):
    if sentiment == "Positive":
        return 5
    elif sentiment == "Negative":
        return 1
    else:
        return 3

df["rating"] = df["sentiment"].apply(get_rating)


df["date"] = pd.to_datetime(df["date"], errors='coerce')


df.to_csv("reddit_cleaned_final.csv", index=False)

print("Done ETL + Sentiment")