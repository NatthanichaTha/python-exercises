from urllib.request import urlretrieve, Request, urlopen
from bs4 import BeautifulSoup

# req = Request('https://www.dragonball-multiverse.com/it/page-1.html')
# html_page = urlopen(req).read()

# soup = BeautifulSoup(html_page, 'html.parser')
# # dapage = soup.find_all("div", {"class": "dapage"})[0]
# # image_link = dapage.findChildren("a", recursive=False)[0]
# # image = image_link.findChildren("img", recursive=False)[0]
# image = soup.find("img", {"id": "balloonsimg"})
# image_url = "https://www.dragonball-multiverse.com/"+image.attrs['src']
# # urlretrieve(url, path) --> downloads the file at the specified url to the specified path
# urlretrieve(image_url, "page1.png")

for i in range(1, 11):
    req = Request("https://www.dragonball-multiverse.com/it/page-"+str(i)+".html")
    html_page = urlopen(req).read()
    soup = BeautifulSoup(html_page, 'html.parser')
    image = soup.find("img", {"id": "balloonsimg"})
    if image == None:
        pass
    else:
        image_url = "https://www.dragonball-multiverse.com/"+image.attrs['src']
        urlretrieve(image_url, "page" + str(i) +".png")