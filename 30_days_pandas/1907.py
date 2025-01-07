import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    categories = {
        "Low Salary": 0,
        "Average Salary": 0,
        "High Salary": 0
    }

    for account in accounts:
        print(f"\nincome:{type(account)} account:{account}")
        # income:int = int(account["income"])
        # if income < 20000:
        #     categories["Low Salary"] += 1
        # elif 20000 <= income <= 50000:
        #     categories["Average Salary"] += 1
        # else:  # income > 50000
        #     categories["High Salary"] += 1

    # Here we format the results into the desired output structure
    result = []
    for category, count in categories.items():
        result.append({
            "category": category,
            "accounts_count": count
        })
    
    return result



data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}

# Create DataFrame
df = pd.DataFrame(data)

print(count_salary_categories(df))