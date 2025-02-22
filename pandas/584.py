
import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    customer.loc[:,"referee_id"] = customer.loc[:,"referee_id"].fillna(0).astype(int)
    mask_customer_is_not_2:pd.Series = (customer.loc[:,"referee_id"] != 2)
    return customer.loc[mask_customer_is_not_2,["name"]]

# Create the DataFrame
data = {
    'id': [1, 2, 3, 4, 5, 6],
    'name': ['Will', 'Jane', 'Alex', 'Bill', 'Zack', 'Mark'],
    'referee_id': [None, None, 2, None, 1, 2]
}

customer_df = pd.DataFrame(data)

print(find_customer_referee(customer_df))