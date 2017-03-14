#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
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

        for letter in folders_by_letters.keys():
            all_content_in_this_letter = folders_by_letters[letter]
            size_of_content_in_this_letter = len(all_content_in_this_letter)

            for i in range(size_of_content_in_this_letter):
                print catalog_descriptions[all_content_in_this_letter[i]]
                print '\n'


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
