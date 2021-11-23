# On importe la fonction 'get' (téléchargement) de 'requests' 
# Et la classe 'Selector' (Parsing) de 'scrapy'
from requests_html import HTMLSession 
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
# sample youtube video url
video_url = "https://www.youtube.com/watch?v=rKxbm-npg8I"
# init an HTML Session
session = HTMLSession()
# get the html content
response = session.get(video_url)
# execute Java-script
response.html.render(sleep=1)
# create bs object to parse HTML
soup = bs(response.html.html, "html.parser")
title = soup.find("meta", itemprop="name")['content']
print(title)