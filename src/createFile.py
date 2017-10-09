#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import io
import os
import simplejson as json

from src.msg import warning_msg, info_msg


class CreateFile():

    def __init__(self):
        pass

    def create_file(self, file_type, content, folder_name='.', file_name='description.js', create_folder=False):

        file_path = folder_name + '/' + file_name + '.' + file_type

        if create_folder:
            self.create_folder(folder_name)

        info_msg('Writing in the file < {}.{} >...'.format(file_name, file_type), True)

        with io.open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        info_msg('Writing completed!', True)

    def create_js_file(self, content,
                       folder_name='.',
                       file_name='data-json',
                       create_folder=False):

        data = 'var data=' + json.dumps(content, ensure_ascii=False) + ';'
        self.create_file('js', data, folder_name, file_name, create_folder)

    def create_json_file(self, content,
                         folder_name='.',
                         file_name='description',
                         create_folder=False,
                         overrideData=[]):
        content['path'] = folder_name
        if overrideData:

            if os.path.exists('{}/{}.json'.format(folder_name, file_name)):
                open_format = 'r'
            else:
                open_format = 'w'

            with io.open('{}/{}.json'.format(folder_name, file_name), open_format, encoding='utf-8') as f:
                file_content = f.read()
                old_data = json.loads(file_content) if len(file_content) > 0 else {}

                for new_data in overrideData:
                    if new_data != 'image':
                        old_data[new_data] = content[new_data]

                content = old_data

        data = json.dumps(content, ensure_ascii=False)
        self.create_file('json', data, folder_name, file_name, create_folder)

    def is_folder(self, folder_path='.', folder_name=''):
        return os.path.isdir(folder_path + '/' + folder_name)

    def create_folder(self, folder_name):
        folder_exists = self.is_folder(folder_name)

        if folder_exists:
            warning_msg('{} exists'.format(folder_name), True)
        else:
            os.mkdir(folder_name)
            info_msg('{} created!'.format(folder_name), True)

    def format_file(self, get_infos):

        if get_infos.get('totalEpisodes', 0) is None:
            totalEpisodes = 0
        else:
            totalEpisodes = get_infos.get('totalEpisodes', 0)

        return {
            'name': get_infos['name'],
            'description': get_infos.get('description', ''),
            'totalEpisodes': totalEpisodes,
            'episodesDownloaded': self.get_episodesDownloaded(get_infos.get('path', False)),
            'genre': get_infos.get('genre', []),
            "season": get_infos.get('season', 1),
            "othersSeasons": get_infos.get('othersSeasons', []),
            "rate": get_infos.get('rate', 0),
            "obs": get_infos.get('obs', ''),
            "path": get_infos.get('path', '')
        }

    def get_episodesDownloaded(self, anime_path):
        i = 0
        try:
            if anime_path:
                list_dir = os.listdir(anime_path)
                for listed_file in list_dir:
                    if not listed_file.endswith(tuple([".png", ".json"])):
                        i += 1

        except Exception:
            return 0

        return i
