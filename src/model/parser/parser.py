from io import open
from collections import OrderedDict

from ..msg import error_msg
from ..cataloguer import Cataloguer
from ..parse import Parse
from ..animes import AnimeLib

class Parser:
    def __init__(self, **kwargs):

        self.create_folder, \
        self.ends_with, \
        self.file, \
        _, \
        self.just_with, \
        self.list_type, \
        self.only, \
        self.override, \
        self.path, \
        self.starts_with = dict(OrderedDict(sorted(kwargs.items()))).values()

        if self.list_type == '' or self.file == '':
            error_msg('list type or file/path is empty')
            raise SystemExit

        if self.list_type not in ['list', 'folder']:
            error_msg('unrecognized list type. Please use < list > or < folder >')
            raise SystemExit


    def get_anime_list(self):
        anime_list = []

        if self.list_type == 'list':
            with open(self.file, 'r', encoding='utf-8') as f:
                for anime in f.readlines():
                    anime_name = anime.split('/', 4)[-1][:-1]
                    anime_list.append(anime_name)

        elif self.list_type == 'folder':

            path = self.path + '/' if self.path and self.path[-1] != '/' else self.path
            cataloguer = Cataloguer(path, 'dummy')
            anime_list = cataloguer.get_all_folders(path)

        return self._search_limit(anime_list)


    def _search_limit(self, anime_list):
        starts_with, ends_with, just_with = self.starts_with, self.ends_with, self.just_with

        if starts_with or (starts_with and ends_with) or just_with:
            if just_with:
                starts_with = just_with
                ends_with = just_with

            anime_list = sorted(anime_list)
            alphanumeric = [
                "a", "b", "c", "d", "e", "f", "g", "h",
                "i", "j", "k", "l", "m", "n", "o", "p",
                "q", "r", "s", "t", "u", "v", "w", "x",
                "y", "z", "0", "1", "2", "3", "4", "5",
                "6", "7", "8", "9"]
            starts_index = alphanumeric.index(starts_with)
            ends_index = alphanumeric.index(ends_with or "9")

            for word in anime_list[:]:
                if not word.lower().startswith(tuple(alphanumeric[starts_index:ends_index + 1])):
                    anime_list.remove(word)

        return anime_list

    def do(self, anime_list):
        parse_settings = [self.list_type, self.path,
                          self.create_folder, self.override, self.only]
        know_animes = AnimeLib().data

        Parse(anime_list, know_animes, parse_settings)





