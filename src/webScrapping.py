from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import html2text
import datetime

import requests  # http request
from bs4 import BeautifulSoup # webscrapping

from src.master import Master


class WebScapper(Master):

    def __init__(self, url):
        super().__init__()
        self.now = datetime.datetime.now()
        self.content = 1
        self.url = url

    def run(self):
        self.extract_news()

    def extract_news(self):
        print("Extracting Hacker News Stories")
        self.logger.info("Starting Scrapping")
        cnt = ''
        cnt += ('<b>HN Top Stories:</b>\n'+'<br>'+'-'*50+'<br>')
        response = requests.get(self.url)
        content = response.content

        soup = BeautifulSoup(content, 'html.parser')
        # for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        for i, tag in enumerate(soup.find_all('li', attrs={'class': 'fnt_siz_e'})):
            cnt += (str(i + 1) + ' ::' + tag.text + '\n' + '<br>') if tag.text != 'More' else ''

        cnt += '<br>-----------------------<br><br><br>End Of Message'
        print(html2text.html2text(cnt))
        self.logger.info("Scrapping has been completed")


