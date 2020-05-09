import requests, bs4, _csv

num = 0
datas = []

for page in range(1, 51):
    url = 'https://www.futbin.com/players?page='+str(page)
    req =  requests.get(url).text
    soup = bs4.BeautifulSoup(req,'html.parser')
    numbers = [1,2]

    for number in numbers:
        players = soup.findAll('tr','player_tr_'+str(number))
        for p in players:
            tds = p.find_all('td')
            name = tds[0].text.strip()
            clubs = p.find('span', 'players_club_nation').findAll('a')
            club = clubs[0]['data-original-title'].replace('Icons', '-').strip()
            nation = clubs[1]['data-original-title'].replace('Icons', '-').strip()
            league = clubs[2]['data-original-title'].replace('Icons', '-').strip()
            rat = tds[1].find('span').text.strip()
            pos = tds[2].text.strip()
            ps = tds[4].text.strip()
            ski = tds[5].text.strip()
            wf = tds[6].text.strip()
            wr = tds[7].text.strip()
            pac = tds[8].text.strip()
            sho =tds[9].text.strip()
            pas =tds[10].text.strip()
            dri =tds[11].text.strip()
            defend = tds[12].text.strip()
            phy =tds[13].text.strip()
            heigh =tds[14].text.split('|')[0].strip()
            pop =tds[15].text.strip()
            bs =tds[16].text.strip()
            igs = tds[17].text.strip()
            num +=1
            print('Number   : ',num)
            print('Name     : ',name)
            print('Club     : ',club)
            print('Nation   : ',nation)
            print('League   : ',league)
            print('Rating   : ',rat)
            print('Position : ',pos)
            print('Price    : ', ps)
            print('Skill    : ', ski)
            print('Weak foot: ',wf)
            print('Att/deff : ', wr)
            print('Pac      : ',pac)
            print('Shoting  : ', sho)
            print('Passing  : ',pas)
            print('Dribling : ', dri)
            print('Def      : ',defend)
            print('Phy      : ',phy)
            print('Heigh    : ',heigh)
            print('Pop      : ', pop)
            print('Bs       : ',bs)
            print('IGS      : ',igs, '\n')
            datas.append([name, club, nation, league, rat, pos, ps, ski, wf,
                          wr, pac, sho, pas, dri, defend,phy, heigh, pop, bs, igs])

with open('results.csv', 'w', newline='', encoding='utf-8') as file:
    writer = _csv.writer(file)
    headers = [
        'Name','Club', 'Nation', 'League', 'Rat', 'Pos', 'PS', 'Skill', 'WF',
        'Att/Deff', 'PAC', 'Shott','Pass', 'Dribling', 'Def', 'Phy', 'Heigh, Pop, BS, IGS'
    ]
    writer.writerow(headers)
    for data in datas:
        writer.writerow(data)