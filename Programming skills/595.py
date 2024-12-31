import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    mask_big_coutries = (world.loc[:,"area"] >= 3_000_000) | (world.loc[:,"population"] >= 25_000_000)
    return world.loc[mask_big_coutries,["name","population","area"]]

    