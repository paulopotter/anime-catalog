import io
import requests

from src.utils import get_configs, normalize_name
from src.animes import Anime
from src.parseUrl import ParseUrl


class Parse():

    def __init__(self, list_animes, know_animes, parse_settings):
        self.list_animes = list_animes
        self.know_animes = know_animes
        self.parse_settings = parse_settings
        self.config = get_configs()
        self.parse_exec()

    def parse_exec(self):
        anime_list = self.list_animes
        total = 0
        success = 0
        fail = 0
        skipped = 0

        for anime_name in anime_list:
            anime_name = normalize_name(anime_name)

            if anime_name not in self.config.get('exclude', ''):
                total += 1
                print('\n- {}:'.format(anime_name))
                success, fail = self.parse_anime(anime_name, success, fail)
            else:
                skipped = skipped + 1

        print("\nTotal: {}\nSuccess: {}\nFail: {}\nSkipped: {}".format(total, success, fail, skipped))

    def parse_anime(self, anime_name, success, fail):

        parse = self.parse_by_host(anime_name)

        if parse:
            self.parse_write(parse)
            success = success + 1

        else:
            fail = fail + 1
            with io.open('not-found.log', 'a+', encoding='utf-8') as log:
                msg = u'< {} > not found!\n'.format(anime_name)
                print(msg)
                log.write(msg)

        return success, fail

    def parse_by_host(self, anime_name):
        data = {}
        anime_lib = Anime()
        parse_url = ParseUrl()
        knew_anime = {
            "anime": anime_lib.knew_anime(anime_name, self.know_animes['animes']),
            "ova": anime_lib.knew_anime(anime_name, self.know_animes['ovas']),
            "movie": anime_lib.knew_anime(anime_name, self.know_animes['movies']),
        }
        if knew_anime['anime']:
            data = parse_url.execute_parse('punchsub', knew_anime['anime'])
            if not data:
                for host in self.config['host']:
                    data.update(parse_url.execute_parse(host, knew_anime['anime']))

        elif knew_anime['ova']:
            pass

        elif knew_anime['movie']:
            pass

        else:
            data = parse_url.execute_parse('anbient', {'name': anime_name})

        return data

    def parse_write(self, data):
        list_or_folder, path, create_folder, override, overrideData = self.parse_settings
        anime_name = normalize_name(data['name'])
        try:
            def creating_file(overrideData=[]):
                from src.createFile import CreateFile

                create_file = CreateFile()
                create_file.create_json_file(data,
                                             folder_name=full_path,
                                             create_folder=create_folder,
                                             overrideData=overrideData)

            def getting_img(url_img, path):
                with open(path + '/thumb.png', 'wb') as thumb:
                    bla = requests.get(url_img)
                    thumb.write(bla.content)

            anime_dir = anime_name
            full_path = path + anime_dir

            if override:
                if overrideData:
                    if "image" in overrideData or overrideData == []:
                        getting_img(data['img_url'], full_path)
                    new_data = {}

                    data['path'] = full_path
                    for item in overrideData:
                        if "image" != item:
                            new_data[item] = data.get(item, '')

                    data = new_data
                creating_file(overrideData)

            else:

                import os

                try:
                    if 'description.json' in os.listdir(path + anime_dir):
                        print('\t< description.json > Alread exists!')
                    else:
                        creating_file()
                except OSError:
                    creating_file()
                try:
                    if 'thumb.png' in os.listdir(path + anime_dir):
                        print('\t< thumb.png > Alread exists!')
                    else:
                        getting_img(data['img_url'], full_path)
                except OSError:
                        getting_img(data['img_url'], full_path)

        except Exception as e:
            print('\t< {} > can not be done. \n\t[ERROR]: {} \n'.format(anime_name, e))
