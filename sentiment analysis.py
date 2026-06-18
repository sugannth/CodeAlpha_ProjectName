import pandas as pd
from textblob import TextBlob

df = pd.read_csv(r"D:\25CS270\Intern\alpha2-sentiment analysis\IMDB Dataset.csv")

def get_sentiment(text):
    score = TextBlob(text).sentiment.polarity

    if score > 0:
        return "Positive"
    elif score < 0:
        return "Negative"
    else:
        return "Neutral"

df['Sentiment'] = df['review'].apply(get_sentiment)

#output


print(df['Sentiment'].value_counts())

import seaborn as sns
import matplotlib.pyplot as plt

sns.countplot(x='Sentiment', data=df)

plt.title("Sentiment Analysis")
plt.show()
