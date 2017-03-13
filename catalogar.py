#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import simplejson as json


def get_folder_to_catalog():
    parent_folder = os.path.dirname(os.getcwd())

    return parent_folder + '/Animes'


def get_description(folder, file_name):
    file = folder + '/' + file_name
    with open(file) as data:
        description = json.load(data)

    return description


def break_folders_by_letter(folders):
    letters = {}

    for folder in folders:
        letters.setdefault(folder[:1], []).append(folder)

    return letters


def is_folder(folder_path, folder_name):
     return os.path.isdir(folder_path + '/' + folder_name)


def get_all_folders(folder_content, folder_path):
    all_folders = []
    for content_name in folder_content:
        if is_folder(folder_path, content_name):
            all_folders.append(content_name)

    return all_folders



current_folder = get_folder_to_catalog()
get_all_folders_names = get_all_folders(os.listdir(get_folder_to_catalog()), current_folder)
catalog_descriptions = {}

for folder_name in get_all_folders_names:
    folder = current_folder + '/' + folder_name
    catalog_descriptions[folder_name] = get_description(folder, 'description.json')

break_by_letters = break_folders_by_letter(get_all_folders_names)

print break_by_letters
