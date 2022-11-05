from requests_html import HTML, HTMLSession
import re
session = HTMLSession()

list = ["aatrox", "ahri", "akali", "akshan",
 "alistar", "amumu", "anivia", "annie",
 "aphelios", "ashe", "aurelionsol", "azir",
 "bard", "belveth", "blitzcrank", "brand",
 "braum", "caitlyn", "camille", "cassiopeia",
 "chogath", "corki", "darius", "diana",
 "drmundo", "draven", "ekko", "elise",
 "evelynn", "ezreal", "fiddlesticks", "fiora",
 "fizz", "galio", "gangplank", "garen", 
 "gnar", "gragas", "graves", "gwen",
 "hecarim", "heimerdinger", "illaoi", "irelia",
 "ivern", "janna", "jarvaniv", "jax",
 "jayce", "jhin", "jinx", "ksante",
 "kaisa", "kalista", "karma", "karthus", 
 "kassadin", "katarina", "kayle", "kayn",
 "kennen", "khazix", "kindred", "kled",
 "kogmaw", "leblanc", "leesin", "leona",
 "lillia", "lissandra", "lucian", "lulu",
 "lux", "malphite", "malzahar", "maokai",
 "masteryi", "missfortune", "mordekaiser", "morgana",
 "nami", "nasus", "nautilus", "neeko",
 "nidalee", "nilah", "nocturne", "nunu",
 "olaf", "orianna", "ornn", "pantheon",
 "poppy", "pyke", "qiyana", "quinn",
 "rakan", "rammus", "reksai", "rell",
 "renata", "renekton", "rengar", "riven",
 "rumble", "ryze", "samira", "sejuani",
 "senna", "seraphine", "sett", "shaco",
 "shen", "shyvana", "singed", "sion",
 "sivir", "skarner", "sona", "soraka",
 "swain", "sylas", "syndra", "tahmkench",
 "taliyah", "talon", "taric", "teemo",
 "thresh", "tristana", "trundle", "tryndamere",
 "twistedfate", "twitch", "udyr", "urgot",
 "varus", "vayne", "veigar", "velkoz",
 "vex", "vi", "viego", "viktor",
 "vladimir", "volibear", "warwick", "wukong",
 "xayah", "xerath", "xinzhao", "yasuo",
 "yone", "yorick", "yuumi", "zac",
 "zed", "zeri", "ziggs", "zilean"
 "zoe", "zyra"]
 
Kerdes = "nem"


while(Kerdes != "0"):
    Kerdes = input("Írd be a hős nevét: ")
    Champion_Name  = Kerdes
    if list.__contains__(Champion_Name.lower()):
        url = ("https://www.leagueofgraphs.com/rankings/summoners/" + Champion_Name.lower())

        r = session.get(url)

        proba = r.html.find('div#mainContent', first=True)
        tabla = proba.find('table.summonerRankingsTable', first=True)
        tablan_belul = proba.find('div.txt', first=True)


        nev = tablan_belul.find('span.name', first=True).text
        server = tablan_belul.find('i', first=True).text



        nev = nev.replace(' ', '+')

        


        new_url = ("https://leagueofgraphs.com/summoner/champions/"+ Champion_Name.lower()+"/"+server.lower()+"/"+nev)

        new_r = session.get(new_url)

        meccs = new_r.html.find('a.full-cell', first=True)
        meccsketto = meccs.xpath('//a/@href')
        meccs = meccsketto[0]

        print("https://www.leagueofgraphs.com"+meccs)





