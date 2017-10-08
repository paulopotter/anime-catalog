#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from src.findAnime import PunchLib


class AnimeLib():
    def __init__(self):
        self.data = {
            "animes": PunchLib("animes").full_list,
            "ovas": PunchLib("ovas").full_list,
            "movies": PunchLib("movies").full_list,
        }


class Anime():
    def __init__(self):
        pass

    def knew_anime(self, anime_name, anime_list):
        full_list = anime_list
        char_list = full_list.get(anime_name[:1].upper(), '')
        for pos, anime in enumerate(char_list):
            if anime["name"] == anime_name:
                return anime

        return False
