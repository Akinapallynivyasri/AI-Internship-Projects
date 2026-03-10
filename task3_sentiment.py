import pandas as pd
import pickle

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


df = pd.read_csv("reviews.csv")

print("\nDataset preview:\n", df.head())



df['sentiment'] = df['sentiment'].map({'positive':1, 'negative':0})



vectorizer = CountVectorizer()

X = vectorizer.fit_transform(df['review'])
y = df['sentiment']



model = LogisticRegression()
model.fit(X, y)



pred = model.predict(X)
print("\nAccuracy:", accuracy_score(y, pred))



pickle.dump(model, open("sentiment_model.pkl","wb"))
pickle.dump(vectorizer, open("sentiment_vectorizer.pkl","wb"))

print("\nModel saved successfully")



print("\nEnter review (type quit to stop)\n")

while True:
    msg = input("Review: ")

    if msg.lower() == "quit":
        break

    result = model.predict(vectorizer.transform([msg]))

    if result[0] == 1:
        print("Sentiment: Positive 😊\n")
    else:
        print("Sentiment: Negative 😞\n")