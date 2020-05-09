import requests
import bs4

url = 'https://www.futbin.com/players?page=1'
req =  requests.get(url).text
soup = bs4.BeautifulSoup(req,'html.parser')

rencana = [
            {'nama':'Maya', 'kelas':'IPA A'},
            {'nama':'Tika', 'kelas':'IPA B'},
            {'nama':'Koko', 'kelas':'IPA C'}
        ]

data = []
for number in [1,2]:
    players = soup.findAll('tr','player_tr_'+str(number))
    for p in players:
        tds = p.find_all('td')
        name = tds[0].text.strip()
        clubs = p.find('span', 'players_club_nation').findAll('a')
        club = clubs[0]['data-original-title'].replace('Icons', 'Unknow').strip()
        nation = clubs[1]['data-original-title'].replace('Icons', 'Unknow').strip()
        league = clubs[2]['data-original-title'].replace('Icons', 'Unknow').strip()

        data.append(
                        {'Name':name,'Club':club, 'Nation':nation, 'League':league}
                    )

print(data)
print(rencana)