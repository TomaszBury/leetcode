import pandas as pd
# import numpy as np

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    if len(orders) < 1:
        return pd.DataFrame({"customer_number":[]})
    sorted_orders = orders.groupby(["customer_number"])[["customer_number"]].count().reset_index(names='custom_name').sort_values(by=["customer_number"] ,ascending=False).iloc[[0],[0]].rename(columns={"custom_name":"customer_number"})
    return sorted_orders


df = pd.DataFrame({
    'order_number': [1, 2, 3, 4],
    'customer_number': [1, 2, 3, 3]
})

print(largest_orders(df))