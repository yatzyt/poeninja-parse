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

df.drop(["id", "icon", "artFilename", "itemClass", "count", "detailsId", "listingCount", "sparkline", "lowConfidenceSparkline", "implicitModifiers", "explicitModifiers", "flavourText"], axis=1, inplace=True)
