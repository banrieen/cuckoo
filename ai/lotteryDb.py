#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : banrieen
# @Function: Lottery DB ORM

from sqlalchemy import create_engine
from sqlalchemy import MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker


class NumDb():
    """ Lottery Db init
    # create database lottery;
    # GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'BigData1018';
    # CREATE TABLE lottery (id int not null primary key,
    #                       date TEXT, 
    #                       name varchar(50),
    #                       lottery json, 
    #                       status int);


    #     loterry = Table('student', metadata,
    #                Column('id', Integer, primary_key=True),
    #                Column('name', String(50), ),
    #                Column('age', Integer),
    #                Column('address', String(10)),
    #    )
    #  """
    def __init__(self):
        # self.conn = sqlite3.connect('lottery.db')
        self.engine = create_engine('mysql://root:BigData1018@122.51.195.199/lottery')
        self.metadata = MetaData(engine)
        # metadata.create_all(engine)

    def __del__(self):
        self.engine.close()
        
    def update_lottery(self, date, name, body, foot, status):
        self.conn.executemany('INSERT OR REPLACE INTO history (date, name, body, foot, status) VALUES({date}, {name}, {body}, {foot}, {status})')
        self.conn.commit()









