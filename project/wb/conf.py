# -*- coding: utf-8 -*-
'''- Configuration module -'''

import os
import logging
import configparser

logger = logging.getLogger()
document_root = os.path.dirname(os.path.abspath(__file__))

cfg = configparser.ConfigParser()
cfg.read(os.path.join(document_root,"settings.conf"))

debug = int(cfg["Settings"]["debug"])

db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')
db_user = os.getenv('DB_USERNAME')
db_pass = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_DATABASE')
