#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import simplejson as json



class Cataloguer():


    def __init__(self):
        current_folder = self.get_folder_to_catalog('Animes')
        get_all_folders_names = self.get_all_folders(os.listdir(current_folder), current_folder)
        catalog_descriptions = {}

        for folder_name in get_all_folders_names:
            folder = current_folder + '/' + folder_name
            catalog_descriptions[folder_name] = self.get_description(folder, 'description.json')

        break_by_letters = self.break_folders_by_letter(get_all_folders_names)

        print break_by_letters



    def get_folder_to_catalog(self, folder):
        parent_folder = os.path.dirname(os.getcwd())

        return parent_folder + '/' + folder


    def get_description(self, folder, file_name):
        file = folder + '/' + file_name
        with open(file) as data:
            description = json.load(data)

        return description


    def break_folders_by_letter(self, folders):
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
    Cataloguer()