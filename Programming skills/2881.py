import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees.loc[:,"bonus"] = employees.loc[:,"salary"] * 2
    return employees


data_input = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433]
}

# Create the DataFrame
df_input = pd.DataFrame(data_input)

data_output = {
    'name': ['Piper', 'Grace', 'Georgia', 'Willow', 'Finn', 'Thomas'],
    'salary': [4548, 28150, 1103, 6593, 74576, 24433],
    'bonus': [9096, 56300, 2206, 13186, 149152, 48866]
}

# Create the DataFrame
df_output = pd.DataFrame(data_output)

assert createBonusColumn(df_input).equals(df_output)