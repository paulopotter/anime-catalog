#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from termcolor import colored


def error_msg(msg, tab=False):
    t = '\t' if tab else ''
    print(colored(t + '[ERROR]', 'red') + ': ' + msg)


def warning_msg(msg, tab=False):
    t = '\t' if tab else ''
    print(colored(t + '[WARNING]', 'yellow') + ': ' + msg)


def info_msg(msg, tab=False):
    t = '\t' if tab else ''
    print(colored(t + '[INFO]', 'cyan') + ': ' + msg)


def simple_msg(msg, color='green', msg2='', tab=False):
    t = '\t' if tab else ''
    print(t + colored(msg, color) + '' + str(msg2))
