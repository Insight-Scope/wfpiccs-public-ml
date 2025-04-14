# Create a dictionary to hold the word tokenizers
WORD_TOKENIZERS = dict(
    lemma=dict(code="lemma", name="Lemmatization"),
    stem=dict(code="stem", name="Stemming")
)

# Create a dictionary to hold the acronyms and their full forms
WFPICCS_COMMON_ABBREVIATIONS = dict(
    nicu="neonatal intensive care unit",
    wfpiccs="world federation of pediatric intensive and critical care societies",
    icu="intensive care unit",
    picu="pediatric intensive care unit",
)

WFPICCS_THRESHOLD_SCORE = dict(
    threshold=1.073868191,
    empty_abstract_threshold=1.05624354,
    exclusion_threshold=1.042033879
)
