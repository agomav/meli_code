import os
from configuration.configProvider import configurationServer

from sqlalchemy import (
    Column,
    MetaData,
    String,
    DateTime,
    Integer,
    Numeric,
    Table,
    Float,
    
    Text,
    create_engine,
)
from sqlalchemy.sql.sqltypes import Numeric

meta_data=MetaData()

prop=configurationServer()

item=Table(
    "item",
    meta_data,
    Column('site', String(5), primary_key=True),
    Column('id', Integer, primary_key=True),
    Column('price', Float, nullable=True),
    Column('start_time', String(60), nullable=True),
    Column('name', String(20), nullable=True),
    Column('description', String(255), nullable=True),
    Column('nickname', String(20), nullable=True)
)


def init_db_engine(db_uri=None):
    
    uri =prop.getProperty('db_uri_connecttion')
    db_engine = create_engine(uri, convert_unicode=True)
    __create_tables_if_not_exists(db_engine)
    return db_engine


def db_connect(db_engine):
    return db_engine.connect()



def close_db_connection(db_connection):
    try:
        db_connection.close()
    except:
        pass



    

def __create_tables_if_not_exists(db_engine):
    item.create(db_engine, checkfirst=True)


def get_db_connecion():
    db_engine = init_db_engine()
    __create_tables_if_not_exists(db_engine)
    return db_connect(db_engine)