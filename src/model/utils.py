import os
import yaml

from .msg import error_msg
from .createFile import CreateFile


def get_configs():

    new_path = os.path.realpath('./') + '/config.yaml'
    with open(new_path, 'r') as f:
        try:
            config = yaml.load(f, Loader=yaml.FullLoader)

        except yaml.YAMLError as exc:
            error_msg(exc)

    return config


def normalize_name(name):
    return name[0].upper() + name[1:].lower()


def names_to_try(original_anime_name):
    animes_names = [original_anime_name]

    if "-and-" in original_anime_name:
        animes_names.append(original_anime_name.replace("-and-", "-e-"))
        animes_names.append(original_anime_name.replace("-and-", "-"))

    if ' ii' in original_anime_name or ' 2 ' in original_anime_name:
        animes_names.append(original_anime_name.replace(" ii", " 2 "))
        animes_names.append(original_anime_name.replace(" 2 ", " ii "))

    return animes_names


def get_all_folders(folder_path):
    create_file = CreateFile()
    all_folders = []
    for content_name in os.listdir(folder_path):
        if create_file.is_folder(folder_path, content_name):
            all_folders.append(content_name)

    return all_folders
