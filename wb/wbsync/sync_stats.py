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
    url = "https://advert-api.wb.ru/adv/v1/promotion/count"
    query = """
    INSERT INTO campaigns(company_id, type, status, advert_id, change_time)  
    VALUES (%s, %s, %s, %s, %s) 
    ON DUPLICATE KEY UPDATE change_time = VALUES(change_time);
    """
    
    data = webapi.curlGet(api_key, url)    
    #print(data)
    if 'errors' in data:
        logging.info('Run agentSyncWBSales Errors: ' + ', '.join(data['errors']))
        data['code'] = 429
    if 'code' in data and data['code'] == 429:
        time.sleep(61)
        data = webapi.curlGet(api_key, url)

    if 'errors' in data:
        logging.info('Run agentSyncWBSales Errors: ' + ', '.join(data['errors']))
        data['code'] = 429

    if 'code' in data and data['code'] == 429:
        time.sleep(61)
        data = webapi.curlGet(api_key, url)

    if data and 'adverts' in data and isinstance(data['adverts'], list):
        param_list=[]
        for datum in data['adverts']:
            count = datum['count']
            status = datum['status']
            type = datum['type']
            for advert in datum['advert_list']:
                #pp.pprint(advert)
                advert_id = advert['advertId']
                change_time = advert['changeTime']
                change_time_obj = datetime.datetime.strptime(change_time, '%Y-%m-%dT%H:%M:%S.%f%z')
                # Format the datetime object in the required format for MySQL
                formatted_change_time = change_time_obj.strftime('%Y-%m-%d %H:%M:%S')                
                params_tuple = (company_id, type, status, advert_id, formatted_change_time)
                param_list.append(params_tuple)
            #pp.pprint(datum)
        # Write or update campaigns            
        #pp.pprint(query)
        #pp.pprint(param_list)
        dbapi.executemany_in(query, param_list)
    return None