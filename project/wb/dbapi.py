# -*- coding: utf-8 -*-
'''- Database api module -'''
import mysql.connector
import logging
from wb import conf
import os
from typing import List, Tuple

logger = logging.getLogger()

# === (B) database operations
_connection = None
def get_connection():
    '''Opens database connection.'''
    global _connection
    if not _connection:
        try:
            _connection = mysql.connector.connect(
                host=conf.db_host,
                user=conf.db_user,
                password=conf.db_pass,
                database=conf.db_name
            )
            if _connection.is_connected():
                #print("Connected to MySQL")
                return _connection
        except mysql.connector.Error as e:
            print(e)         
            logging.error("Error connecting to MySQL: %s", e)
    return _connection


def close_connection():
    '''Closes database connection.'''
    if(get_connection()):
        _connection.close()
    return 0


def execute_in(query, params):
    con = get_connection()
    if con:
        with con.cursor() as _cursor:
            try:
                _cursor.execute(query, params)
                # Commit the transaction
                con.commit()
            except mysql.connector.Error as error:
                logging.error("Error executing SQL insert/update query: %s", error)
                
def executemany_in(query, param_list):
    con = get_connection()
    if con:
        with con.cursor() as _cursor:
            try:
                _cursor.executemany(query, param_list)
                # Commit the transaction
                con.commit()
            except mysql.connector.Error as error:
                logging.error("Error executing SQL multiinsert query: %s", error)                
        
def executescalar_out(query, parameters):
    record = []
    con = get_connection()
    if con:
        with con.cursor() as _cursor:
            try:
                _cursor.execute(query, parameters)
                record = _cursor.fetchone()
            except Exception as e:
                logging.error("Error executing SQL scalar select query: %s", error)                
    return record

def execute_out(query, parameters):
    records = []
    con = get_connection()
    if con:
        with con.cursor() as _cursor:
            try:
                _cursor.execute(query, parameters)
                records = _cursor.fetchall()
            except Exception as e:
                logging.error("Error executing SQL select query: %s", error)                
    return records

# TODO remove      
def get_companies() -> List[Tuple]:
    records = []
    con = get_connection()
    if con:
        with con.cursor() as _cursor:
            query = """
                select companies.id as company_id, 
                api_keys.api_key1 as api_key  
                from companies left join api_keys on companies.id = api_keys.company_id 
                and companies.is_active = 1 
                where api_key1 is not null
            """   
            _cursor.execute(query)
            records = _cursor.fetchall()
    return records

__all__ = [ 'get_connection', 'close_connection' ]

# === (E) database operations