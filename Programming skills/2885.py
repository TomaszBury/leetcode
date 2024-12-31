import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # students.columns = ["student_id","first_name","last_name","age_in_years"]
    # return students
    return students.rename(columns = {'id' : 'student_id', 'first':'first_name', 'last':'last_name', 'age':'age_in_years'})


data_input = {
    'id': [1, 2, 3, 4, 5],
    'first': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age': [6, 7, 16, 18, 10]
}
data_output = {
    'student_id': [1, 2, 3, 4, 5],
    'first_name': ['Mason', 'Ava', 'Taylor', 'Georgia', 'Thomas'],
    'last_name': ['King', 'Wright', 'Hall', 'Thompson', 'Moore'],
    'age_in_years': [6, 7, 16, 18, 10]
}

# Create the DataFrame
df_input = pd.DataFrame(data_input)
df_output = pd.DataFrame(data_output)

assert renameColumns(df_input).equals(df_output)