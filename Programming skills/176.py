import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    N =2
    if len(employee) >= N and len(employee.loc[:,'salary'].drop_duplicates()) >= N and N > 0:
        employee.sort_values(by='salary', ascending=False, inplace=True)
        unique_salaries = employee.drop_duplicates(subset=["salary"])
        unique_salaries.reset_index(inplace=True, drop=True)
        df_return = unique_salaries.loc[[N - 1],["salary"]].rename(columns={"salary":f"SecondHighestSalary"})
        return df_return
    else:
        return pd.DataFrame({ f'SecondHighestSalary': [np.nan] } )
    