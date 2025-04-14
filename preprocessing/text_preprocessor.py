import re

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer


class TextPreprocessor:
    word_tokenizer = None
    abbreviation_set = None
    normalization_list = None

    def __init__(self, tokenizer):
        self.abbreviation_set = set()

        # set the word tokenizer type
        self.word_tokenizer = PorterStemmer()

    def clean_text(self, base_text, stop_word_list=None, apply_tokenization: bool = True):
        # if there is no base text, exit early
        if not base_text:
            return

        # set the stopwords list to an empty list if none supplied
        if stop_word_list is None:
            stop_word_list = []

        # remove any punctuation and keep only words
        cleaned_text = re.sub(r'[^a-zA-Z0-9]', ' ', base_text)

        # remove all numbers
        cleaned_text = re.sub(r'\s+[0-9]+\s+', ' ', cleaned_text)

        # remove all single character words
        cleaned_text = re.sub(r'\s+[a-zA-Z]\s+', ' ', cleaned_text)

        # substitute multiple spaces with single spaces
        cleaned_text = re.sub(r'\s+', ' ', cleaned_text, flags=re.I)

        # if there is a normalization list, apply it
        if self.normalization_list:
            for key, value in self.normalization_list.items():
                # first get a list of the values for each key, each item is separated by a comma and may have whitespace
                problem_words = [word.strip() for word in value.split(',')]
                # replace any instance of any value with the normalized version of the word. ie. FaceMask to FacePiece
                for word in problem_words:
                    normalized_text = re.sub(f' {word.lower()}', f' {key.lower()}', cleaned_text)
                    # replace the normalized text if it is changed
                    if cleaned_text != normalized_text:
                        cleaned_text = normalized_text.lower()

        # now apply the preprocessor to the text and convert to word tokens
        tokens = cleaned_text.lower().split()

        # remove stop words
        stopwords_set = stopwords.words("english")
        stopwords_set.extend(stop_word_list)
        stopwords_set = set(stopwords_set)
        tokens = [word for word in tokens if word not in stopwords_set]

        if not apply_tokenization:
            return ' '.join(tokens)

        # apply the stemming to the tokens and then join the tokens back into a string
        tokens = [self.word_tokenizer.stem(word) for word in tokens]
        preprocessed_text = ' '.join(tokens)
        return preprocessed_text
