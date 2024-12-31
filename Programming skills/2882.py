import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    customers.drop_duplicates(subset="email",keep="first",inplace=True,ignore_index=True)
    return customers

data_input = {
    'customer_id': [1, 2, 3, 4, 5, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Finn', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'john@example.com', 'alice@example.com']
}

# Create the DataFrame
df_input = pd.DataFrame(data_input)

data_output = {
    'customer_id': [1, 2, 3, 4, 6],
    'name': ['Ella', 'David', 'Zachary', 'Alice', 'Violet'],
    'email': ['emily@example.com', 'michael@example.com', 'sarah@example.com', 'john@example.com', 'alice@example.com']
}

# Create the DataFrame
df_output = pd.DataFrame(data_output)

assert dropDuplicateEmails(df_input).equals(df_output)

print(dropDuplicateEmails(df_input))
print(df_output)