#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import requests
from bs4 import BeautifulSoup

from slugify import slugify

from src.utils import get_configs, normalize_name


class FindAnime():

    def __init__(self, anime_name):
        config = get_configs()
        self.anime_name = anime_name
        host = config['host']['anbient'] + '/'
        uri = 'search?search_api_views_fulltext=' + anime_name
        url = host + uri
        print('\t' + url)
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
        url = self.host + self.config['uris']['punchsub'][position]
        request_get = requests.get(url)
        return request_get.json()

    def format_full_list(self, position):
        full_list = self.get_full_list(position)
        new_full_list = {}
        for anime in full_list:
            new_full_list.setdefault(anime[2].upper(), []).append(self._list_2_dict(anime))

        return new_full_list

    def _list_2_dict(self, value):
        name = normalize_name(value[1])
        return {
            "name": name,
            "id": value[0],
            "quality": value[5],
            "season": value[3] or "Primeira temporada",
            "totalEpisodes": value[6],
            "genres": [value[4]]
        }
