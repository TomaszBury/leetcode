import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:

    mask_low_salary = (accounts.loc[:,"income"] < 20_000)
    mask_average_salary = (accounts.loc[:,"income"] >= 20_000) & (accounts.loc[:,"income"] <= 50_000)
    mask_high_salary = (accounts.loc[:,"income"] > 50_000)

    low_salary:int = len(accounts.loc[mask_low_salary,"income"])
    average_salary:int = len(accounts.loc[mask_average_salary,"income"])
    high_salary:int = len(accounts.loc[mask_high_salary,"income"])


    categories = {
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count":[low_salary,average_salary,high_salary]

    }
    result_df = pd.DataFrame(categories)
    
    return result_df



data = {
    'account_id': [3, 2, 8, 6],
    'income': [108939, 12747, 87709, 91796]
}

# Create DataFrame
df = pd.DataFrame(data)

print(count_salary_categories(df))