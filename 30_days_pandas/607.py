import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # # Merge Orders with SalesPerson (using sales_id)
    # merged_df = orders_df.merge(salesperson_df, on='sales_id', how='outer')

    # # Merge Orders with Company (using com_id)
    # merged_df = orders_df.merge(company_df, on='com_id', how='outer')

    # Merge all three DataFrames
    combined_df = (orders_df
                .merge(salesperson_df, on='sales_id', how='outer')
                .merge(company_df, on='com_id', how='outer'))
    
    # mask_name_company = combined_df.loc[:,"name_y"] != "RED"
    
    # return combined_df.loc[mask_name_company,["name_x"]]
    return combined_df


# Create SalesPerson DataFrame
salesperson_data = {
    'sales_id': [1, 2, 3, 4, 5],
    'name': ['John', 'Amy', 'Mark', 'Pam', 'Alex'],
    'salary': [100000, 12000, 65000, 25000, 5000],
    'commission_rate': [6, 5, 12, 25, 10],
    'hire_date': ['4/1/2006', '5/1/2010', '12/25/2008', '1/1/2005', '2/3/2007']
}
salesperson_df = pd.DataFrame(salesperson_data)

# Create Company DataFrame
company_data = {
    'com_id': [1, 2, 3, 4],
    'name': ['RED', 'ORANGE', 'YELLOW', 'GREEN'],
    'city': ['Boston', 'New York', 'Boston', 'Austin']
}
company_df = pd.DataFrame(company_data)

# Create Orders DataFrame
orders_data = {
    'order_id': [1, 2, 3, 4],
    'order_date': ['1/1/2014', '2/1/2014', '3/1/2014', '4/1/2014'],
    'com_id': [3, 4, 1, 1],
    'sales_id': [4, 5, 1, 4],
    'amount': [10000, 5000, 50000, 25000]
}
orders_df = pd.DataFrame(orders_data)

print(sales_person(salesperson_df, company_df, orders_df))