""" test.py  """
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division

import os
import logging
import sys
import argparse


import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

#plt.ion()
#plt.plot([1, 2])

if not os.environ.get('DISPLAY'):
    import matplotlib
    matplotlib.use("Agg", force=True)

from matplotlib.backends.backend_pdf import PdfPages

plt.ioff()
plt.switch_backend('agg')


parser = argparse.ArgumentParser(description='ctCNV, a python tool for CNV anlaysis of ctDNA.',
        epilog="Contact Hao Guo <guo.hao@genecast.com.cn> for help.")
parser.add_argument('integers', metavar='N', type=int, nargs='+',
        help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
        const=sum, default=max,
        help='sum the integers (default: find the max)')
parser.add_argument('--version', action='version', version='%(prog)s 2.0')

args = parser.parse_args()
print args
#print(args.accumulate(args.integers))


