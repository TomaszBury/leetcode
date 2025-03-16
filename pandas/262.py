import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    mask_data:pd.Series = (trips.loc[:,"request_at"] != "2013-10-04")

    mask_banned:pd.Series = (users.loc[:,"banned"] == "No")
    users_not_banned:pd.DataFrame = users.loc[mask_banned,:]
    trips_data:pd.DataFrame = trips.loc[mask_data,:]
    return_df:pd.DataFrame = pd.merge(left=trips_dataf, right=users_not_banned, left_on=["client_id"], right_on=["users_id"], how="inner")
    return_df:pd.DataFrame = pd.merge(left=return_df, right=users_not_banned, left_on=["driver_id"], right_on=["users_id"])

    mask_cancelled_by_client:pd.Series = (return_df.loc[:,"status"] != "completed")
    cancelled_by_client:pd.DataFrame = return_df.loc[mask_cancelled_by_client,:].groupby("request_at")["status"].count().reindex(return_df['request_at'].unique(), fill_value=0).reset_index()
    

    group_by:pd.DataFrame = return_df.groupby("request_at")["status"].count()

    day_ratio:pd.DataFrame = pd.merge(left=group_by, right=cancelled_by_client, on=["request_at"], how="left")

    day_ratio.loc[:,"Cancellation Rate"] = round(day_ratio.loc[:,"status_y"] / day_ratio.loc[:,"status_x"],2)

    mask_status_y:pd.Series = (day_ratio.loc[:,"status_y"] == 0) & (day_ratio.loc[:,"status_x"] == 1)
    day_ratio.loc[mask_status_y,"Cancellation Rate"] = 0

    day_ratio.rename(columns={"request_at":"Day"}, inplace=True)

    return day_ratio.loc[:,["Day","Cancellation Rate"]]
    # return return_df
print("-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=")
trips_data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'client_id': [1, 2, 3, 4, 1, 2, 3, 2, 3, 4],
    'driver_id': [10, 11, 12, 13, 10, 11, 12, 12, 10, 13],
    'city_id': [1, 1, 6, 6, 1, 6, 6, 12, 12, 12],
    'status': ['completed', 'cancelled_by_driver', 'completed', 'cancelled_by_client',
               'completed', 'completed', 'completed', 'completed', 'completed',
               'cancelled_by_driver'],
    'request_at': ['2013-10-01', '2013-10-01', '2013-10-01', '2013-10-01',
                  '2013-10-02', '2013-10-02', '2013-10-02', '2013-10-03',
                  '2013-10-03', '2013-10-03']
}
trips_df = pd.DataFrame(trips_data)

# Create Users DataFrame
users_data = {
    'users_id': [1, 2, 3, 4, 10, 11, 12, 13],
    'banned': ['No', 'Yes', 'No', 'No', 'No', 'No', 'No', 'No'],
    'role': ['client', 'client', 'client', 'client', 'driver', 'driver', 'driver', 'driver']
}
users_df = pd.DataFrame(users_data)

# print(trips_and_users(trips_df,users_df))

trips = pd.DataFrame({
    'id': [1],
    'client_id': [1],
    'driver_id': [10],
    'city_id': [1],
    'status': ['cancelled_by_client'],
    'request_at': ['2013-10-04']
})

# Create the 'Users' DataFrame
users = pd.DataFrame({
    'users_id': [1, 10],
    'banned': ['No', 'No'],
    'role': ['client', 'driver']
})

# print(trips_and_users(trips,users))

trips = pd.DataFrame({
    'id': [1111],
    'client_id': [1],
    'driver_id': [10],
    'city_id': [1],
    'status': ['completed'],
    'request_at': ['2013-10-01']
})

# Create the 'Users' DataFrame
users = pd.DataFrame({
    'users_id': [1, 10],
    'banned': ['No', 'No'],
    'role': ['client', 'driver']
})

print(trips_and_users(trips, users))

trips = pd.DataFrame({
    'id': [1111],
    'client_id': [1],
    'driver_id': [10],
    'city_id': [1],
    'status': ['completed'],
    'request_at': ['2013-10-01']
})

# Create the 'Users' DataFrame
users = pd.DataFrame({
    'users_id': [1, 10],
    'banned': ['No', 'Yes'],
    'role': ['client', 'driver']
})

print(trips_and_users(trips, users))

# Create Trips dataframe
trips_data = {
    'id': [1],
    'client_id': [1],
    'driver_id': [10],
    'city_id': [1],
    'status': ['cancelled_by_client'],
    'request_at': ['2013-10-04']
}

trips = pd.DataFrame(trips_data)

# Create Users dataframe
users_data = {
    'users_id': [1, 10],
    'banned': ['No', 'No'],
    'role': ['client', 'driver']
}

users = pd.DataFrame(users_data)

print(trips_and_users(trips,users))