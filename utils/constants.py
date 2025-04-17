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

WFPICCS_GOAL_OF_PROJECT = """
Advances in survival of pediatric ICU (PICU) patients has led to increased interest in the burden of morbidity and the physical, cognitive, social, and psychologic impairments experienced by PICU survivors, as well as the psycho-social impact on family members. Recognizing the importance of better understanding and improving the long term outcomes of pediatric critical care survivors and their families, investigators from the Canadian Critical Care Trials Group (CCCTG), including the Canadian PICU Follow-up Consortium and the Canadian Critical Illness Recovery Consortium (CCCIRC) are collaborating on a wide range of projects. 
One of the initial priorities of this collaborative is a living scoping review of studies evaluating long term outcome following pediatric critical illness. This scoping review will be accompanied by an open access database available to the broader international PICU community to facilitate the conduct of more focused systematic and scoping reviews. This living scoping review will identify all studies describing a population or cohort of children having been admitted to a PICU and investigating or reporting on the health of the child or a caregiver/family member after discharge. 
The first two knowledge synthesis projects that will use this database have been identified and include: 
(1) Development of Post-PICU Follow Up Clinics: A Living Scoping Review (see https://pediatrics.knack.com/wfpiccs22#followup-project/ for further details), 
(2) Posttraumatic Stress in the Pediatric Intensive Care Unit: A systematic review (see https://pediatrics.knack.com/wfpiccs22#ptsd-project/ for further details). 
Following peer-review, the electronic database search for this living scoping review has identified over 16000 citations for screening. Our goal is to assemble a team of 20 to 30 members of the PICU community to participate in both the development of the living scoping review (see Comments & Advice to Reviewers, below) and the two focused projects. Team recruitment will occur through the WFPICCS Conference and Evidence Hackathon workshop, held on July 12, 2022 (Workshop ID WO4) (see https://pediatrics.knack.com/wfpiccs22#home/ for more details). Once assembled, the team will work together in the 2 to 4 weeks following the WFPICCS conference to complete the project tasks. Approximately 2 months following the conference, we will present the results of this initiative back to the WFPICCS community as part of a seminar.
"""

WFPICCS_INCLUSION_CRITERIA_TA = """
#PICU PATIENTS: Study participants must be patients 0-17 years of age admitted to a PICU (ex. trauma, medical, surgical, congenital cardiac) surviving to discharge, AND/OR the family members or caregivers of such patients. NOTE: PICU CLUE WORDS: Cardiac surgery, ECMO/ECLS, CRRT, Solid Organ Transplant, Neurocritical Care, Severe TBI, Severe/critical injury/trauma, severe burns or “burn unit”, Severe pulmonary hypertension, Shock.  NOTE: CARDIAC SURGERY CLUE WORDS: Atrial septostomy, ASD/VSD/AVSD repair, Tetralogy of Tallot repair, named cardiac surgical procedures: Norwood, Glenn, Fontan, Sano; pump time, cardiac bypass, HLHS, cyanotic heart disease repair.   NOTE: retain surveys of health care providers regarding follow up of post-PICU patients or family members. 

#PRIMARY PICU: Patients recruited from PICU, -OR- If mixed population (settings outside of PICU, mixed ages) PICU patient outcomes must be reported separately.

#FOLLOW-UP: Must describe some type of follow up assessment or data at 14 days or later post PICU. Follow up data can be of any content or obtained in any format. The assessment may be conducted for clinical or research purposes. NOTE: FOLLOW UP EXAMPLES: mortality or readmission statistics, mental health of child or parent, neuro-development, neurologic or functional status, weight gain, quality of life, tracheal stenosis, surgical site integrity, renal function, post-op organ function. 

#STUDY DESIGN: Any of the following will be included: observational or interventional studies, qualitative research, surveys of patients/families or care providers, and study protocols. Scoping reviews or systematic reviews on the subject will also be included, for the purpose of reviewing reference lists

#PUBLICATION: Published in or after year 2000. No language restrictions.
"""
