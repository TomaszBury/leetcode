import pandas as pd
import numpy as np

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(employees, employee_uni, on="id", how="left")

    result = result.drop("id", axis=1)

    # result["unique_id"] = result['unique_id'].where(result['unique_id'].notna(), np.null)÷

    result = result[['unique_id', 'name']]

    return result


employees = pd.DataFrame({
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
})

# EmployeeUNI DataFrame
employee_UNI = pd.DataFrame({
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
})

print(replace_employee_id(employees, employee_UNI))