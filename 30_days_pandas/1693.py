import pandas as pd
from datetime import datetime

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    result = daily_sales.groupby(['date_id', 'make_name']).agg({
        'lead_id': pd.Series.nunique,
        'partner_id': pd.Series.nunique
    }).reset_index()

    result.columns = ['date_id', 'make_name', 'unique_leads', 'unique_partners']

    result['date_id'] = result['date_id'].dt.strftime('%Y-%m-%d')
    return result



data = {
    'date_id': [
        datetime(2020, 12, 8),
        datetime(2020, 12, 8),
        datetime(2020, 12, 8),
        datetime(2020, 12, 7),
        datetime(2020, 12, 7),
        datetime(2020, 12, 8),
        datetime(2020, 12, 8),
        datetime(2020, 12, 7),
        datetime(2020, 12, 7),
        datetime(2020, 12, 7)
    ],
    'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota', 'honda', 'honda', 'honda', 'honda', 'honda'],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
}

df = pd.DataFrame(data)

print(daily_leads_and_partners(df))