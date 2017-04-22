#!/usr/bin/env python

# import io
import urllib

import requests
from BeautifulSoup import BeautifulSoup


class Parse():

    def __init__(self, host, uri):
        self.host = host
        # host = 'https://www.anbient.com/'
        # uri = 'anime/seikon-no-qwaser'
        url = host + uri
        self.tree = self.beautifulSoup_page(url)

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.content

        return requests_response

    def beautifulSoup_page(self, url):
        return BeautifulSoup(self.getPage(url))

    def parse_description(self):
        for node in self.tree.findAll('div', {"class": 'field field-body'}):

            description = node.find('div', attrs={'class': 'item '})
            return description.getText()

    def get_image(self):
        for node in self.tree.findAll('div', {"class": 'anime-info'}):

            img = node.find('img')
            url_img = self.host[:-1] + img.attrs[0][1]

            urllib.urlretrieve(url_img, self.name + '/thumb.png')
            return url_img

    def parse_total_ep(self):
        for node in self.tree.findAll('div', {"class": 'field-num-episodios inline inline field'}):

            total_ep = node.find('span')
            return total_ep.getText()

    def parse_name(self):
        for node in self.tree.findAll('h1', {"id": 'page-title'}):

            return node.getText()

    def parse_genres(self):
        for node in self.tree.findAll('span', {"class": 'generos'}):

            genres = node.findAll('a')
            txt = []
            for value in genres:
                txt.append(value.getText())

            return txt


# class MakeTheMagic():

#     def __init__(self):
#         with io.open('blo.txt', 'r', encoding='utf-8') as lista_de_animes:
#             for anime in lista_de_animes.readlines():

#                 create_file = CreateFile()
#                 parse = Parse(anime[:-1])
#                 name = parse.parse_name()

#                 try:
#                     create_file.create_json_file(parse, name)
#                     parse.get_image(name)
#                 except Exception as e:
#                     print '<{}> nao pode ser realizado. \n'.format(name, e)


# MakeTheMagic()