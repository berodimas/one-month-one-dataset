from itsdangerous import json
import requests
import pandas as pd
from datetime import datetime

url = 'https://niftyprice.herokuapp.com/'
current_utc = datetime.utcnow()

r = requests.get(url).json()
get_value = r.get('message')

dataframe = pd.DataFrame.from_dict(get_value)
dataframe.to_csv('{}_niftyprice.csv'.format(str(current_utc.date())), index=False)