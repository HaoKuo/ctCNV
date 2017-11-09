""" test2.py  """
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import os
import logging
import sys
#import argparse
import fire

import numpy as np
import pandas as pd

#import matplotlib.pyplot as plt

from case.tabio import *


#print "hello world"
#def _cmd_target(args):
#    regions = tabio.read_auto(args.interval)

class Date(object):
    day = 0
    month = 0 
    year = 0
    def __init__(self, day=0, month=0, year=0):
        self.day = 0
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1


def test(arg):
    print "Hello "+str(arg)


def main():
    fire.Fire(test)
    date2 = Date.from_string('11-09-2012')
    print date2

if __name__ == "__main__":
    main()
