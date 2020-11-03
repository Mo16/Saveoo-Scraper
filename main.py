from urllib.request import urlopen, Request
from bs4 import BeautifulSoup as soup

page_num = 1

headers = "Page,Product,Link \n"
f = open("Savesoo.csv", "w", encoding="utf-8")
f.write(headers)
while True:
    my_url = f"https://gb.savesoo.com/freebies?pageNo={page_num}"
    req = Request(my_url, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    page_soup = soup(webpage, "html.parser")
    containers = page_soup.findAll("div", {"class": "goodOutside"})

    for container in containers:
        title = container.findAll("div", {"class": "layer"})[0]
        main_link = title.a["href"]
        link = f"https://gb.saveesoo.com{main_link}".replace('\n', '')
        product = (main_link.split("/review-product/")[-1]).replace("-", " ").replace('\n', '')[6:]
        f.write(f"{str(page_num)},{product.replace(',', '|')},{link}\n")
        print(f"{page_num},{product},{link}")
    page_num += 1
