#!/usr/bin/env python


def checkio(data):
    """https://checkio.org/mission/house-password"""
    data = str(data)
    if len(data) < 10:
        return False
    if data.isdigit():
        return False
    if data.isalpha():
        return False
    if data.islower():
        return False
    if data.isupper():
        return False
    else:
        return True


print checkio('A1213pokl') # False
print checkio('bAse730onE') # True
print checkio('asasasasasasasaas') # False
print checkio('QWERTYqwerty') # False
print checkio('123456123456') # False
print checkio('QwErTy911poqqqq') # True