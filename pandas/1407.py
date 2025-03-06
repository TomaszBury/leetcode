import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    return_df:pd.DataFrame = pd.merge(left=users, right=rides, left_on=["id"], right_on=["user_id"],how='left')
    return_df = return_df.fillna(0)
     
    distance_by_name = return_df.groupby(['id_x',"name"])['distance'].sum().reset_index()
    # return distance_by_name
    return distance_by_name.sort_values(by=["distance","name"],ascending=[False,True]).rename(columns={"distance":"travelled_distance"}).loc[:,["name","travelled_distance"]]



users_data = {
    'id': [1, 2, 3, 4, 7, 13, 19],
    'name': ['Alice', 'Bob', 'Alex', 'Donald', 'Lee', 'Jonathan', 'Elvis']
}
users_df = pd.DataFrame(users_data)

# Create Rides dataframe
rides_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'user_id': [1, 2, 3, 7, 13, 19, 7, 19, 7],
    'distance': [120, 317, 222, 100, 312, 50, 120, 400, 230]
}
rides_df = pd.DataFrame(rides_data)

print(top_travellers(users_df, rides_df))

users_data = {
    'id': [1, 2, 3, 19],
    'name': ['Alice', 'Bob', 'Alex', 'Alice']
}
users_df = pd.DataFrame(users_data)

rides_data = {
    'id': [1, 2, 3, 4, 5, 9],
    'user_id': [1, 2, 3, 7, 13, 7],
    'distance': [120, 317, 222, 100, 312, 230]
}
rides_df = pd.DataFrame(rides_data)

print(top_travellers(users_df, rides_df))