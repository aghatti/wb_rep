#!/usr/bin/python3.8
# -*- coding: utf-8 -*-

import sys, os
import argparse 
import fcntl 
import json

#import pprint

from datetime import datetime, timedelta
from decimal import Decimal

import logging
from logging import config
from logging.config import dictConfig

import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs

from wb import conf         # configuration
from wb import dbapi        # database connection api
from wb import utils        # utility functions

# synchronization services
from wb.wbsync import sync_campaigns


document_root = os.path.dirname(os.path.abspath(__file__))

# logging config
log_config = {
    "version":1,
    "root":{
        "handlers" : ["console", "file"],
        "level": "DEBUG"
    },
    "handlers":{
        "console":{
            "formatter": "std_out",
            "class": "logging.StreamHandler",
            "level": "DEBUG"
        },
        "file":{
            "formatter":"std_out",
            "class":"logging.handlers.RotatingFileHandler",
            "level":"DEBUG",
            "filename":os.path.join(document_root,"app.log"),
            "mode": "a",
            "maxBytes": 10485760,
            "backupCount": 3
        }
    },
    "formatters":{
        "std_out": {
            "format": "%(asctime)s %(levelname)s : %(module)s : %(funcName)s : %(message)s",
            "datefmt":"%d-%m-%Y %H:%M:%S%z",
        }
    },
}
dictConfig(
 log_config
)

# List of synchronization services
svc_list = {
    "sync_campaigns": sync_campaigns.run_sync
    #,"sync_stats": sync_stats.run_sync    
}


def main():
    '''Main function.'''

    # == Get arguments
    parser = argparse.ArgumentParser(description="Get campaigns")
    parser.add_argument('-d', '--debug', required=False, help='Debug mode', default=False)
    args = parser.parse_args(sys.argv[1:]) 
       
    # == Use locked file to prevent simultaneous script run
    lock = None
    try:
        lock = open(os.path.join(document_root,'lock'), 'w')
        lock.write(str(os.getpid()))
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as error:
        print('Unable to obtain file lock. Process already running.')
        raise SystemExit('Unable to obtain file lock')
        return 0
       
    # Connect to database   
    con = dbapi.get_connection()
    if con is None:
        logger.error("Unable to connect to database")
        return
    
    # Get companies
    r_companies = dbapi.get_companies()
    
    # Run each synchronization service step by step
    for svc_name, svc_function in svc_list.items():
        for r_company in r_companies:
            #print(f"company id {r_company[0]}, company api_key {r_company[1]}.")
            company_id = r_company[0]
            api_key = r_company[1]
            # Call the synchronization function with the required arguments
            svc_function(api_key, company_id)      
    
        # Synchronize company's marketing campaigns        
        #sync_campaigns.run_sync(api_key, company_id) 
    
        
    dbapi.close_connection()

if __name__ == '__main__':
    # initialize logger
    logger = logging.getLogger()    
    main()