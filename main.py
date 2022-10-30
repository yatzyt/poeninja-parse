import requests
import pandas as pd
import sys

url = "https://poe.ninja/api/data/"

overview_choice = input('Choose: \n1. Currency \n2. Item\n')
overview = 'overview/'

if overview_choice == '1':
    overview = 'currency' + overview
elif overview_choice == '2':
    overview = 'item' + overview
else:
    sys.exit("Did not enter a valid option.")

league = input('Which league?\n')
type = input('Which type?\nCurrency (Currency)\nFragment (Currency)\nArtifact (Item)\nOil (Item)\nIncubator (Item)\nScarab (Item)\nFossil (Item)\nResonator (Item)\nEssence (Item)\nDivinationCard (Item)\nSkillGem (Item)\nBaseType (Item)\nHelmetEnchant (Item)\nUniqueMap (Item)\nMap (Item)\nUniqueJewel (Item)\nUniqueFlask (Item)\nUniqueWeapon (Item)\nUniqueArmour (Item)\nUniqueAccessory (Item)\nBeast (Item)\nDeliriumOrb (Item)\nInvitation (Item)\nClusterJewel (Item)\nVial (Item)\n')

def construct_url(url_base, league, type):
    return url_base + "?league=" + league + "&type=" + type

final_url = construct_url(url + overview, league, type)

response = requests.get(final_url)
data = response.json()
requests.session().close()

df = pd.DataFrame(data["lines"])

df.to_csv('out.csv', index=False)