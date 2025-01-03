import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns={"name":"Department"}, inplace=True)
    employee.rename(columns={"name":"Employee", "salary":"Salary"}, inplace=True)
    result_df:pd.DataFrame = pd.merge(employee, department, left_on="departmentId", right_on="id", how="outer")
    
    # max_salaries = result_df.groupby(['Employee', 'Department'])['Salary'].idxmax()
    print(f"\n-----------------------------------")
    max_salary = result_df.groupby(['Department','Employee'])['Salary'].max(numeric_only=True)
    # max_salary = max_salary.drop_duplicates(keep='first')
    # print(f"max salaries:\n{max_salary}")

    max_salaries_per_dept = employee.groupby('departmentId')['Salary'].max().reset_index()
    max_salaries = employee.groupby('departmentId')['Salary'].max().reset_index()['Salary'].to_list()
    max_name = employee.groupby('departmentId')['Employee'].max().reset_index()['Employee'].to_list()
    max_dept:pd.DataFrame = pd.merge(max_salaries_per_dept, department, left_on="departmentId", right_on="id", how="left")["Department"].to_list()
    print(f"\n-----------------------------------")
    mask_highest_salary = (result_df.loc[:,"Salary"].isin(max_salaries)) & (result_df.loc[:,"Department"].isin(max_dept)) & (result_df.loc[:,"Employee"].isin(max_name))
    print(employee.groupby(['departmentId',"Employee"])['Salary'].max())
    print(f"\n-----------------------------------")

    # mask_max_salaries = result_df.loc[:,["Salary"]] == max_salaries
    
    # return result_df.loc[mask_max_salaries,['Department','Employee', 'Salary']]
    return result_df.loc[mask_highest_salary,['Department','Employee','Salary']]

employee_data = { 'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': [70000, 90000, 80000, 60000, 90000], 'departmentId': [1, 1, 2, 2, 1] } 
employee_df = pd.DataFrame(employee_data) 

department_data = { 'id': [1, 2], 'name': ['IT', 'Sales'] } 
department_df = pd.DataFrame(department_data)

print(department_highest_salary(employee_df,department_df))