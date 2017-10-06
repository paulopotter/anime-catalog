import os
import yaml


def get_configs():

    new_path = os.path.realpath('./') + '/config.yaml'
    with open(new_path, 'r') as f:
        try:
            config = yaml.load(f)

        except yaml.YAMLError as exc:
            print(exc)

    return config
