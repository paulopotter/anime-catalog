#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import io
import argparse
import inspect
import yaml

from slugify import slugify


def try_parse(host, uris, anime, searching=True):
    from src.parseUrl import Parse

    parse = Parse(host, uris[0] + anime)
    print('\t{}{}{}'.format(host, uris[0], anime))
    if (parse.parse_name()).strip() in [u'A página não foi encontrada', 'Animes']:
        if len(uris[1::]) > 0:
            return try_parse(host, uris[1::], anime)
        else:
            print('\t[ERROR]: Page  < {} > not found!'.format(anime))

            if searching:
                print('\tTrying to find the anime < {} > '.format(anime))

                from src.findAnime import FindAnime

                search = FindAnime(anime).parse_search()
                if search:
                    print('\t' + str(search))
                    return try_parse(host, [''], search.get(slugify(anime), anime), False)

            return False
    else:
        return parse


def make_parse(parse, anime_name, path, create_folder, override, list_or_folder='list', overrideData=[]):

    data = {
        "name": parse.parse_name(),
        "description": parse.parse_description(),
        "totalEpisodes": parse.parse_total_ep(),
        "genre": parse.parse_genres()
    }

    try:
        slugify_name = slugify(anime_name, separator=' ')
        slugify_name = anime_name[0].upper() + anime_name[1::]
        anime_dir = anime_name if (list_or_folder == 'folder') else slugify_name
        full_path = path + anime_dir

        if overrideData:
            new_data = {}
            for item in overrideData:
                new_data[item] = data[item]

            data = new_data

        def creating_file(overrideData=[]):
            from src.createFile import CreateFile

            create_file = CreateFile()
            create_file.create_json_file(data,
                                         folder_name=full_path,
                                         create_folder=create_folder,
                                         overrideData=overrideData)

        def getting_img():
            parse.get_image(full_path)

        if override:
                creating_file(overrideData)
                getting_img()
        else:

            import os

            try:
                if 'description.json' in os.listdir(path + anime_dir):
                    print('\t< description.json > Alread exists!')
                else:
                    creating_file()
            except OSError:
                creating_file()


            try:
                if 'thumb.png' in os.listdir(path + anime_dir):
                    print('\t< thumb.png > Alread exists!')
                else:
                    getting_img()
            except OSError:
                    getting_img()

    except Exception as e:
        print('\t< {} > can not be done. \n\t[ERROR]: {} \n'.format(data['name'], e))


def cataloguer(folder_name, description_file):
    from src.cataloguer import Cataloguer
    from src.createFile import CreateFile

    cataloguer = Cataloguer(folder_name, description_file)
    create_file = CreateFile()
    data = cataloguer.prepared_content()
    create_file.create_js_file(data)


def parse(list_type, file, path, create_folder, override, only):
    if list_type == '' or file == '':
        print('[ ERROR ]: list type or file/path is empty')
        return False

    configs = get_config()
    host = configs.get('host', '')
    uris = configs.get('uris', '')

    if list_type == 'list':
        with io.open(file, 'r', encoding='utf-8') as anime_list:
            for anime in anime_list.readlines():
                anime_name = anime.split('/', 4)[-1][:-1]
                do_parse(anime_name, host, uris, 'list', path, create_folder, override, only)

    elif list_type == 'folder':
        from src.cataloguer import Cataloguer

        cataloguer = Cataloguer(path, 'dummy')
        anime_list = cataloguer.get_all_folders(path)
        for anime_name in anime_list:
            do_parse(anime_name, host, uris, 'folder', path, create_folder, override, only)

    else:
        print('[ ERROR ] unrecognized list type. Please use < list > or < folder >')
        return False


def do_parse(anime_name, host, uris, type_of_parse, path, create_folder, override, only):
    print('\n- {}:'.format(anime_name))
    parse = try_parse(host, uris, slugify(anime_name))

    if parse:
        make_parse(parse, anime_name, path, create_folder, override, type_of_parse, only)
    else:
        with io.open('not-found.log', 'w+', encoding='utf-8') as log:
            msg = u'< {} > not found!\n'.format(anime_name)
            print(msg)
            log.write(msg)


def get_config():
    with open("config.yaml", 'r') as f:
        try:
            config = yaml.load(f)
        except yaml.YAMLError as exc:
            print(exc)

    return config

# ####


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommand")

    parser_cataloguer = subparsers.add_parser('cataloguer')
    parser_cataloguer.add_argument("--folder_name", default='Animes')
    parser_cataloguer.add_argument("--description_file", default='description.json')
    parser_cataloguer.set_defaults(func=cataloguer)

    parser_parse = subparsers.add_parser('parse')
    parser_parse.add_argument("--list_type", default='list')
    parser_parse.add_argument("--file", default='list.txt')
    parser_parse.add_argument("--path", default='./')
    parser_parse.add_argument("--override", action='store_true', default=False)
    parser_parse.add_argument("--only", action='append', default=[])
    parser_parse.add_argument("--create_folder", action='store_true', default=False)
    parser_parse.set_defaults(func=parse)

    args = parser.parse_args()

    arg_spec = inspect.getargspec(args.func)
    if arg_spec.keywords:
        # # convert args to a dictionary
        args_for_func = vars(args)
    else:
        # # get a subset of the dictionary containing just the arguments of func
        args_for_func = {k: getattr(args, k) for k in arg_spec.args}

    args.func(**args_for_func)
