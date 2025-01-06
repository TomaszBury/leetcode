import pandas as pd
"""
Made with LLM.
"""
def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    df_melted = pd.melt(products, id_vars=['product_id'], 
                    value_vars=['store1', 'store2', 'store3'], 
                    var_name='store', 
                    value_name='price')

    # Remove rows where price is null since the product is not available in that store
    df_melted = df_melted.dropna(subset=['price'])

    # Sort by product_id and then by the order of stores for clarity (optional)
    df_melted = df_melted.sort_values(['product_id', 'store'])
    return df_melted
    