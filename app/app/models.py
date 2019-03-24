#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017-09-22 michael_yin
#
from datetime import datetime
from sqlalchemy import create_engine, Column, Table, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, SmallInteger, String, Date, DateTime, Float, Boolean, Text, LargeBinary)

from scrapy.utils.project import get_project_settings

DeclarativeBase = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)

class KitamuraUsedDB(DeclarativeBase):
    __tablename__ = "used_kitamura"

    id = Column(Integer, primary_key=True)
    ac = Column('ac', String(100))
    maker = Column('maker', String(100))
    name = Column('name', String(100))
    price = Column('price', String(100))
    shop = Column('shop', String(100))
    state = Column('state', String(100))
    date = Column('date', String(100))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

class MapcameraUsedDB(DeclarativeBase):
    __tablename__ = "used_mapcamera"

    id = Column(Integer, primary_key=True)
    mapcode = Column('mapcode', String(100))
    jancode = Column('jancode', String(100))
    maker = Column('maker', String(100))
    name = Column('name', String(100))
    price = Column('price', String(100))
    state = Column('state', String(100))
    point = Column('point', String(100))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)


