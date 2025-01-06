import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by="score",ascending=False, inplace=True)
    previous_score:int = 0
    rank:int = 1
    scores.loc[:,["rank"]] = rank
    for score in scores.loc[:,"score"].unique().tolist():
        mask_score = (scores.loc[:,"score"] == score)
        scores.loc[mask_score,"rank"] = rank
        rank += 1
    
    return scores.loc[:,["score","rank"]]

data_input = {
    'id': [1, 2, 3, 4, 5, 6],
    'score': [3.50, 3.65, 4.00, 3.85, 4.00, 3.65]
}

df_input = pd.DataFrame(data_input)

data_output = {
    'score': [4.00, 4.00, 3.85, 3.65, 3.65, 3.50],
    'rank': [1, 1, 2, 3, 3, 4]
}

df_output = pd.DataFrame(data_output)

print("------------------------------------------------------------------------------------")
print(order_scores(df_input))
print(df_output)