from requests_html import HTML, HTMLSession
session = HTMLSession()

#Kerdes = input("Írd be a hős nevét: ")
#Champion_Name  = Kerdes
Champion_Name = "akshan"
url = ("https://www.leagueofgraphs.com/rankings/summoners/" + Champion_Name.lower())

r = session.get(url)

proba = r.html.find('div#mainContent', first=True)
tabla = proba.find('table.summonerRankingsTable', first=True)
tablan_belul = proba.find('div.txt', first=True)


nev = tablan_belul.find('span.name', first=True).text
server = tablan_belul.find('i', first=True).text



nev = nev.replace(' ', '+')

print(nev + " " +server)


print("https://leagueofgraphs.com/summoner/champions/"+ Champion_Name.lower()+"/"+server.lower()+"/"+nev)
