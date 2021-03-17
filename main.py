import requests
import webbrowser
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, keywords):
        self.markup = requests.get('https://news.ycombinator.com/').text
        self.keywords = keywords
        self.parse()
        self.outputHTML()


    def parse(self):
        soup = BeautifulSoup(self.markup, 'html.parser')
        links = soup.find_all('a',{'class': 'storylink'})
        self.savedlinks = []
        for link in links:
            for keyword in self.keywords:
                if keyword in link.text:
                    self.savedlinks.append(link)
    
    def outputHTML(self):
        f = open('TodaysNews.html', 'w')
        body = " "
        for link in self.savedlinks:
            body += str(link)+ "<br><br>"
        
        f.write("<header><title>News of the Day</title><link rel="'stylesheet'" href="'style.css'"></header><body>")
        f.write(body)
        f.write("</body>")
        f.close()
        webbrowser.open_new_tab('TodaysNews.html')
