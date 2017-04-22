#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import argparse
import inspect


def cataloguer(folder_name, description_file):
    from cataloguer import Cataloguer
    from createFile import CreateFile

    cataloguer = Cataloguer(folder_name, description_file)
    create_file = CreateFile()
    data = cataloguer.prepared_content()
    create_file.create_js_file(data)


def parse(list_type, file, path, create_folder):
    if list_type == '' or file == '':
        print '[ Error ]: list type or file/path is empty'
        return False

    # Import only necessary
    import io

    from slugify import slugify

    from createFile import CreateFile
    from parseUrl import Parse

    host = 'https://www.anbient.com/'

    if list_type == 'list':

        with io.open(file, 'r', encoding='utf-8') as anime_list:
            for anime in anime_list.readlines():

                uri = anime.split('/', 3)[-1][:-1]
                parse = Parse(host, uri)

                data = {"name": parse.parse_name(),
                        "description": parse.parse_description(),
                        "totalEpisodes": parse.parse_total_ep(),
                        "genre": parse.parse_genres()
                        }
                try:
                    anime_name = slugify(uri.split('/')[1], separator=' ')
                    anime_name = anime_name[0].upper() + anime_name[1::]
                    full_path = path + anime_name
                    create_file = CreateFile()
                    create_file.create_json_file(data,
                                                 folder_name=full_path,
                                                 create_folder=create_folder)
                    parse.get_image(full_path)
                except Exception as e:
                    print '< {} > nao pode ser realizado. \n[ERROR]: {} \n'.format(data['name'], e)

    elif list_type == 'folder':

        from cataloguer import Cataloguer

        cataloguer = Cataloguer(path, 'dummy')
        anime_list = cataloguer.get_all_folders(path)
        for anime in anime_list:
                print anime + '\n'
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
                                                 folder_name=path + anime,
                                                 create_folder=create_folder)
                    parse.get_image(path + data['name'])
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
    parser_cataloguer.add_argument("--folder_name", default='Animes')
    parser_cataloguer.add_argument("--description_file", default='description.json')
    parser_cataloguer.set_defaults(func=cataloguer)

    parser_parse = subparsers.add_parser('parse')
    parser_parse.add_argument("--list_type", default='list')
    parser_parse.add_argument("--file", default='list.txt')
    parser_parse.add_argument("--path", default='./')
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
