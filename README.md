# World Federation of Pediatric Intensive & Critical Care Societies (WFPICCS) ML Citation Classification

## WFPICCS Evidence Hackathon: Engaging the conference community in collaborative knowledge synthesis

This project performs text classification on assessment data using a combination of pre-trained fastText embeddings and
machine learning models. Built with Python, the tool reads data from an Excel file, processes it using TF-IDF and
fastText, and outputs classification results in a user-friendly format. Read more about the project
here: [WFPICCS SR](https://insightscope.tech/preview_project/268)

## Built By

This project was developed by **Algonquin College** in partnership with the **Children's Hospital of Eastern Ontario (
C.H.E.O.), Ottawa**.

## Dependencies

This project uses the following Python packages:

| Package         | Version | Documentation |
|----------------|---------|----------------|
| fasttext       | 0.9.3   | [fastText Docs](https://fasttext.cc/docs/en/support.html) |
| matplotlib     | 3.7.5   | [Matplotlib Docs](https://matplotlib.org/stable/index.html) |
| nltk           | 3.9.1   | [NLTK Docs](https://www.nltk.org/) |
| numpy          | 1.24.4  | [NumPy Docs](https://numpy.org/doc/) |
| openpyxl       | 3.1.5   | [openpyxl Docs](https://openpyxl.readthedocs.io/en/stable/) |
| pandas         | 2.0.3   | [Pandas Docs](https://pandas.pydata.org/docs/) |
| pycountry      | 24.6.1  | [pycountry Docs](https://pypi.org/project/pycountry/) |
| scikit-learn   | 1.3.2   | [scikit-learn Docs](https://scikit-learn.org/stable/documentation.html) |
| scipy          | 1.10.1  | [SciPy Docs](https://docs.scipy.org/doc/scipy/) |

Additionally, the project uses the
compressed  [fastText language identification model](https://fasttext.cc/docs/en/language-identification.html): `lid.176.ftz`

## Quick Start

Follow these steps to set up and run the project:

### 1. Create and Activate Your Environment

We recommend using a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 2. Install Requirements

```bash
pip install -r requirements.txt # install required packages
```

### 3. Prepare Your Data

- Place your assessments Excel file (.xlsx) into the data/ directory. The Excel sheet should be named 'Assessments'.
- This Excel sheet should have at least two columns named 'title' and 'abstract'
- It is recommended to use an ID column as well to easily share results for each paper

### 4. Run the Program

```bash
# from the repository root
python main.py
```

### 5. Provide File Path When Prompted and view the output

- When prompted, input the full path to your Excel file
- Your processed results will be saved automatically to the `data/output/` directory.

## Acknowledgements:

The [insightScope](https://www.insightscope.ca) project is a collaborative effort led by Kevin Holmes
from [Algonquin College's Social Innovation Lab](https://slidelab7.ca/), in partnership with students from Algonquin
College and the Children's Hospital of Eastern Ontario (C.H.E.O.) in Ottawa. We gratefully acknowledge the contributions
of all researchers, data scientists, and collaborators involved.
