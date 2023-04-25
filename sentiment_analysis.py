import nltk
nltk.download('stopwords')

from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
from nltk.sentiment import SentimentIntensityAnalyzer
import urllib.request
nltk.download('vader_lexicon')



# Define the set of filler words to remove
filler_words = set(stopwords.words('english'))

# Define the sentence to remove filler words from
sentence = "This is a sentence with some filler words in it, such as 'and', 'the', and 'a'."

# Split the sentence into words
words = nltk.word_tokenize(sentence)

# Remove filler words from the list of words
filtered_words = [word for word in words if word.lower() not in filler_words]

# Join the remaining words back into a sentence
filtered_sentence = ' '.join(filtered_words)

# Print the filtered sentence
print(filtered_sentence)


# Download the article text
url = "https://www.brighthedge.com/technical-analysis/"
html = urllib.request.urlopen(url).read()
text = html.decode('utf8')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Perform sentiment analysis on the article text
scores = sia.polarity_scores(text)

# Print the sentiment scores
print("Negative Score: ", scores['neg'])
print("Neutral Score: ", scores['neu'])
print("Positive Score: ", scores['pos'])
print("Compound Score: ", scores['compound'])
