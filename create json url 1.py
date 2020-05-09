import requests
import bs4
import json

prograss = 0
data = {}
data['url_player'] = []
for page in range(1, 2):
    url = 'https://www.futbin.com/players?page='+str(page)
    req =  requests.get(url).text
    soup = bs4.BeautifulSoup(req,'html.parser')
    players = soup.findAll('a','player_name_players_table')
    for player in players:
        url_player = 'https://futbin.com'+str(player['href']).strip()
        data['url_player'].append(url_player)
        prograss+=1
        print(prograss)
with open('1page.json', 'w') as file:
    json.dump(data, file)