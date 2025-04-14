import pickle


def load_embedding_model_from_pickle():
    """Load the embedding model from a pickle file stored in this GitHub Repo."""
    tf_idf_pickle_file = open('model/project_268_tf_idf_embedding_model.pickle', 'rb')
    tf_idf_embedding_model = pickle.load(tf_idf_pickle_file)
    tf_idf_pickle_file.close()
    return tf_idf_embedding_model
