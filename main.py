import warnings

from classifier import classify_papers
from model import load_embedding_model_from_pickle, apply_embedding_model_to_text
from postprocessing import DataCenter
from preprocessing import TextPreprocessor
from utils import read_excel_file_to_dataframe, WFPICCS_INCLUSION_CRITERIA_TA, WFPICCS_GOAL_OF_PROJECT

warnings.filterwarnings("ignore", category=UserWarning)


def main():
    # First get the file path of the excel file from the users
    # This should have the columns title and abstract
    # We recommend adding this file to the data folder
    file_path = input("Enter the path to the Excel file: ")
    assessment_dataframe = read_excel_file_to_dataframe(file_path)
    
    # Use the DataCenter class to filter the dataframe first and report back to the main user how many papers were removed
    print(f"Total papers in the dataframe: {assessment_dataframe.shape[0]}")
    assessment_datacenter = DataCenter(assessment_dataframe)
    assessment_datacenter.filter_citations()
    print(f"Total papers after filtering: {assessment_datacenter.assessment_df.shape[0]}")
    
    # Add features to the dataframe
    assessment_datacenter.add_features()
    assessment_dataframe = assessment_datacenter.assessment_df
    
    # Clean the text in the combined title and abstract column
    text_preprocessor = TextPreprocessor()
    assessment_dataframe["title_abstract"] = assessment_dataframe.apply(
        lambda row: text_preprocessor.clean_text(f"{row['title']} {row['abstract']}"), axis=1
    )
    
    # Create the project query (the search vector) based on the project settings
    cleaned_project_query = text_preprocessor.clean_text(' '.join([WFPICCS_GOAL_OF_PROJECT, WFPICCS_INCLUSION_CRITERIA_TA]))

    # Load the prebuilt tf_idf model from the WFPICCS project and evaluate each citation
    wfpiccs_tf_idf_model = load_embedding_model_from_pickle()
    assessment_dataframe['stem_tf_idf_cosine_similarity_score'] = assessment_dataframe['title_abstract'].apply(
        lambda citation: apply_embedding_model_to_text(
            search_text=cleaned_project_query,
            comparison_text=citation,
            embedding_model=wfpiccs_tf_idf_model
        )
    )

    # With the evaluated citations we can now classify them as Retain (or No Assessment) or Exclude
    assessment_dataframe["Reviewer Response"] = assessment_dataframe[['stem_tf_idf_cosine_similarity_score', 'empty_abstract']].apply(
        lambda citation: classify_papers(
            similarity_score=citation['stem_tf_idf_cosine_similarity_score'],
            empty_abstract=citation['empty_abstract']
        ),
        axis=1
    )

    # Save the results to an excel file
    assessment_dataframe.to_excel("data/output/wfpiccs_citation_evaluation_output.xlsx", index=False)
    print(">>> WFPICCS Citation Evaluation is Complete: Results saved to <data/output/wfpiccs_citation_evaluation_output.xlsx>")


if __name__ == "__main__":
    main()
