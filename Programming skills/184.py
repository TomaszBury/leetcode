import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    department.rename(columns={"name":"Department"}, inplace=True)
    employee.rename(columns={"name":"Employee", "salary":"Salary"}, inplace=True)
    employee_department_df:pd.DataFrame = pd.merge(employee, department, left_on="departmentId", right_on="id", how="left")

    if len(employee_department_df) == 0:
        return pd.DataFrame({ "Department": [], "Employee": [], "Salary": [] })

    departments:list[str] = employee_department_df.loc[:,"Department"].unique().tolist()
    
    result_df:pd.DataFrame = pd.DataFrame()

    for department in departments:
        mask_department = (employee_department_df.loc[:,"Department"] == department)
        max_salary:int = int(employee_department_df.loc[mask_department,["Salary"]].max().item())
        mask_salary_department = (employee_department_df.loc[:,"Department"] == department) & (employee_department_df.loc[:,"Salary"] == max_salary)

        result_df = pd.concat([result_df, employee_department_df.loc[mask_salary_department,:]])

    return result_df.loc[:,["Department", "Employee",  "Salary"]]

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
employee_data = { 'id': [1, 2, 3, 4, 5], 'name': ['Joe', 'Jim', 'Henry', 'Sam', 'Max'], 'salary': [70000, 90000, 80000, 60000, 90000], 'departmentId': [1, 1, 2, 2, 1] } 
employee_df = pd.DataFrame(employee_data) 

department_data = { 'id': [1, 2], 'name': ['IT', 'Sales'] } 
department_df = pd.DataFrame(department_data)

print(department_highest_salary(employee_df,department_df))

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
employee_data = data = { "id": [1, 2, 4], "name": ["Joe", "Sam", "Max"], "salary": [60000, 50000, 50000], "departmentId": [1, 1, 2] }
employee_df = pd.DataFrame(employee_data) 


data = { "Department": ["IT", "Sales", "IT"], "Employee": ["Jim", "Henry", "Max"], "Salary": [90000, 80000, 90000] }

df = pd.DataFrame(data)
print(df)

print("________________________________________________________________________________________________________________________________________________________________")
print(department_highest_salary(employee_df,department_df))
print("________________________________________________________________________________________________________________________________________________________________")
data = {
    "Department": ["IT", "HR"],
    "Employee": ["Joe", "Max"],
    "Salary": [60000, 50000]
}
df = pd.DataFrame(data)
print(df)

print("---------------------------------------------------------------------------------------------------------------------------------------------------------------------")
employee_data = { 'id': [], 'name': [], 'salary': [], 'departmentId': [] } 
employee_df = pd.DataFrame(employee_data) 

department_data = { 'id': [], 'name': [] } 
department_df = pd.DataFrame(department_data)

print(department_highest_salary(employee_df,department_df))