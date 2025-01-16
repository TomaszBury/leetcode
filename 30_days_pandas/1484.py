import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    grouped = activities.groupby('sell_date')['product'].agg([
        ('num_sold', 'nunique'),
        ('products', lambda x: ','.join(sorted(x.unique())))
    ]).reset_index()

    grouped['products'] = grouped['products'].str.split(',').apply(lambda x: ','.join(sorted(x)))

    result = grouped.sort_values('sell_date')

    return result

data = {
    'sell_date': ['2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30', '2020-06-01', '2020-06-02', '2020-05-30'],
    'product': ['Headphone', 'Pencil', 'Mask', 'Basketball', 'Bible', 'Mask', 'T-Shirt']
}

df = pd.DataFrame(data)

print(categorize_products(df))