from bs4 import BeautifulSoup as bs
import pandas as pd
import requests

temp_list = []
Star_names = []
Distance = []
Mass = []
Radius = []

startUrl = 'https://en.wikipedia.org/wiki/List_of_brown_dwarfs'
page = requests.get(startUrl)
soup = bs(page.text, 'html.parser')
starTable = soup.find_all('table')
table_rows = starTable[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][0])
    Distance.append(temp_list[i][5])
    Mass.append(temp_list[i][7])
    Radius.append(temp_list[i][8])

df = pd.DataFrame(list(zip(Star_names, Distance, Mass, Radius)), columns=['Star_name', 'Distance', 'Mass', 'Radius'])
df.to_csv('DwarfStars.csv') 