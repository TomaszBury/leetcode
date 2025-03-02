import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:

    sales_return:pd.DataFrame = pd.merge(sales, product, on=["product_id"])
    
    return sales_return.loc[:,["product_name","year","price"]]

# Create Sales DataFrame
sales_data = {
    'sale_id': [1, 2, 7],
    'product_id': [100, 100, 200],
    'year': [2008, 2009, 2011],
    'quantity': [10, 12, 15],
    'price': [5000, 5000, 9000]
}
sales_df = pd.DataFrame(sales_data)

# Create Product DataFrame
product_data = {
    'product_id': [100, 200, 300],
    'product_name': ['Nokia', 'Apple', 'Samsung']
}
product_df = pd.DataFrame(product_data)

print(sales_analysis(sales_df,product_df))