#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import io
import os
import argparse
import inspect

from src.msg import error_msg, info_msg
from src.animes import AnimeLib
from src.parse import Parse
from src.utils import normalize_name


def cataloguer(folder_name, description_file):
    from src.cataloguer import Cataloguer
    from src.createFile import CreateFile

    cataloguer = Cataloguer(folder_name, description_file)
    create_file = CreateFile()
    data = cataloguer.prepared_content()
    create_file.create_js_file(data)


def parse(list_type, file, path, create_folder, override, only, starts_with, ends_with, just_with):

    if list_type == '' or file == '':
        error_msg('list type or file/path is empty')
        return False

    anime_list = []

    path = path + '/' if path and path[-1] != '/' else path
    if list_type == 'list':
        with io.open(file, 'r', encoding='utf-8') as f:
            for anime in f.readlines():
                anime_name = anime.split('/', 4)[-1][:-1]
                anime_list.append(anime_name)

    elif list_type == 'folder':
        from src.cataloguer import Cataloguer

        cataloguer = Cataloguer(path, 'dummy')
        anime_list = cataloguer.get_all_folders(path)

    else:
        error_msg('unrecognized list type. Please use < list > or < folder >')
        return False

    parse_settings = [list_type, path, create_folder, override, only]
    anime_list = search_limit(anime_list, starts_with, ends_with, just_with)
    know_animes = AnimeLib().data

    Parse(anime_list, know_animes, parse_settings)


def search_limit(anime_list, starts_with, ends_with, just_with):
    if starts_with or (starts_with and ends_with) or just_with:
        if just_with:
            starts_with = just_with
            ends_with = just_with

        anime_list = sorted(anime_list)
        alphanumeric = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        starts_index = alphanumeric.index(starts_with)
        ends_index = alphanumeric.index(ends_with or "9")

        for word in anime_list[:]:
            if not word.lower().startswith(tuple(alphanumeric[starts_index:ends_index + 1])):
                anime_list.remove(word)

    return anime_list


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
