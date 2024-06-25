# implementing the elimination of unwanted words and lemmatization of text 

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

class Preprocessor:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stop_words = set(stopwords.words('english'))
        
        # additional_words = {'um', 'uh', 'eh', 'mhm', 'like'}
        # self.stop_words.update(additional_words)

    def preprocess(self, tokens):
        filtered = [word for word in tokens if word.lower() not in self.stop_words]
        lemmatized = [self.lemmatizer.lemmatize(word) for word in filtered]
        return lemmatized