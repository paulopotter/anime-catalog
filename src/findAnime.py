#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import requests
from bs4 import BeautifulSoup

from slugify import slugify


class FindAnime():

    def __init__(self, anime_name):
        self.anime_name = anime_name
        host = 'https://www.anbient.com/'
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
