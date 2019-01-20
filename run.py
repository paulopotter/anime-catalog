#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
import argparse
import inspect

from src.model.msg import error_msg, info_msg
from src.model.utils import normalize_name

from src.model.parser.parser import Parser


def cataloguer(folder_name, description_file):
    from src.model.cataloguer import Cataloguer
    from src.model.createFile import CreateFile

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
    parser_cataloguer.set_defaults(func=cataloguer)

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
    parser_parse.set_defaults(func=parse)

    parser_rename = subparsers.add_parser('rename')
    parser_rename.add_argument("--folder_name", default='../Animes')
    parser_rename.set_defaults(func=rename)

    args = parser.parse_args()

    arg_spec = inspect.getargspec(args.func)
    if arg_spec.keywords:
        # # convert args to a dictionary
        args_for_func = vars(args)
    else:
        # # get a subset of the dictionary containing just the arguments of func
        args_for_func = {k: getattr(args, k) for k in arg_spec.args}
    args.func(**args_for_func)
