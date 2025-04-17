from math import isnan

from utils.constants import WFPICCS_THRESHOLD_SCORE


def classify_papers(similarity_score: float, empty_abstract: bool):
    """Classify papers based on the citation text and the threshold scores from the Original WFPICCS Project Run."""
    if isnan(similarity_score):
        # if the similarity score cannot be read then do not assess the citation
        return 'Not Evaluated By ML'
    elif similarity_score >= WFPICCS_THRESHOLD_SCORE['threshold']:
        # The paper's similarity scores exceeds the primary threshold
        return 'Retain|No Assessment'
    elif empty_abstract and similarity_score >= WFPICCS_THRESHOLD_SCORE['empty_abstract_threshold']:
        # the WFPICCS PI decided to use a separate threshold's for citations without an abstract
        return 'Retain|No Assessment'
    elif similarity_score < WFPICCS_THRESHOLD_SCORE['exclusion_threshold']:
        # Fully exclude any papers that are below the exclusion threshold
        return 'Exclude|Exclude'
    # If a paper is in-between the primary threshold and exclusion threshold, partially exclude
    return 'Exclude|No Assessment'
