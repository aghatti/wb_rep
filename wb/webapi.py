# -*- coding: utf-8 -*-
'''- webapi module -'''

import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs


def curlGet(api_key, url, data=None):
        response = requests.get(url, params=data, headers={'Content-Type': 'application/json', 'Authorization': api_key})
        response.raise_for_status()
        return response.json()

def curlPost(api_key, url, data=None):
    response = requests.post(url, json=data, headers={'Content-Type': 'application/json', 'Authorization': api_key})
    response.raise_for_status()
    return response.json()


def url_post(url, auth_key, query):
    '''Makes post request to Langraf clickhouse database to get data.'''
    try:
        with requests.Session() as s:           
            s.auth = (ch_usr, ch_pass)
            resdata = s.post(ch_url, data = query)
            if(debug == 1):
               logger.info('CH query: ' + query)
            decoded_content = resdata.content.decode('utf-8')
            return decoded_content
    except requests.exceptions.RequestException as e:  
        print("Error ", e)
        logger.error(str(e))
        return None
        
def url_get(url, auth_key):
    return None