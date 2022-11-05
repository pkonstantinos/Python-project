import pandas as pd
from pandas import read_html
import html5lib

Champion_Name = input("Írd be a hős nevét: ")
Champion_Name = Champion_Name.lower
url = "https://www.leagueofgraphs.com/rankings/summoners/" + Champion_Name


print(url)