import pandas as pd

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:

    employees_bonus:pd.DataFrame = pd.merge(employee, bonus, on="empId", how="left")
    bonus_lt_1000:pd.Series = (employees_bonus.loc[:,"bonus"] < 1000) | (employees_bonus.loc[:,"bonus"].isna())


    return employees_bonus.loc[bonus_lt_1000,["name","bonus"]]

    # return employee.loc[mask_employee,:]

# Create Employee DataFrame
employee_data = {
    'empId': [3, 1, 2, 4],
    'name': ['Brad', 'John', 'Dan', 'Thomas'],
    'supervisor': [None, 3, 3, 3],
    'salary': [4000, 1000, 2000, 4000]
}
employee_df = pd.DataFrame(employee_data)

# Create Bonus DataFrame
bonus_data = {
    'empId': [2, 4],
    'bonus': [500, 2000]
}
bonus_df = pd.DataFrame(bonus_data)

print(employee_bonus(employee_df, bonus_df))


# Create empty Employee DataFrame
empty_employee_data = {
    'empId': [],
    'name': [],
    'supervisor': [],
    'salary': []
}
empty_employee_df = pd.DataFrame(empty_employee_data)

# Create empty Bonus DataFrame
empty_bonus_data = {
    'empId': [],
    'bonus': []
}
empty_bonus_df = pd.DataFrame(empty_bonus_data)

print(employee_bonus(empty_employee_df, empty_bonus_df))
