# -*- coding: utf-8 -*-
'''- Sync stats module -'''

import logging
import time
import datetime
import pprint

from .. import dbapi
from .. import webapi

logger = logging.getLogger()
pp = pprint.PrettyPrinter(indent=4)

def run_sync(api_key, company_id):    
    return None