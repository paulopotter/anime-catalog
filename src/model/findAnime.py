#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import re
import json


import requests
from bs4 import BeautifulSoup

from slugify import slugify

# from src.msg import simple_msg
from .utils import get_configs, normalize_name


class FindAnime():

    def __init__(self, anime_name):
        config = get_configs()
        self.anime_name = anime_name
        host = config['host']['anbient'] + '/'
        uri = 'search?search_api_views_fulltext=' + anime_name
        url = host + uri
        # simple_msg(url, 'white', tab=True)
        self.tree = self.beautifulSoup_page(url)

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.content

        return requests_response

    def beautifulSoup_page(self, url):

        return BeautifulSoup(self.getPage(url), 'html.parser')

    def parse_search(self):
        founds = {}
        for node in self.tree.findAll('a', {"rel": 'bookmark'}):
            name = slugify(node.string)
            founds[name] = node.attrs['href']

        return founds


class PunchLib():

    def __init__(self, list_type):
        self.config = get_configs()
        self.host = self.config['host']['punchsub'] + '/'
        position = {"animes": 0, "movies": 2, "ovas": 1}
        self.full_list = self.format_full_list(position[list_type])

    def get_full_list(self, position):
        url = 'https://punchsubs.net/buscar-projeto/anime'
        request_get = requests.get(url)
        content = request_get.content
        bs = BeautifulSoup(content, 'html.parser')
        pattern = re.compile("var values = \[.*?\]\;")
        values = pattern.findall(bs.text)[0]
        value = values.split('var values = ')[1].rsplit(';', 1)
        the_list = json.loads(json.loads(json.dumps(value))[0])
        return the_list

    def format_full_list(self, position):
        full_list = self.get_full_list(position)
        new_full_list = {}
        for anime in full_list:
            new_full_list.setdefault(anime['titulo'].upper(), []).append(self._list_2_dict(anime))

        return new_full_list

    def _list_2_dict(self, value):
        name = normalize_name(value['titulo'])
        return {
            "name": name,
            # "id": value[0],
            # "quality": value[5],
            "season": "Primeira temporada",
            "totalEpisodes": value['sinopse'],
            "genres": [value['genero']],
            "link": value['link'],
            "imagem": value['imagem']
        }
