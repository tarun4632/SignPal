from nltk.parse.stanford import StanfordParser

# Initialize the Stanford Parser
sp = StanfordParser(
    path_to_jar='path/to/stanford-parser-full-2018-02-27/stanford-parser.jar',
    path_to_models_jar='path/to/stanford-parser-full-2018-02-27/stanford-parser-3.9.1-models.jar'
)

