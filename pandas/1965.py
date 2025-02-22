import pandas as pd

def find_employees(employees: pd.DataFrame, salaries: pd.DataFrame) -> pd.DataFrame:

    employees_with_salaries:pd.DataFrame = pd.merge(employees, salaries, on="employee_id", how="outer")

    mask_employees_salary_name_missing:pd.Series = (employees_with_salaries.loc[:,"salary"].isna()) | (employees_with_salaries.loc[:,"name"].isna())
    
    return employees_with_salaries.loc[mask_employees_salary_name_missing,["employee_id"]]

# First set of DataFrames (complete data)
employees = pd.DataFrame({
    'employee_id': [2, 4, 5],
    'name': ['Crew', 'Haven', 'Kristian']
})

salaries = pd.DataFrame({
    'employee_id': [5, 1, 4],
    'salary': [76071, 22517, 63539]
})

print(find_employees(employees, salaries))

# Second set of DataFrames (with missing data)
employees_missing = pd.DataFrame({
    'employee_id': [2, 4, 5],
    'name': ['Crew', None, 'Kristian']  # Haven's name is missing
})

salaries_missing = pd.DataFrame({
    'employee_id': [5, 1, 4],
    'salary': [76071, None, 63539]  # Salary for employee_id 1 is missing
})

print(find_employees(employees_missing, salaries_missing))