import pandas


def read_excel_file_to_dataframe(file_path: str) -> pandas.DataFrame:
    """Reads an Excel file and returns a DataFrame."""
    try:
        excel_dataframe = pandas.read_excel(
            file_path, sheet_name="Assessments", engine="openpyxl"
        )
        return excel_dataframe
    except Exception as e:
        print(f"Error reading the Excel file: {e}")
        return pandas.DataFrame()  # Return an empty DataFrame on error
