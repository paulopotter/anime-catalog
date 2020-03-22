#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import json

from ..msg import error_msg
# from .createFile import CreateFile
# from .utils import get_configs


class Cataloguer():

    def get_folder_to_catalog(self, folder):
        parent_folder = os.path.dirname(os.getcwd())

        return parent_folder + '/' + folder

    def get_description(self, folder, file_name):
        file = folder + '/' + file_name

        try:
            with open(file, encoding='utf-8') as data:
                description = json.load(data)
        except FileNotFoundError:
            error_msg('< ' + file_name + ' > do not exist')
            description = { "name": file_name }

        return description
