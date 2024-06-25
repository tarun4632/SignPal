# combines all the steps of isl_generator and preprocessing into a single pipeline

from .parser import EnglishParser
from .parser import SentenceReorderer
from .preprocessor import Eliminator
from .preprocessor import Lemmatizer

class ISLGenerator:
    def __init__(self):
        self.parser = EnglishParser()
        self.reorderer = SentenceReorderer()
        self.eliminator = Eliminator()
        self.lemmatizer = Lemmatizer()

    def process(self, text):
        parsed = self.parser.parse(text)

        reordered = self.reorderer.reorder(parsed)

        eliminated = self.eliminator.eliminate(reordered)

        lemmatized = self.lemmatizer.lemmatize(eliminated)

        return lemmatized