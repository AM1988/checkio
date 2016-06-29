#!/usr/bin/env python

from __future__ import division


def checkio(data):
    """ https://checkio.org/mission/median/ """
    data.sort()
    if len(data)%2 != 0:
        return data[len(data)//2]
    else:
        return (data[int(len(data)/2)] + data[int(len(data)/2) - 1])/2

print checkio([1, 2, 3, 4, 5]) #3
print checkio([3, 1, 2, 5, 3]) # 3
print checkio([1, 300, 2, 200, 1]) #2
print checkio([3, 6, 20, 99, 10, 15]) # 12.5