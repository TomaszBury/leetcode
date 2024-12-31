import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    students.dropna(inplace=True,ignore_index=True, subset="name")
    return students

data_input = {
    'student_id': [32, 217, 779, 849],
    'name': ['Piper', None, 'Georgia', 'Willow'],
    'age': [5, 19, 20, 14]
}

# Create the DataFrame. Note that pandas represents None as NaN (Not a Number)
df_input = pd.DataFrame(data_input)

data_output = {
    'student_id': [32, 779, 849],
    'name': ['Piper', 'Georgia', 'Willow'],
    'age': [5, 20, 14]
}

# Create the DataFrame
df_output = pd.DataFrame(data_output)

assert dropMissingData(df_input).equals(df_output)

data_input = {
    'student_id': [355, 951, 470, 977, 300],
    'name': [None, None, 'Quincy', 'Sophia', 'Liam'],
    'age': [9, 8, 20, None, 15]
}
data_output = {
    'student_id': [470, 977, 300],
    'name': ['Quincy', 'Sophia', 'Liam'],
    'age': [20, None, 15]
}

df_input = pd.DataFrame(data_input)
df_output = pd.DataFrame(data_output)

assert dropMissingData(df_input).equals(df_output)