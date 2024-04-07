# -*- coding: utf-8 -*-
'''- Sync campaign stats module -'''

import logging
import time
import datetime
import json
import pprint

from .. import dbapi
from .. import webapi

logger = logging.getLogger()
pp = pprint.PrettyPrinter(indent=4)

def run_sync(api_key, company_id):
    url = "https://advert-api.wb.ru/adv/v2/fullstats"
    # Get current date
    current_date_obj = datetime.datetime.now().date()
    current_date = current_date_obj.strftime('%Y-%m-%d')
    # TEST 
    #current_date ="2024-04-07"
    # Get campaigns
    query_read_campaigns = """
    SELECT advert_id FROM campaigns WHERE company_id=%s AND status IN (7,9,11);
    """
    query = """
    INSERT INTO campaign_stats
    (advert_id, stat_date, app_type, card_nmID, name, views, clicks, ctr, cpc, sum, atbs, orders, cr, shks, sum_price)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        views = VALUES(views),
        clicks = VALUES(clicks),
        ctr = VALUES(ctr),
        cpc = VALUES(cpc),
        sum = VALUES(sum),
        atbs = VALUES(atbs),
        orders = VALUES(orders),
        cr = VALUES(cr),
        shks = VALUES(shks),
        sum_price = VALUES(sum_price);
    """
    params = []
    params.append(company_id)
    r_campaigns = dbapi.execute_out(query_read_campaigns, params)
    data = []
    # Make api data parameter with all campaigns
    for r_campaign in r_campaigns:
        campaign_id = r_campaign[0]
        
        data_entry = {"id": campaign_id, "dates": [current_date]}
        data.append(data_entry)
    
        # TEST
        #campaign_id = 11411467
        #data_dict = {'id': campaign_id, 'dates': [current_date]}                
        #data = json.dumps([data_dict])                

    j_data = {}
    if len(data) > 0:
        # Get stats for campaigns   
        j_data = webapi.curlPost(api_key, url, data)
        if 'errors' in j_data:
            logging.info('Run sync_stats errors: ' + ', '.join(j_data['errors']))
        if 'code' in data and data['code'] == 429:
            time.sleep(61)
            j_data = webapi.curlPost(api_key, url, data)

        if 'errors' in data:
            logging.info('Run sync_stats errors: ' + ', '.join(j_data['errors']))

        if 'code' in j_data and j_data['code'] == 429:
            time.sleep(61)
            j_data = webapi.curlPost(api_key, url, data)
    if not j_data:
        return None
    #pp.pprint(j_data)
    param_list=[]
    for entry in j_data:
        advert_id = entry["advertId"]
        # Iterate over "nm" values within "apps" list
        for day in entry["days"]:
            for app in day["apps"]:
                app_type = app["appType"]
                for nm_value in app["nm"]:
                    # Extract nm values
                    nm_name = nm_value["name"]
                    nm_id = nm_value["nmId"]
                    views = nm_value["views"]
                    clicks = nm_value["clicks"]
                    ctr = nm_value["ctr"]
                    cpc = nm_value["cpc"]
                    nm_sum = nm_value["sum"]
                    atbs = nm_value["atbs"]
                    orders = nm_value["orders"]
                    cr = nm_value["cr"]
                    shks = nm_value["shks"]
                    sum_price = nm_value["sum_price"]
                    
                    params_tuple = (advert_id, current_date, app_type, nm_id, nm_name, views, clicks, ctr, cpc, nm_sum, atbs, orders, cr, shks, sum_price)
                    param_list.append(params_tuple)
                    #print(" NM Name:", nm_name)
                    #print(" NM ID:", nm_id)
    if len(param_list) > 0:
        dbapi.executemany_in(query, param_list)
    
    return None