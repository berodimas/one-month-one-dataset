import requests, warnings 
import pandas as pd
from datetime import datetime, timezone, timedelta
warnings.filterwarnings('ignore')

## Scraper fucntion
def scraper():
    ## Define time_start
    time_start = datetime.utcnow().date() - timedelta(days=365)
    time_start_ts = datetime.strptime(f"{time_start} 00:00", "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp()
    ## Define time_end
    time_end = datetime.utcnow().date()
    time_end_ts = datetime.strptime(f"{time_end} 00:00", "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc).timestamp()
    ## Define data endpoint 
    url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id=3513&convertId=2781&timeStart={int(time_start_ts)}&timeEnd={int(time_end_ts)}"
    ## GET json return from endpoint and define dataframe
    r = requests.get(url).json()
    get_value = r.get('data')['quotes']
    df = pd.DataFrame()
    ## Append every rows from parsed return
    for x in get_value:
        df = df.append(x['quote'], ignore_index=True)
    ## Write csv files based on data
    df.to_csv('{}_FTM.csv'.format(str(datetime.utcnow().date())), index=False)