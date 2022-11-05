from requests_html import HTML, HTMLSession
import re
session = HTMLSession()

#Kerdes = input("Írd be a hős nevét: ")
#Champion_Name  = Kerdes
Champion_Name = "brand"
url = ("https://www.leagueofgraphs.com/rankings/summoners/" + Champion_Name.lower())

r = session.get(url)

proba = r.html.find('div#mainContent', first=True)
tabla = proba.find('table.summonerRankingsTable', first=True)
tablan_belul = proba.find('div.txt', first=True)


nev = tablan_belul.find('span.name', first=True).text
server = tablan_belul.find('i', first=True).text



nev = nev.replace(' ', '+')

print(nev + " " +server)


new_url = ("https://leagueofgraphs.com/summoner/champions/"+ Champion_Name.lower()+"/"+server.lower()+"/"+nev)

new_r = session.get(new_url)

meccs = new_r.html.find('a.full-cell', first=True)
meccsketto = meccs.xpath('//a/@href')
meccs = meccsketto[0]

print("https://www.leagueofgraphs.com"+meccs)