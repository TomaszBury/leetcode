import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    return customers


data_customers = { 'id': [1, 2, 3, 4], 'name': ['Joe', 'Henry', 'Sam', 'Max'] }
# Create the dictionary 
data_customers = dict(data_customers)
df_customers = pd.DataFrame(data_customers)
df_customers.set_index("id", inplace=True)

data = { 'id': [1, 2], 'customerId': [3, 1] } 
# Create the DataFrame 
df_orders = pd.DataFrame(data)
df_orders.set_index("id", inplace=True)

# print(df_customers)
# print(df_orders)

joined_df = pd.merge(df_customers, df_orders, left_on="id", right_on="customerId", how="outer")
# print("\nJoined DataFrame:") 
# print(joined_df)
mask_NaN = joined_df.loc[:,"customerId"].isna()


# print("\nJoined DataFrame:") 
# print(joined_df.loc[mask_NaN,:])
result_df = joined_df.loc[mask_NaN,:]

result_df = result_df.rename(columns={"name":"Customers"})
print(result_df.loc[:,"Customers"])
