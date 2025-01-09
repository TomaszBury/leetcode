import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees.loc[:,"out_time"] - employees.loc[:,"in_time"]
    result_df = employees.groupby(["event_day","emp_id"])[["total_time"]].sum().reset_index()
    result_df.rename(columns={"event_day":"day"}, inplace=True)
    return result_df


data = {
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
}

df = pd.DataFrame(data)

print(total_time(df))