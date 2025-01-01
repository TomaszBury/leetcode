import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask_conditions = (patients.loc[:,"conditions"].str.contains(r'(^| )DIAB1', na=False))
    print(patients.loc[mask_conditions,:])
    return patients

data_input = { 'patient_id': [1, 2, 3, 4, 5], 'patient_name': ['Daniel', 'Alice', 'Bob', 'George', 'Alain'], 'conditions': ['YFEV COUGH', '', 'DIAB100 MYOP', 'ACNE DIAB100', 'DIAB201'] } 
# Creating DataFrame 
df_input = pd.DataFrame(data_input)


find_patients(df_input)