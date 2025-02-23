import pandas as pd

def find_employees(employees: pd.DataFrame) -> pd.DataFrame:

    mask_menager:pd.Series = employees.loc[:,"manager_id"].isin(employees.loc[:,"employee_id"])

    result_df:pd.DataFrame = employees.loc[:,["employee_id","name","manager_id","salary"]].assign(manager_is_employed=mask_menager)

    mask_salary:pd.Series = (result_df.loc[:,"salary"] < 30_000) & (result_df.loc[:,"manager_is_employed"] == False) & (result_df.loc[:,"manager_id"].notnull())
    
    result_sorted:pd.DataFrame = result_df.loc[mask_salary,["employee_id"]].sort_values(by=["employee_id"],ascending=True)
    
    return result_sorted
    # return employees.loc[mask_menager,:]

employees = pd.DataFrame({
    'employee_id': [3, 12, 13, 1, 9, 11],
    'name': ['Mila', 'Antonella', 'Emery', 'Kalel', 'Mikaela', 'Joziah'],
    'manager_id': [9, None, None, 11, None, 6],
    'salary': [60301, 31000, 67084, 21241, 50937, 28485]
})


# print(find_employees(employees))


employees = pd.DataFrame({
    'employee_id': [18, 20, 10, 13, 17, 21, 7, 9, 2, 8, 11, 3, 14, 19],
    'name': ['Drew', 'Ronan', 'Jaxton', 'Louie', 'Mylah', 'Kenia', 'Hadley', 
             'Hayden', 'Nixon', 'Arthur', 'Brycen', 'Noemi', 'Hayden', 'Astrid'],
    'manager_id': [None, 3, 15, 16, 20, 15, 6, 4, None, 11, None, None, None, 20],
    'salary': [41568, 65209, 96667, 6801, 26540, 98690, 23590, 90798, 
               25560, 67027, 42570, 87321, 4123, 37680]
})

print(find_employees(employees))