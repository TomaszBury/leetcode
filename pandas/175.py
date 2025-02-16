import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    
    return pd.merge(person, address, on='personId', how='left').loc[:,["firstName","lastName","city","state"]]



#Create Person table
person_data = {
    'personId': [1, 2],
    'lastName': ['Wang', 'Alice'],
    'firstName': ['Allen', 'Bob']
}

person_df = pd.DataFrame(person_data)

# Create Address table
address_data = {
    'addressId': [1, 2],
    'personId': [2, 3],
    'city': ['New York City', 'Leetcode'],
    'state': ['New York', 'California']
}

address_df = pd.DataFrame(address_data)


print(combine_two_tables(person_data, address_data))