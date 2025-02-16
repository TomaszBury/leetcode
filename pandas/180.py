import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    len_df:int = len(logs)

    if len_df < 3:
        return pd.DataFrame({
                'ConsecutiveNums': []
                })
    list_consecutive_numbers:list[int] = []
    for i in range(len_df-2):
        # print(logs.iloc[i,[1]])
        # print(logs.iloc[i+1,[1]])
        # print(logs.iloc[i+2,[1]])
        three:bool = int(logs.iloc[i,[1]]) == int(logs.iloc[i+1,[1]]) == int(logs.iloc[i+2,[1]])
        # print(three)
        if three:
            list_consecutive_numbers.append(int(logs.iloc[i,[1]]))
        
    return pd.DataFrame({
                'ConsecutiveNums': list(set(list_consecutive_numbers))
                })



# Data for Logs table
logs_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8],
    'num': [1, 1, 1, 2, 1, 2, 2,999]
}

# Create DataFrame
logs_df = pd.DataFrame(logs_data)

print(consecutive_numbers(logs_df))

# Data for the DataFrame
data = {
    'id': [1, 2, 3],
    'num': [1, 1, 1]
}

# Create the DataFrame
df = pd.DataFrame(data)

print(consecutive_numbers(df))

# Data for the DataFrame
logs_data = {
    'id': [1, 2, 3, 4],
    'num': [3, 3, 3, 3]
}

# Create the DataFrame
logs_df = pd.DataFrame(logs_data)

print(consecutive_numbers(logs_df))