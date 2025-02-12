import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:

    menager_count = employee["managerId"].value_counts(dropna=False)
    
    merged_df = pd.merge(employee, menager_count, left_on='id', right_index=True, how='left')

    mask = merged_df.loc[:,"count"] > 4

    return merged_df.loc[mask,["name"]]

# Data for the DataFrame
data = {
    'id': [101, 102, 103, 104, 105, 106],
    'name': ['John', 'Dan', 'James', 'Amy', 'Anne', 'Ron'],
    'department': ['A', 'A', 'A', 'A', 'A', 'B'],
    'managerId': [None, 101, 101, 101, 101, 101]
}

# Creating DataFrame
df = pd.DataFrame(data)

print(find_managers(df))