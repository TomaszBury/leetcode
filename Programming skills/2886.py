import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})


data_input = { 'student_id': [1, 2], 'name': ['Ava', 'Kate'], 'age': [6, 15], 'grade': [73.0, 87.0] }
df_input = pd.DataFrame(data_input)
df_output = pd.DataFrame(data_input)

df_output.loc[:,"grade"] = df_output.loc[:,"grade"].astype(float)

assert changeDatatype(df_input).equals(df_output)