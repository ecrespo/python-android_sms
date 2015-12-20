#!/usr/bin/env python
# -*- coding: utf-8 -*-


from sqlalchemy import *
import datetime

#Se crea la instancia de la base de datos.
db = create_engine('sqlite:///sms.db')
#Se desactiva el eco.
db.echo = False

#Se instancia metadato.
metadata = MetaData(db)

#Funcion que devuelve la hora en el momento que se ejecuta la funcion.
def now():
    return datetime.datetime.now()



#Se crea la tabla contactos tal cual el mismo ejemplo de
#sqlite.

mensajes = Table(
    'mensajes',metadata,
    Column('id',Integer,primary_key=True),
    Column('texto',Unicode(144)))


grupos = Table(
    'grupos',metadata,
    Column('id',Integer,primary_key=True),
    Column('nombre',Unicode(100)))


contactos = Table(
    'contactos',metadata,
    Column('id',Integer,primary_key=True),
    Column('numcel',String(11)),
    Column('grupo',Unicode(100)),
    Column('contacto',Unicode(100)))


#Definicion de la tabla bitacora
bitacora = Table(
    'bitacora',metadata,
    Column('id',Integer,primary_key=True),
    Column('grupo',Unicode(100)),
    Column('mensaje',Unicode(144)),
    Column('timestamp',TIMESTAMP(), default=now()),
    Column('numcel',String(11)),
    Column('estatus',Boolean,default=False))




#Se crea todas las tablas.
metadata.create_all()

