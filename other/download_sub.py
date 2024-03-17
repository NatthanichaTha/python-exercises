from urllib.request import urlretrieve, Request, urlopen
from bs4 import BeautifulSoup
from random import randint
import urllib.parse

req = Request("https://kitsunekko.net/dirlist.php?dir=subtitles%2Fjapanese%2F")
html_page = urlopen(req).read()
soup = BeautifulSoup(html_page, 'html.parser')

anime_list = soup.find_all("tr")
first_anime = anime_list[0].find("a")
first_anime_link = first_anime.attrs["href"]
first_anime_name = first_anime.find("strong")
print(first_anime_name.text, first_anime_link)

anime_resource_link = "https://kitsunekko.net" + first_anime_link
print(anime_resource_link)
req = Request(anime_resource_link)
html_page = urlopen(req).read()
soup = BeautifulSoup(html_page, 'html.parser')
subtitle_list = soup.find_all("tr")
subtitle = subtitle_list[0].find("a")
subtitle_link = urllib.parse.quote(subtitle.attrs["href"])
subtitle_name = subtitle.find("strong")
# print(subtitle_name)
urlretrieve("https://kitsunekko.net"+subtitle_link, subtitle_name.text)