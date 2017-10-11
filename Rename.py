#!/usr/bin/env python
# -*- coding: utf-8 -*- #

import os
from src.utils import normalize_name

dire =  "../Animes/"
all_dir_names = os.listdir(dire)
for dir_name in all_dir_names:
    try:
        os.rename(dire + dir_name, dire + normalize_name(dir_name))
    except Exception as e:
        print(e)
