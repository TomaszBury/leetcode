import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask_employee = (employees.loc[:,"employee_id"] % 2 == 1) & ~(employees.loc[:,"name"].str.startswith("M"))
    employees.loc[mask_employee,"bonus"] = employees.loc[mask_employee,"salary"]
    employees.fillna(0.0, inplace=True)
    employees.sort_values(by="employee_id",inplace=True)
    print(employees.loc[:,["employee_id","bonus"]])
    # print(employees.dtypes)
    return employees

data_input = { 'employee_id': [2, 3, 7, 8, 9], 'name': ['Meir', 'Michael', 'Addilyn', 'Juan', 'Kannon'], 'salary': [3000, 3800, 7400, 6100, 7700] } 
# Creating DataFrame 
df_input = pd.DataFrame(data_input)

data_output = { 'employee_id': [2, 3, 7, 8, 9], 'bonus': [0, 0, 7400, 0, 7700] } 
# Creating DataFrame 
df_output = pd.DataFrame(data_output)
print(df_output)
print(df_output.dtypes)

assert calculate_special_bonus(df_input).equals(df_output)