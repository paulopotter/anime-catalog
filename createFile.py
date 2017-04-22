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

        print 'Writing in the file < {} >...'.format(file_name)

        with io.open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print 'Writing completed!'

    def create_js_file(self, content,
                       folder_name='.',
                       file_name='data-json',
                       create_folder=False):

        data = 'var data=' + json.dumps(content, ensure_ascii=False) + ';'
        self.create_file('js', data, folder_name, file_name, create_folder)

    def create_json_file(self, content,
                         folder_name='.',
                         file_name='description',
                         create_folder=False):

        self.create_file('json', content, folder_name, file_name, create_folder)

    def is_folder(self, folder_path='.', folder_name=''):
        return os.path.isdir(folder_path + '/' + folder_name)

    def create_folder(self, folder_name):
        folder_exists = self.is_folder(folder_name)

        if folder_exists:
            print '{} exists'.format(folder_name)
        else:
            os.mkdir(folder_name)
            print '{} created!'.format(folder_name)

    def format_file(self, get_infos):
        return {
            'name': get_infos['name'],
            'description': get_infos['description'],
            'totalEpisodes': get_infos['total_ep'],
            'genre': get_infos['genres'],
            "season": get_infos['season'],
            "othersSeasons": get_infos['othersSeasons'],
            "rate": get_infos['rate'],
            "obs": get_infos['obs`']
        }
