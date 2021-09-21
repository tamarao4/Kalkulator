# -*- coding: utf-8 -*-
"""Moduo omoguÄ‡ava parsiranje aritmetiÄ�kih izraza."""
import re


__author__ = 'mijicd'


REGEX = r'(?:\d*\.\d+)|(?:\d+)|(?:[()+\-\^/*])'


def tokenize(expression):
    """Funkcija kreira tokene na osnovu zadatog izraza.

    Postupak formiranja liste tokena koristi regularni izraz
    zadat putem REGEX varijable. OmoguÄ‡eno je pronalaÅ¾enje
    sledeÄ‡ih tipova tokena:
        - floating-point vrednosti
        - celobrojne vrednosti
        - operatori +, -, *, /, ^
        - zagrade

    Args:
        expression (string): Izraz koji se parsira.

    Returns:
        list: Lista pronaÄ‘enih tokena.

    Raises:
        AssertionError: Ako izraz nije zadat kao string.
    """
    assert isinstance(expression, str), "Expression should be string!"
    return re.findall(REGEX, expression)


if __name__ == '__main__':
    #
    # key: izraz, value: oÄ�ekivana lista tokena
    #
    test_cases = {
        # test floats
        "3.14   ^2": ['3.14', '^', '2'],
        "(2.08-.03) ^  2": ['(', '2.08', '-', '.03', ')', '^', '2'],

        # test integers
        "2+(3*4)": ['2', '+', '(', '3', '*', '4', ')'],
        "22     56": ['22', '56'],

        # test invalid
        "ab cd": [],
        "10,22": ['10', '22']
    }

    for expression, expected in test_cases.iteritems():
        assert expected == tokenize(expression)
        
    print (tokenize('1+2'))