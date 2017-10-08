#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import requests
from bs4 import BeautifulSoup
from slugify import slugify

from utils import get_configs


class ParseUrl():
    def __init__(self):
        self.config = get_configs()

    def execute_parse(self, host, anime):

        if host == 'punchsub':
            return self.parse_punch(host['punchsub'], anime)

        elif host == 'anbient':
            return self.parse_anbient(host, anime['name'])

        return {}

    def parse_punch(self, host, anime):
        punchsub_parser = PunchParser()
        # import ipdb; ipdb.set_trace()
        parser = punchsub_parser.parser(anime)

        return parser

    def parse_anbient(self, host, anime_name):
        uris = self.config['uris']
        anbient_parse = AnbientParse()
        parser = anbient_parse.try_parse(host, uris['anbient'], anime_name, True)

        data = {
            "name": anbient_parse.parse_name(parser) or anime_name,
            "description": anbient_parse.parse_description(parser),
            "totalEpisodes": anbient_parse.parse_total_ep(parser),
            "genre": anbient_parse.parse_genres(parser),
            "img": anbient_parse.parse_image(parser)
        }
        return data


class AnbientParse():

    def __init__(self):
        self.config = get_configs()
        self.host = self.config['host']['anbient']
        # url = host + uri
        # self.tree = self.beautifulSoup_page(url)

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.content

        return requests_response

    def beautifulSoup_page(self, url):

        return BeautifulSoup(self.getPage(url), 'html.parser')

    def parse_description(self, tree):
        for node in tree.findAll('div', {"class": 'field field-body'}):

            description = node.find('div', attrs={'class': 'item '})
            return description.getText()

    def parser_image(self, tree, path='.'):
        for node in tree.findAll('div', {"class": 'anime-info'}):
            img = node.find('img')

            return self.host + img.attrs['src']

    def parse_total_ep(self, tree):
        if (tree.findAll('div', {"class": 'field-num-episodios inline inline field'})):
            for node in tree.findAll('div', {"class": 'field-num-episodios inline inline field'}):
                total_ep = node.find('span')
                return total_ep.getText()
        else:
            for node in tree.findAll('span', {"itemprop": 'numberOfEpisodes'}):
                return node.getText()

    def parse_name(self, tree):
        for node in tree.findAll('h1', {"id": 'page-title'}):

            return node.getText()

    def parse_genres(self, tree):
        for node in tree.findAll('span', {"class": 'generos'}):

            genres = node.findAll('a')
            txt = []
            for value in genres:
                txt.append(value.getText())

            return txt

    def try_parse(self, host, uris, anime, searching=True):
        host = self.host
        parse = self.beautifulSoup_page(host + uris[0] + anime)

        print('\t{}{}{}'.format(host, uris[0], anime))
        if (self.parse_name(parse)).strip() in [u'A página não foi encontrada', 'Animes']:
            if len(uris[1::]) > 0:
                return self.try_parse(host, uris[1::], anime)
            else:
                print('\t[ERROR]: Page  < {} > not found!'.format(anime))

                if searching:
                    print('\tTrying to find the anime < {} > '.format(anime))

                    from findAnime import FindAnime

                    animes_names = self.names_to_try(anime)

                    for anime_name in animes_names:
                        search = FindAnime(anime_name).parse_search()

                        if search:
                            print('\t' + str(search))

                            if search.get(slugify(anime), False):
                                anime_name = search.get(slugify(anime), anime)
                            else:
                                import prompt

                                i = 0
                                print("")
                                for search_keys, search_options in search.items():
                                    print('\t\t[ {} ]: {}'.format(i, search_keys))
                                    i += 1

                                print('\t\tAny another number: Cancel choice')
                                choice = prompt.integer(prompt="\t\tPlease enter a number: ")

                                keys_in_list = list(search.keys())
                                if choice == 99 or choice >= len(search):
                                    return False

                                anime_name = search[keys_in_list[choice]]

                            return self.try_parse(host, [''], anime_name, False)

                return False
        else:
            return parse

    def names_to_try(self, original_anime_name):
        animes_names = [original_anime_name]

        if "-and-" in original_anime_name:
            animes_names.append(original_anime_name.replace("-and-", "-e-"))
            animes_names.append(original_anime_name.replace("-and-", "-"))

        return animes_names


class PunchParser():
    def __init__(self):
        config = self.get_configs()
        self.host = config['host']['punchsub']

    def getPage(self, url):
        request_get = requests.get(url)
        requests_response = request_get.json()

        return requests_response

    def parser(self, anime):
        uri = '/listar/{}/episodios/{}'.format(anime['id'], anime['quality'])
        page = self.getPage(self.host + uri)

        return {
            "name": anime['name'],
            "description": page[6],
            "totalEpisodes": anime['totalEpisodes'],
            "genre": anime['genres'],
            "season": anime['season'],
            "img_url": "{}/imagens/projetos/animes/{}_thumb2.jpg".format(self.host, anime['id']),
            "url": "{}/#{}/1".format(self.host, uri)
        }
