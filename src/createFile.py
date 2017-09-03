#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import io
import os
import simplejson as json


class CreateFile():

    def __init__(self):
        pass

    def create_file(self, file_type, content, folder_name='.', file_name='description.js', create_folder=False):

        file_path = folder_name + '/' + file_name + '.' + file_type

        if create_folder:
            self.create_folder(folder_name)

        print('\tWriting in the file < {}.{} >...'.format(file_name, file_type))

        with io.open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print('\tWriting completed!')

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
            with io.open('{}/{}.json'.format(folder_name, file_name), 'r', encoding='utf-8') as f:
                old_data = json.loads(f.read())

                for new_data in overrideData:
                    old_data[new_data] = content[new_data]

                content = old_data

        data = json.dumps(content, ensure_ascii=False)
        self.create_file('json', data, folder_name, file_name, create_folder)

    def is_folder(self, folder_path='.', folder_name=''):
        return os.path.isdir(folder_path + '/' + folder_name)

    def create_folder(self, folder_name):
        folder_exists = self.is_folder(folder_name)

        if folder_exists:
            print('\t{} exists'.format(folder_name))
        else:
            os.mkdir(folder_name)
            print('\t{} created!'.format(folder_name))

    def format_file(self, get_infos):

        if get_infos.get('totalEpisodes', 0) is None:
            totalEpisodes = 0
        else:
            totalEpisodes = get_infos.get('totalEpisodes', 0)

        return {
            'name': get_infos['name'],
            'description': get_infos.get('description', ''),
            'totalEpisodes': totalEpisodes,
            'episodesDownloaded': get_infos.get('episodesDownloaded', 0),
            'genre': get_infos.get('genre', []),
            "season": get_infos.get('season', 1),
            "othersSeasons": get_infos.get('othersSeasons', []),
            "rate": get_infos.get('rate', 0),
            "obs": get_infos.get('obs', ''),
            "path": get_infos.get('path', '')
        }
