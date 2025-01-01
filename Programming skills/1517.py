import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode\.com$'
    mask_mail = (users.loc[:,"mail"].str.match(pattern, na=False))
    print(users.loc[mask_mail,:])
    return users

data_input = { 'user_id': [1, 2, 3, 4, 5, 6, 7], 'name': ['Winston', 'Jonathan', 'Annabelle', 'Sally', 'Marwan', 'David', 'Shapiro'], 'mail': ['winston@leetcode.com', 'jonathanisgreat', 'bella-@leetcode.com', 'sally.come@leetcode.com', 'quarz#2020@leetcode.com', 'david69@gmail.com', '.shapo@leetcode.com'] } 
# Creating DataFrame 
df_input = pd.DataFrame(data_input)

valid_emails(df_input)

data_input = { 'user_id': [862, 34, 891, 745, 46, 156, 528, 63, 379, 348, 393, 660, 99, 822, 732, 689, 182, 192], 'name': ['Refael', 'Aharon', 'Sarah', 'Shimon', 'Freida', 'Yosef', 'Refael', 'Azriel', 'Daniel', 'Menachem', 'Yehudit', 'Yaakov', 'Yaffah', 'Refael', 'Yehudit', 'Michael', 'Adam', 'Miriam'], 'mail': ['Refaelm5m', '9.Aharon@leetcode.com', 'Sarah@L.com', '2019_Shim0n@leetcode.com', 'Freida(A1oA2N7tK@leetcode.com', 'Yosef@h.com', 'Refael@N6J.com', 'Azriel@jaB.com', 'DanielT7ugi@leetcode.com', 'Menachem$R6CLTItUEi@leetcode.com', 'Yehudit3y22YK', '-Yaakov@leetcode.com', 'YaffahsXa@leetcode.com', '_Refael@leetcode.com', 'Yehudit..lk@leetcode.com', 'Michael--4@leetcode.com', 'AdamPs@leetcode.com', 'Miriam^GCPhliEUL@leetcode.com'] }
df_input = pd.DataFrame(data_input)

valid_emails(df_input)
