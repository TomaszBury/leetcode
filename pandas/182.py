import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated_emails = person[person.duplicated(subset=['email'], keep=False)]['email'].unique()
    return pd.DataFrame(duplicated_emails, columns=['email'])
    
# Data for the DataFrame
data = {
    "id": [1, 2, 3],
    "email": ["a@b.com", "c@d.com", "a@b.com"]
}

# Creating the DataFrame
df = pd.DataFrame(data)

# Displaying the DataFrame
print(duplicate_emails(df))
