import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_Nigerian_Grammy_Award_winners_and_nominees'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': 'wikitable sortable plainrowheaders'})

data = []
for row in table.find_all('tr'):
    columns = row.find_all(['th', 'td'])
    row_data = [col.get_text(strip=True) for col in columns]
    data.append(row_data)

header = data[1]
df = pd.DataFrame(data[2:], columns=header)
print(df)

df.to_csv('afrobeats_grammy.csv', index=False, header=True)
print(df_csv)
