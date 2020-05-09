import requests
import bs4
import csv
import json

with open('1.json','r') as file:
    data =file.read()
url_players = json.loads(data)['url_player']
# print(len(url_players))
hitung = 0
datas = []
for url_player in url_players:
    req_player = requests.get(url_player).text
    soup_player = bs4.BeautifulSoup(req_player, 'html.parser')
    # print(soup_player)
    info = soup_player.find('div',{'id':'info_content'}).findAll('tr')
    Name = info[0].find('td').text.strip()
    Club = info[1].find('td').text.strip()
    Nation = info[2].find('td').text.strip()
    League = info[3].find('td').text.strip()
    Skills = info[4].find('td').text.strip()
    Weak_Foot = info[5].find('td').text.strip()
    Intl_Rep =info[6].find('td').text.strip()
    Foot =info[7].find('td').text.strip()
    Height =info[8].find('td').text.strip()
    Weight =info[9].find('td').text.strip()
    Revision =info[10].find('td').text.strip()
    Def_WR =info[11].find('td').text.strip()
    Att_WR =info[12].find('td').text.strip()
    Added_on =info[13].find('td').text.strip()
    Origin =info[14].find('td').text.strip()
    R_Face =info[15].find('td').text.strip()
    B_Type = info[16].find('td').text.strip()
    Age = info[17].find('td').text.strip()
