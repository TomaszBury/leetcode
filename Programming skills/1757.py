import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask_low_fats_recyclable = (products.loc[:,"low_fats"] == "Y") & (products.loc[:,"recyclable"] == "Y")
    return pd.DataFrame(products.loc[mask_low_fats_recyclable,"product_id"])
    