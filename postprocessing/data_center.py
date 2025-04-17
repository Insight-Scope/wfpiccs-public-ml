import pandas
import re
import pycountry
import fasttext

from model import load_fasttext_language_detection_model


class DataCenter:
    assessment_df: pandas.DataFrame
    required_columns = ["title", "abstract"]

    def __init__(self, assessment_df: pandas.DataFrame):
        # First check if the dataframe is empty and it has the columns title and abstract
        is_dataframe_valid = all(
            col in assessment_df.columns for col in self.required_columns
        )
        if assessment_df.empty or not is_dataframe_valid:
            raise ValueError(
                "DataFrame is empty or does not contain the required columns."
            )

        # If the dataframe is valid, set the assessment_df attribute
        assessment_df['title'] = assessment_df['title'].astype(str)
        assessment_df['abstract'] = assessment_df['abstract'].astype(str)
        self.assessment_df = assessment_df

    def filter_citations(self):
        """Must be called before any other function in this class and reported to the user"""

        # If the title and abstract is empty for this paper then remove it from evaluation
        self.assessment_df = self.assessment_df.loc[
            ~(
                (self.assessment_df["title"] == "")
                & (self.assessment_df["abstract"] == "")
            )
        ]

    def add_features(self):
        # Combine the title and abstract into a new column
        self.assessment_df["title_abstract"] = self.assessment_df[
            ["title", "abstract"]
        ].agg(" ".join, axis=1)
        self.assessment_df['title_abstract'] = self.assessment_df['title_abstract'].astype(str)

        # Check if the abstract is empty, if it is then set the empty_abstract column to True
        # These papers will be evalauted with a lower threshold
        self.assessment_df['empty_abstract'] = self.assessment_df.apply(
            lambda paper: DataCenter.is_empty_abstract(paper.abstract), axis=1
        )

        # Detect the language in the dataframe using a prebuilt fasttext model
        # First load the LID.176.BIN fast-text model to detect the language in a dataframe column
        language_detection_model = load_fasttext_language_detection_model()

        # Using the language detection model and the dataframe, create the new columns by applying the detect_language
        self.assessment_df[["language", "is_english"]] = (
            self.assessment_df["title_abstract"]
            .apply(
                lambda source_text: DataCenter.detect_language(
                    source_text=source_text,
                    language_detection_model=language_detection_model,
                )
            )
            .apply(pandas.Series)
        )
        

    @staticmethod
    def is_empty_abstract(abstract_text: str):
        if isinstance(abstract_text, str):
            return (
                (abstract_text == "")
                | bool(re.match(r"^\w+$", abstract_text))
                | (len(abstract_text) <= 10)
            )
        else:
            return True  # since the abstract isn't even a string we can say the abstract is empty

    @staticmethod
    def detect_language(source_text: str, language_detection_model: fasttext.FastText):
        # If we don't have any source text, exit early
        if not source_text:
            raise Exception("There is no source text for this cell", source_text)

        # Predict what the language is of the source text and using k=1 we can return only the top prediction
        language_prediction = language_detection_model.predict(source_text.replace('\n', ''), k=1)
        language_code = language_prediction[0][0].replace('__label__', '')

        # Now using the language code that was detected from the text and the language code for english
        # we can check if the language of the text is non-english or not and return the name of the language
        english_language = pycountry.languages.get(alpha_2="en")

        # Try and get the language name based on the returned language code from the model, if we can't then text is
        # marked as Unknown, and we return False for its english value
        try:
            language_name = pycountry.languages.get(alpha_2=language_code).name
            is_english_text = english_language.name == language_name
        except AttributeError:
            language_name = "Unknown"
            is_english_text = False
        return language_name, is_english_text
