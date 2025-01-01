import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask_tweet_len = (tweets.loc[:,"content"].str.len() > 15)
    print(pd.DataFrame(tweets.loc[mask_tweet_len,"tweet_id"]).reset_index(drop=True))
    return pd.DataFrame(tweets.loc[mask_tweet_len,"tweet_id"].reset_index(drop=True))

data_input = { 'tweet_id': [1, 2], 'content': ['Let us Code', 'More than fifteen chars are here!'] } 
# Creating DataFrame 
df_input = pd.DataFrame(data_input)

data_output = { 'tweet_id': [2] } 
# Creating DataFrame 
df_output = pd.DataFrame(data_output)

assert invalid_tweets(df_input).equals(df_output)