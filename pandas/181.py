import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee_names:list[str] = []
    employees = employee[employee['managerId'].notna()]
    for salary_employee, managersId, employee_name in employees.loc[:,["salary","managerId","name"]].values:
        mask_manager = (employee.loc[:,"id"] == managersId)
        if mask_manager.any():
            manager_salary:float = float(employee.loc[mask_manager,"salary"].iloc[0])
            if salary_employee > manager_salary:
                employee_names.append(employee_name)
    return pd.DataFrame({"Employee":employee_names})
    



data = {
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max'],
    'salary': [70000, 80000, 60000, 90000],
    'managerId': [3, 4, None, None]  # Use None for SQL NULL values in Python
}

df = pd.DataFrame(data)

print(find_employees(df))