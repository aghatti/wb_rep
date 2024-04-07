# -*- coding: utf-8 -*-
'''- Utility functions -'''

import os
from datetime import datetime, timedelta
import logging

logger = logging.getLogger()

# string to date
def strToDt(_str):
   '''Converts string to date.'''
   return datetime.strptime(_str, '%Y-%m-%d %H:%M:%S')

# date to string
def dtToStr(_dt):
   '''Converts date to string.'''
   return _dt.strftime('%Y-%m-%d %H:%M:%S')
   
# date to file name strint
def dtToFilename(_dt):
   '''Converts date to string for using in file names.'''
   return _dt.strftime('%Y-%m-%d-%H-%M-%S')   

# split array by groups of n elements
def split(a, N):
   '''Splits array by groups of N elements.'''
   return [a[i:i+N] for i in range(0,len(a),N)]

# RESERVED merge files to fname
#def merge_files(fname, files):
#    with open(conf.outdir + fname,'wb') as wfd:
#            for f in files:
#                with open(conf.outdir + f,'rb') as fd:
#                    shutil.copyfileobj(fd, wfd)