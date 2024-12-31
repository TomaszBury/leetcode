
import pandas as pd

def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    mask_weight = animals.loc[:,"weight"] > 100
    animals = animals.sort_values(ascending=False, by="weight")
    return pd.DataFrame(animals.loc[mask_weight,"name"])
    