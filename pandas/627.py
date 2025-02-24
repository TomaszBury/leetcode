import pandas as pd

def swap_salary(salary: pd.DataFrame) -> pd.DataFrame:
    mask_f:pd.Series = (salary.loc[:,"sex"] == "f")
    mask_m:pd.Series = (salary.loc[:,"sex"] == "m")

    salary_f:pd.DataFrame = salary.loc[mask_f,:]
    salary_f.loc[:,"sex"] = "m"
    salary_m:pd.DataFrame = salary.loc[mask_m,:]
    salary_m.loc[:,"sex"] = "m"

    
    return pd.concat([salary_f,salary_m])

salary_df = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['A', 'B', 'C', 'D'],
    'sex': ['m', 'f', 'm', 'f'],
    'salary': [2500, 1500, 5500, 500]
})

print(swap_salary(salary_df))