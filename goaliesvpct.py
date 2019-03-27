import requests
from bs4 import BeautifulSoup


resp = requests.get("http://www.espn.com/nhl/statistics/player/_/stat/goaltending/sort/savePct/year/2019/seasontype/2")


soup = BeautifulSoup(resp.text, 'html.parser')


# f = open("espnNHL1.txt", "w+")

# f.write(str(soup.prettify()))

# f.close()

# goalrow = soup.find_all('tr')[2]

# print(goalrow)

# data = soup.find('table')
# print(data)


goalies = {}
goalie2 = ""
svpct2 = 0
goalie_stats = []

for name in soup.find_all("tr")[2:]:
    
    
    for child in name.children:
        goalie_stats.append(child)
    
    if len(goalie_stats) > 2:
        
        rank = len(goalies)+1
        
        goalie1 = goalie_stats[1]
        goalie1 = goalie1.get_text()
        goalie = goalie1.partition(",")[0]
        
        if goalie != "SHOOTOUTS":
            svpct = goalie_stats[11]
            svpct = svpct.get_text()
            if svpct == svpct2: rank = rank - 1
            print(rank, goalie, svpct)
            goalies.update({goalie :[rank, svpct]})
            svpct2 = svpct
            goalie_stats = []
            continue
        elif goalie == "SHOOTOUTS":
            goalie = ""
            goalie_stats = []
            continue
    continue

# print(goalies)

rank = len(goalies)+1
svpct = .929
goalie = 'Ian Greengross'
print(rank, goalie, svpct)
goalies.update({goalie: [rank, svpct]})


find_goalie = input("Please enter a goalie:")

goalie_svpct = goalies[find_goalie][1]
print("His save percentage is: ", goalie_svpct)