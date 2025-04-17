import fasttext
import os


def load_fasttext_language_detection_model():
    """Load the fasttext language detection model."""
    # Load the LID.176.BIN fast-text model to detect the language in a dataframe column
    dir_name = os.path.dirname(__file__)
    model_path = os.path.join(dir_name, "lid.176.ftz")
    language_detection_model = fasttext.load_model(model_path)
    return language_detection_model
