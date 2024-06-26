import re
from nltk import ParentedTree, Tree
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from .utils import clean, sp

class ISLConverter:
    def __init__(self):
        self.lemmatizer = WordNetLemmatizer()
        self.stopwords_set = set(stopwords.words('english'))

    def convert_isl(self, parsetree):
        dict = {}
        parenttree = ParentedTree.convert(parsetree)
        for sub in parenttree.subtrees():
            dict[sub.treeposition()] = 0
        
        isltree = Tree('ROOT', [])
        i = 0
        for sub in parenttree.subtrees():
            if sub.label() == "NP" and dict[sub.treeposition()] == 0 and dict[sub.parent().treeposition()] == 0:
                dict[sub.treeposition()] = 1
                isltree.insert(i, sub)
                i += 1
            if sub.label() == "VP" or sub.label() == "PRP":
                for sub2 in sub.subtrees():
                    if (sub2.label() == "NP" or sub2.label() == 'PRP') and dict[sub2.treeposition()] == 0 and dict[sub2.parent().treeposition()] == 0:
                        dict[sub2.treeposition()] = 1
                        isltree.insert(i, sub2)
                        i += 1
        for sub in parenttree.subtrees():
            for sub2 in sub.subtrees():
                if len(sub2.leaves()) == 1 and dict[sub2.treeposition()] == 0 and dict[sub2.parent().treeposition()] == 0:
                    dict[sub2.treeposition()] = 1
                    isltree.insert(i, sub2)
                    i += 1
        return isltree

    def text_to_isl(self, sentence):
        pattern = r'[^\w\s]'
        sentence = re.sub(pattern, '', sentence)
        englishtree = [tree for tree in sp.parse(sentence.split())]
        parsetree = englishtree[0]
        isl_tree = self.convert_isl(parsetree)
        words = parsetree.leaves()
        lemmatized_words = [self.lemmatizer.lemmatize(w) for w in words]
        islsentence = " ".join([w for w in lemmatized_words if w not in self.stopwords_set])
        islsentence = islsentence.lower()
        isltree = [tree for tree in sp.parse(islsentence.split())]
        return islsentence
