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


get_all_folders_names = os.listdir(get_folder_to_catalog())
current_folder = get_folder_to_catalog()
catalog_descriptions = {}

for folder_name in get_all_folders_names:
    folder = current_folder + '/' + folder_name
    catalog_descriptions[folder_name] = get_description(folder, 'descricao.json')


print catalog_descriptions
