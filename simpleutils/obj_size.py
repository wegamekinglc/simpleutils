#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import getsizeof


def size_KB(python_obj):
    return float(getsizeof(python_obj, default=0)) / 1000.0

def size_MB(python_obj):
    return float(getsizeof(python_obj, default=0)) / 1000000.0

def size_GB(python_obj):
    return float(getsizeof(python_obj, default=0)) / 1000000000.0

