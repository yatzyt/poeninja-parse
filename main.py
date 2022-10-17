from cmath import nan
import requests
import pandas as pd

url_currency = "https://poe.ninja/api/data/currencyoverview"
url_item = "https://poe.ninja/api/data/itemoverview"


def construct_url(url_base, league, type):
    return url_base + "?league=" + league + "&type=" + type

div_card = construct_url(url_item, "Kalandra", "DivinationCard")
response = requests.get(div_card)
data = response.json()
requests.session().close()

df = pd.DataFrame(data["lines"])

columns_to_drop = ["id", "icon", "artFilename", "itemClass", "count", "detailsId", "listingCount", "sparkline", "lowConfidenceSparkline", "implicitModifiers", "explicitModifiers", "flavourText", "exaltedValue"]
df.drop(columns_to_drop, axis=1, inplace=True)

df.fillna(value=float(1), axis=1, inplace=True)

def stack_price_in_chaos(row):
    return row.chaosValue * row.stackSize

def stack_price_in_divine(row):
    return row.divineValue * row.stackSize

df['stackPriceInChaos'] = df.apply(lambda row: stack_price_in_chaos(row), axis=1)

df['stackPriceInDivine'] = df.apply(lambda row: stack_price_in_divine(row), axis=1)

df.to_csv('out.csv', index=False)