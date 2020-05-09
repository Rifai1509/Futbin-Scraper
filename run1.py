import requests
import bs4
import _csv
import json



with open('1page.json','r') as file:
    data =file.read()
url_players = json.loads(data)['url_player']
# print(len(url_players))
Number = 0
datas = []
for url_player in url_players:
    req_player = requests.get(url_player).text
    # print(req_player)
    soup_player = bs4.BeautifulSoup(req_player, 'html.parser')
    # print(soup_player)
    info = soup_player.find('div',{'id':'info_content'}).findAll('tr')
    Number +=1
    print(Number)
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


    datas.append([Number,Name, Club, Nation, League, Skills, Weak_Foot, Intl_Rep, Foot, Height, Weight,
                 Revision, Def_WR, Att_WR, Added_on, Origin, R_Face, B_Type, Age])

    print(Name)
    print(Club)
    print(Nation)
    print(League)
    print(Skills)
    print(Weak_Foot)
    print(Intl_Rep)
    print(Foot)
    print(Height)
    print(Weight)
    print(Revision)
    print(Def_WR)
    print(Att_WR)
    print(Added_on)
    print(Origin)
    print(R_Face)
    print(B_Type)
    print(Age)

with open('result1.csv', 'w', newline='') as file:
    writer = _csv.writer(file)
    headers = [
        'Num','Name','Club', 'Nation', 'League', 'Skills', 'Weak_Foot', 'Intl.Rep', 'Foot', 'Height',
        'Weight', 'Revision', 'Def_WR','Att_WR', 'Added_on', 'Origin', 'R.Face', 'B.Type', 'Age'
    ]
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)