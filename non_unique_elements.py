#!/usr/bin/env python

import itertools


def checkio(data):
    """https://checkio.org/mission/non-unique-elements/"""
    selector_list = []
    for char in data:
        selector_list.append(data.count(char))
    return list((d for d, s in zip(data, selector_list) if s != 1))

