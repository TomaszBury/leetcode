import pandas as pd
import numpy as np

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if len(employee) >= N and len(employee.loc[:,'salary'].drop_duplicates()) >= N and N > 0:
        employee.sort_values(by='salary', ascending=False, inplace=True)
        unique_salaries = employee.drop_duplicates(subset=["salary"])
        unique_salaries.reset_index(inplace=True, drop=True)
        df_return = unique_salaries.loc[[N - 1],["salary"]].rename(columns={"salary":f"getNthHighestSalary({N})"})
        return df_return
    else:
        return pd.DataFrame({ f'getNthHighestSalary({N})': [np.nan] } )

print("----------------------------------------------------------------------")

data = { 'id': [1, 2, 3], 'salary': [100, 200, 300] } 
df = pd.DataFrame(data)
print(nth_highest_salary(df, 2))

data_input = { 'id': [1], 'salary': [100] }
df_input = pd.DataFrame(data_input)
print(nth_highest_salary(df_input, 2))


new_data = { 'id': [4, 5], 'salary': [400, 500] } 
new_df = pd.DataFrame(new_data)
print(nth_highest_salary(new_df, 2))

data_new = { 'id': [1, 2], 'salary': [100, 100] }
df_new = pd.DataFrame(data_new)
print(df_new)
print(nth_highest_salary(df_new, 2))

data_new = data = { 'id': [12, 6, 87, 1, 39, 65, 25, 96, 8, 11, 5, 18, 66, 26, 82, 63, 64, 73, 2, 78, 22, 77, 69, 32, 79, 23, 43, 44, 28, 86, 57, 13, 62, 72, 37, 89, 71, 46, 95, 48, 17, 20, 74, 54, 35, 84, 42, 76, 45, 68, 40, 14, 51, 97, 30, 88, 55, 81, 7, 52, 33, 41, 50, 24, 59, 99, 67, 61, 38, 94, 15, 70, 10, 49, 29, 60, 3, 0, 75, 83, 47, 9, 56, 80, 27, 21, 85, 91, 90, 58, 19, 4, 92, 16, 36, 53, 93, 31, 34, 98], 'salary': [761, 1037, 38, 786, 1762, 133, 2529, 403, 4333, 3164, 831, 3579, 4778, 4826, 4957, 1288, 2711, 1842, 2627, 1908, 4667, 199, 576, 2638, 510, 622, 2491, 4435, 4552, 4646, 451, 1852, 2835, 544, 2896, 4699, 220, 2333, 2261, 3210, 398, 57, 176, 4272, 2172, 4686, 2595, 3631, 4022, 3248, 571, 4094, 3272, 2057, 2505, 3805, 4926, 3423, 811, 4664, 1842, 4645, 1490, 3361, 4504, 805, 4561, 4641, 2542, 4361, 1652, 1903, 2109, 1428, 558, 708, 1717, 3162, 1450, 2333, 455, 2360, 1570, 1677, 508, 3994, 2276, 1606, 2269, 1954, 774, 655, 3274, 333, 1744, 2262, 3887, 3521, 1415, 2490] }
df_new = pd.DataFrame(data_new)
# print(df_new)
print(nth_highest_salary(df_new, 88))

data = { 'id': [1, 2, 3], 'salary': [100, 200, 300] }
df_new = pd.DataFrame(data)
# print(df_new)
print(nth_highest_salary(df_new, -1))