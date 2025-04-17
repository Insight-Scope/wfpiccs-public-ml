import os
import pickle

from scipy import spatial
from sklearn.feature_extraction.text import TfidfVectorizer


def load_embedding_model_from_pickle():
    """Load the embedding model from a pickle file stored in this GitHub Repo."""
    # Open the pickle file containing the TF-IDF embedding model (make sure to close before returning)
    dir_name = os.path.dirname(__file__)
    model_path = os.path.join(dir_name, "project_268_tf_idf_embedding_model.pkl")
    tf_idf_pickle_file = open(model_path, 'rb')

    # Load the TF-IDF embedding model which is a pickled TfidfVectorizer
    tf_idf_embedding_model = pickle.load(tf_idf_pickle_file)
    tf_idf_pickle_file.close()
    return tf_idf_embedding_model


def apply_embedding_model_to_text(search_text, comparison_text, embedding_model: TfidfVectorizer):
    """Apply the TF-IDF embedding model to a given text."""
    # Transform the text using the TF-IDF embedding model and convert the sparse matrix to a dense array
    search_vector = embedding_model.transform([search_text]).toarray().flatten()
    comparison_vector = embedding_model.transform([comparison_text]).toarray().flatten()

    # Evaluate the similarity between the two vectors using cosine similarity
    citation_cosine_similarity_score = spatial.distance.cosine(search_vector, comparison_vector)

    # Finally invert the score to get a similarity score. By inverting the scores, we prioritize documents
    # with lower distances, effectively highlighting the top percentiles of papers that closely match the search query.
    return 1 / citation_cosine_similarity_score
