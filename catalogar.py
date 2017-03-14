#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import io
import simplejson as json


class Cataloguer():

    def __init__(self, folder_to_catalog, description_file):
        self.description_file = description_file
        self.current_folder = self.get_folder_to_catalog(folder_to_catalog)

    def create_json_file(self, filename):
        content = self.prepared_content()
        print 'Writing in the file...'
        with io.open('data-json.js', 'w', encoding='utf-8') as f:
            f.write('var data=' + json.dumps(content, ensure_ascii=False) + ';')
        print 'Writing completed!'

    def prepared_content(self):
        content = {}

        get_all_folders_names = self.get_all_folders(os.listdir(self.current_folder), self.current_folder)
        all_descriptions = self.get_all_descriptions(get_all_folders_names)
        folders_by_letters = self.break_alphabetically(get_all_folders_names)

        for letter in folders_by_letters.keys():
            description = []
            order_alphabetically = sorted(folders_by_letters[letter])

            for i in range(len(order_alphabetically)):
                description.append(all_descriptions[order_alphabetically[i]])

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
        except:
            name = folder.split('/')[-1]
            print '< ' + name + ' > do not exist'
            description = {
                "name": name
            }

        return description

    def break_alphabetically(self, folders):
        letters = {}

        for folder in folders:
            letters.setdefault(folder[:1], []).append(folder)

        return letters

    def is_folder(self, folder_path, folder_name):
        return os.path.isdir(folder_path + '/' + folder_name)

    def get_all_folders(self, folder_content, folder_path):
        all_folders = []
        for content_name in folder_content:
            if self.is_folder(folder_path, content_name):
                all_folders.append(content_name)

        return all_folders


if __name__ == "__main__":
    cataloguer = Cataloguer('Animes', 'description.json')
    cataloguer.create_json_file('data')
