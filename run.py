#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import argparse
import inspect


def cataloguer():
    pass


def parse(list_type, file_or_path, create_folder):
    if list_type == '' or file_or_path == '':
        print '[ Error ]: list type or file/path is empty'
        return False

    # Import only necessary
    import io

    from createFile import CreateFile
    from parseUrl import Parse

    host = 'https://www.anbient.com/'

    if list_type == 'list':

        with io.open(file_or_path, 'r', encoding='utf-8') as anime_list:
            for anime in anime_list.readlines():

                uri = anime.split('/', 3)[-1]
                parse = Parse(host, uri[:-1])

                data = {"name": parse.parse_name(),
                        "description": parse.parse_description(),
                        "totalEpisodes": parse.parse_total_ep(),
                        "genre": parse.parse_genres()
                        }
                try:
                    create_file = CreateFile()
                    create_file.create_json_file(data,
                                                 folder_name=data['name'],
                                                 create_folder=create_folder)
                    parse.get_image(data['name'])
                except Exception as e:
                    print '< {} > nao pode ser realizado. \n[ERROR]: {} \n'.format(data['name'], e)
    elif list_type == 'folder':

        from slugify import slugify

        from cataloguer import Cataloguer

        cataloguer = Cataloguer(file_or_path, 'dummy')
        anime_list = cataloguer.get_all_folders(file_or_path)
        anime_list.pop(0)
        for anime in anime_list:
                uri = 'tv/' + slugify(anime)
                parse = Parse(host, uri)

                data = {"name": parse.parse_name(),
                        "description": parse.parse_description(),
                        "totalEpisodes": parse.parse_total_ep(),
                        "genre": parse.parse_genres()
                        }
                try:
                    create_file = CreateFile()
                    create_file.create_json_file(data,
                                                 folder_name=anime,
                                                 create_folder=create_folder)
                    parse.get_image(data['name'])
                except Exception as e:
                    print '< {} > nao pode ser realizado. \n[ERROR]: {} \n'.format(anime, e)

    else:
        print '[ERROR] unrecognized list type. Please use < list > or < folder >'
        return False


# ####


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(title="subcommand")

    parser_cataloguer = subparsers.add_parser('cataloguer')
    # parser_cataloguer.add_argument("--list_type", default='list')
    # parser_cataloguer.add_argument("--file_or_path", default='blo.txt')
    parser_cataloguer.set_defaults(func=parse)

    parser_parse = subparsers.add_parser('parse')
    parser_parse.add_argument("--list_type", default='list')
    parser_parse.add_argument("--file_or_path", default='list.txt')
    parser_parse.add_argument("--create_folder", default=False)
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
