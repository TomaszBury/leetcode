import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    mask_id = students.loc[:,"student_id"] == 101

    return students.loc[mask_id,["name","age"]]


data_full = {
    'student_id': [101, 53, 128, 3],
    'name': ['Ulysses', 'William', 'Henry', 'Henry'],
    'age': [13, 10, 6, 11]
    }


# Create a dictionary from the given data
data_filtered = {
    'name': ['Ulysses'],
    'age': [13]
}

# Create the DataFrame
df = pd.DataFrame(data_filtered)

assert selectData(pd.DataFrame(data_full)).equals(df)