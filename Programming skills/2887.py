import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products.loc[:,"quantity"] = products.loc[:,"quantity"].fillna(0)
    return products

data_input = { 'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'], 'quantity': [None, None, 779, 849], 'price': [135, 821, 9319, 3051] } 
data_output = { 'name': ['Wristwatch', 'WirelessEarbuds', 'GolfClubs', 'Printer'], 'quantity': [0.0, 0.0, 779, 849], 'price': [135, 821, 9319, 3051] }
# Create the DataFrame 
df_input = pd.DataFrame(data_input)
df_output = pd.DataFrame(data_output)

assert  fillMissingValues(df_input).equals(df_output)