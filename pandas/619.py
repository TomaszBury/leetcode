import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
    my_numbers.loc[:,"count"] = my_numbers.loc[:,"num"].map(my_numbers.loc[:,"num"].value_counts())

    mask_count:pd.Series = (my_numbers.loc[:,"count"] == 1)
    if mask_count.any():
        result_df:pd.DataFrame = my_numbers.loc[mask_count,:].sort_values(by=["num"],ascending=False)
        return result_df.iloc[[0],[0]]
    else:
        return pd.DataFrame({"num":[None]})


df = pd.DataFrame({
    'num': [8, 8, 3, 3, 1, 4, 5, 6]
})

print(biggest_single_number(df))