#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import argparse
import inspect
import sys

from src.model.msg import error_msg, info_msg
from src.model.utils import normalize_name
from src.model.parser.parser import Parser
from src.model.cataloguer import Cataloguer
from src.model.createFile import CreateFile


def cataloguer(folder_name, description_file):
    cataloguer = Cataloguer(folder_name, description_file)
    create_file = CreateFile()
    data = cataloguer.prepared_content()
    create_file.create_js_file(data)


def parse(**kwargs):
    parser = Parser(**kwargs)
    anime_list = parser.get_anime_list()
    parser.do(anime_list)


def rename(folder_name):
    all_dir_names = os.listdir(folder_name)
    for dir_name in all_dir_names:
        try:
            info_msg('Renomeando \n\tde:   {} \n\tpara: {}'.format(folder_name + dir_name, folder_name + normalize_name(dir_name)))
            os.rename(folder_name + dir_name, folder_name + normalize_name(dir_name))
        except Exception as e:
            error_msg(e)


# ####


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommand")

    parser_cataloguer = subparsers.add_parser('cataloguer')
    parser_cataloguer.add_argument("--folder_name", default='../Animes')
    parser_cataloguer.add_argument("--description_file", default='description.json')

    parser_parse = subparsers.add_parser('parse')
    parser_parse.add_argument("--list_type", default='list')
    parser_parse.add_argument("--file", default='list.txt')
    parser_parse.add_argument("--path", default='./Animes')
    parser_parse.add_argument("--override", action='store_true', default=False)
    parser_parse.add_argument("--only", action='append', default=[])
    parser_parse.add_argument("--starts_with", default='')
    parser_parse.add_argument("--ends_with", default='')
    parser_parse.add_argument("--just_with", default='')
    parser_parse.add_argument("--create_folder", action='store_true', default=False)

    parser_rename = subparsers.add_parser('rename')
    parser_rename.add_argument("--folder_name", default='../Animes')

    args = parser.parse_args()

    execute = sys.argv[1]

    args_for_func = vars(args)

    if execute == 'parse':
        parse(**args_for_func)

    elif execute == 'cataloguer':
        cataloguer(**args_for_func)

    elif execute == 'rename':
        rename(**args_for_func)

    else:
        error_msg('Erro[1]: Invalid argument.')
