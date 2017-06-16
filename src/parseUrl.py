#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import urllib

import requests
from bs4 import BeautifulSoup


class Parse():

    def __init__(self, host, uri):
        self.host = host
        url = host + uri
        self.tree = self.beautifulSoup_page(url)

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.content

        return requests_response

    def beautifulSoup_page(self, url):

        return BeautifulSoup(self.getPage(url), 'html.parser')

    def parse_description(self):
        for node in self.tree.findAll('div', {"class": 'field field-body'}):

            description = node.find('div', attrs={'class': 'item '})
            return description.getText()

    def get_image(self, path='.'):
        for node in self.tree.findAll('div', {"class": 'anime-info'}):

            img = node.find('img')
            url_img = self.host[:-1] + img.attrs[0][1]

            urllib.urlretrieve(url_img, path + '/thumb.png')
            return url_img

    def parse_total_ep(self):
        if (self.tree.findAll('div', {"class": 'field-num-episodios inline inline field'})):
            for node in self.tree.findAll('div', {"class": 'field-num-episodios inline inline field'}):
                total_ep = node.find('span')
                return total_ep.getText()
        else:
            for node in self.tree.findAll('span', {"itemprop": 'numberOfEpisodes'}):
                return node.getText()

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
