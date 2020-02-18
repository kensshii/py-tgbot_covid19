# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from urllib.request import urlopen

class HtmlParser:
    def __init__(self, url):
        self._content = []
        self.htmlDoc = urlopen(url).read()
        self.htmlParser = BeautifulSoup(self.htmlDoc, 'html.parser')

    def parse(self):
        soup = self.htmlParser.findAll("div", {"class": "maincounter-number"})
        self._content = [
            soup[0].text.replace(',', '').strip(), 
            soup[1].text.replace(',', '').strip(), 
            soup[2].text.replace(',', '').strip()
        ]

    def getContent(self):
        return self._content