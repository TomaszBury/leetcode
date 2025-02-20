import pandas as pd
from datetime import datetime

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    sorted_df = weather.sort_values('recordDate', ascending=True).reset_index(drop=True)

    # print(sorted_df)

    ids_temperatures:dict[str,str] = {"id":[]}

    if len(sorted_df) < 2:
        return pd.DataFrame(ids_temperatures)
    
    for index in sorted_df.index:
        if index < len(sorted_df)-1:
            date_str1 = sorted_df.iloc[index,1]
            date_str2 = sorted_df.iloc[index+1,1]
            date1 = datetime.strptime(date_str1, '%Y-%m-%d')
            date2 = datetime.strptime(date_str2, '%Y-%m-%d')

            print(f"len:{len(sorted_df)} index:{index} day:{sorted_df.iloc[index,1]} tomorow:{sorted_df.iloc[index+1,1]} delta:{(date1 - date2).days}")

            if (date1 - date2).days == -1: 
                temperature_today = sorted_df.iloc[index,2]
                temperature_tomorow = sorted_df.iloc[index+1,2]
                if temperature_today < temperature_tomorow:
                    ids_temperatures["id"].extend([sorted_df.iloc[index+1,0]])

    return pd.DataFrame(ids_temperatures)

# Create the data dictionary
data = {
    'id': [1, 2, 3, 4],
    'recordDate': ['2015-01-01', '2015-01-02', '2015-01-03', '2015-01-04'],
    'temperature': [10, 25, 20, 30]
}

# Create DataFrame
weather_df = pd.DataFrame(data)

print(rising_temperature(weather_df))

# 2,4
# Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).
# Return the result table in any order.
# The result format is in the following example.

data = {
    'id': [1, 2],
    'recordDate': ['2000-12-16', '2000-12-15'],
    'temperature': [3, -1]
}

# Create DataFrame
weather_df = pd.DataFrame(data)

print(rising_temperature(weather_df))

data = {
    'id': [1, 2],
    'recordDate': ['2000-12-14', '2000-12-16'],
    'temperature': [3, 5]
}

# Create DataFrame
weather_df = pd.DataFrame(data)

print(rising_temperature(weather_df))

