import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:

    # Merge the dataframes to link employees with their departments
    df_merged = pd.merge(employee, department, left_on='departmentId', right_on='id', suffixes=('', '_dept'))

    # Group by department and rank salaries in descending order
    df_ranked = df_merged.groupby('name_dept').apply(lambda x: x.sort_values('salary', ascending=False)).reset_index(drop=True)

    # Use rank to get the top 3 unique salaries per department
    df_ranked['rank'] = df_ranked.groupby('name_dept')['salary'].rank(method='dense', ascending=False)

    # Filter to get only top 3 ranks (where rank <= 3)
    high_earners = df_ranked[df_ranked['rank'] <= 3][['name_dept', 'name', 'salary']]

    # Rename columns for clarity
    high_earners.columns = ['Department', 'Employee', 'Salary']

    # Sort for better readability (optional, as order doesn't matter)
    high_earners = high_earners.sort_values(by=['Department', 'Salary'], ascending=[True, False])

    # If you want the result as a list of dictionaries (e.g., for further processing)
    result = high_earners.to_dict(orient='records')
    if not result:
        return pd.DataFrame({"Department":[], "Employee":[], "Salary":[]})
    return pd.DataFrame(result)


# Sample data (matching the SQL example)
employees = [
    {"id": 1, "name": "Joe", "salary": 85000, "departmentId": 1},
    {"id": 2, "name": "Henry", "salary": 80000, "departmentId": 2},
    {"id": 3, "name": "Sam", "salary": 60000, "departmentId": 2},
    {"id": 4, "name": "Max", "salary": 90000, "departmentId": 1},
    {"id": 5, "name": "Janet", "salary": 69000, "departmentId": 1},
    {"id": 6, "name": "Randy", "salary": 85000, "departmentId": 1},
    {"id": 7, "name": "Will", "salary": 70000, "departmentId": 1}
]

departments = [
    {"id": 1, "name": "IT"},
    {"id": 2, "name": "Sales"}
]

# Convert to pandas DataFrames
df_employees = pd.DataFrame(employees)
df_departments = pd.DataFrame(departments)

print(top_three_salaries(df_employees,df_departments))