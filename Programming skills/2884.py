import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:,"salary"] = employees.loc[:,"salary"] * 2
    return employees

data_input = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [19666, 74754, 62509, 54866]
}
data_output = {
    'name': ['Jack', 'Piper', 'Mia', 'Ulysses'],
    'salary': [39332, 149508, 125018, 109732]
}

# Create the DataFrame
df_output = pd.DataFrame(data_output)
df_input = pd.DataFrame(data_input)

assert modifySalaryColumn(df_input).equals(df_output)