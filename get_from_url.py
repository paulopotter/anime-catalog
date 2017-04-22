#!/usr/bin/env python

import io
import urllib

import requests
import simplejson as json
from BeautifulSoup import BeautifulSoup


class Parse():

    def __init__(self, url):
        self.url = url
        # self.url = 'https://www.anbient.com/anime/seikon-no-qwaser'
        self.tree = self.bs_page()
        # self.name = 'seikon-no-qwaser'

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.content

        return requests_response

    def bs_page(self):
        return BeautifulSoup(self.getPage(self.url))

    def parse_description(self):
        for node in self.tree.findAll('div', {"class": 'field field-body'}):

            description = node.find('div', attrs={'class': 'item '})
            return description.getText()

    def get_image(self):
        for node in self.tree.findAll('div', {"class": 'anime-info'}):

            img = node.find('img')
            url_img = 'https://www.anbient.com' + img.attrs[0][1]

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


# #####


class CreateFile():

    def __init__(self):
        pass

    def format_file(self, get_infos):
        data = {
            'name': get_infos.parse_name(),
            'description': get_infos.parse_description(),
            'totalEpisodes': get_infos.parse_total_ep(),
            'genre': get_infos.parse_genres(),
            "season": "1",
            "othersSeason": [],
            "rate": "0",
            "obs": ""
        }

        return data

    def create_json_file(self, parse, folder_name):
        content = self.format_file(parse)
        print 'Writing in the file...'
        with io.open(folder_name + '/description.js', 'w', encoding='utf-8') as f:
            f.write('var data=' + json.dumps(content, ensure_ascii=False) + ';')
        print 'Writing completed!'

        # Parse().get_image()


class MakeTheMagic():

    def __init__(self):
        with io.open('blo.txt', 'r', encoding='utf-8') as lista_de_animes:
            for anime in lista_de_animes.readlines():

                create_file = CreateFile()
                parse = Parse(anime[:-1])
                name = parse.parse_name()

                try:
                    create_file.create_json_file(parse, name)
                    parse.get_image(name)
                except Exception as e:
                    print '<{}> nao pode ser realizado. \n'.format(name, e)


MakeTheMagic()
