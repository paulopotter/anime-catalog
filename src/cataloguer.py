#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import simplejson as json

from src.createFile import CreateFile


class Cataloguer():

    def __init__(self, folder_to_catalog, description_file):
        self.description_file = description_file
        self.current_folder = self.get_folder_to_catalog(folder_to_catalog)

    def prepared_content(self):
        content = {}

        get_all_folders_names = self.get_all_folders(self.current_folder)
        all_descriptions = self.get_all_descriptions(get_all_folders_names)
        folders_by_letters = self.break_alphabetically(get_all_folders_names)

        cf = CreateFile()
        for letter in folders_by_letters.keys():
            description = []
            order_alphabetically = sorted(folders_by_letters[letter])

            for i in range(len(order_alphabetically)):
                data = all_descriptions[order_alphabetically[i]]
                path = '../{}/{}'.format(self.current_folder.rsplit('/', 2)[-2], order_alphabetically[i])

                if 'path' not in data:
                    data['path'] = path

                formated_data = cf.format_file(data)
                description.append(formated_data)

            content[letter] = description

        return content

    def get_folder_to_catalog(self, folder):
        parent_folder = os.path.dirname(os.getcwd())

        return parent_folder + '/' + folder

    def get_all_descriptions(self, folders):
        all_descriptions = {}
        for folder_name in folders:
            folder = self.current_folder + '/' + folder_name
            all_descriptions[folder_name] = self.get_description(folder, self.description_file)
        return all_descriptions

    def get_description(self, folder, file_name):
        file = folder + '/' + file_name
        try:
            with open(file) as data:
                description = json.load(data)
        except Exception:
            name = folder.split('/')[-1]
            print('< ' + name + ' > do not exist')
            description = {
                "name": name
            }

        return description

    def break_alphabetically(self, folders):
        letters = {}

        for folder in folders:
            letters.setdefault(folder[:1], []).append(folder)

        return letters

    def get_all_folders(self, folder_path):
        create_file = CreateFile()
        all_folders = []
        for content_name in os.listdir(folder_path):
            if create_file.is_folder(folder_path, content_name):
                all_folders.append(content_name)

        return all_folders
