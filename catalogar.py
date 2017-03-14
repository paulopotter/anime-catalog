#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import io
import simplejson as json


class Cataloguer():

    def __init__(self, folder_to_catalog, description_file):
        self.current_folder = self.get_folder_to_catalog(folder_to_catalog)
        get_all_folders_names = self.get_all_folders(os.listdir(self.current_folder), self.current_folder)
        catalog_descriptions = {}

        for folder_name in get_all_folders_names:
            folder = self.current_folder + '/' + folder_name
            catalog_descriptions[folder_name] = self.get_description(folder, description_file)

        folders_by_letters = self.break_alphabetically(get_all_folders_names)

        content = {}
        for letter in folders_by_letters.keys():
            description = []
            all_content_in_this_letter = folders_by_letters[letter]
            size_of_content_in_this_letter = len(all_content_in_this_letter)
            order_alphabetically = sorted(all_content_in_this_letter)

            for i in range(size_of_content_in_this_letter):
                description.append(catalog_descriptions[order_alphabetically[i]])

            content[letter] = description

        print 'Write in file...'
        with io.open('data.json', 'w', encoding='utf-8') as f:
            f.write(json.dumps(content, ensure_ascii=False))
        print 'Write complete'

    def get_folder_to_catalog(self, folder):
        parent_folder = os.path.dirname(os.getcwd())

        return parent_folder + '/' + folder

    def get_description(self, folder, file_name):
        file = folder + '/' + file_name
        with open(file) as data:
            description = json.load(data)

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
    Cataloguer('Animes', 'description.json')
