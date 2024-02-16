# tokenization
import nltk
nltk.download('punkt')

example_string = """
We’ll sit for a little on the low wall, up on the hill, 
and as the spring breeze blows around us
perhaps we’ll even imagine that we are flying... Yiannis Ritsos 
"""
nltk.sent_tokenize(example_string)
nltk.word_tokenize(example_string)



# Lemmatizing
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nltk.download('wordnet')
string_for_lemmatizing = "The friends of DeSoto love scarves."
words = word_tokenize(string_for_lemmatizing)
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
lemmatizer.lemmatize("worst")
lemmatizer.lemmatize("worst", pos="a")



# Stemming
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
nltk.download('stopwords')
# Define input text
text = """
The moon has set, and the Pleiades;
It is midnight, the time is going by,
And I lie alone.
Sappho.
"""
# Tokenize the text
tokens = nltk.word_tokenize(text)
# Define stop words
stop_words = set(stopwords.words("english"))
# Remove stop words
filtered_tokens = [token for token in tokens if token.lower() not in stop_words]
# Perform stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(token) for token in filtered_tokens]
# Print the stemmed tokens
print(stemmed_tokens)


# Named Entity Recognition (NER) 
# NER involves identifying named entities (e.g., names of people, organizations, locations) in text.
from nltk import ne_chunk
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
text = """The emperor Alexios Komnenos was a man of war, and he was well known in his time."""
tokens = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(tokens)
named_entities = ne_chunk(pos_tags)
print(named_entities)




