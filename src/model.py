#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importa detatime
import datetime
#Se importa schema y tupes de sqlalchemy
from sqlalchemy import schema, types
from sqlalchemy import *
from sqlalchemy import orm


#Se define metadato.
metadata = schema.MetaData()

#Se define la funcion que devuelve la hora en el momento de ejecutar
def now():

    return datetime.datetime.now()

#Definicion  de la tabla mensajes
mensajes_table = schema.Table('mensajes',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('texto',types.Unicode(100),nullable=False),
    )

#Definicion  de la tabla mensajes
dispositivos_table = schema.Table('dispositivos',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('dispositivo',types.Integer),
    schema.Column('descripcion',types.Unicode(100),nullable=False),
    schema.Column('estatus',Boolean,default=False)
    )



#Definicion de la tabla contactos
contactos_table = schema.Table('contactos',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('numcel',types.String(11)),
    schema.Column('grupo',types.Unicode(100)),
    schema.Column('contacto',types.Unicode(100)),
    )

#Definicion  de la tabla mensajes
grupos_table = schema.Table('grupos',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('nombre',types.Unicode(100),nullable=False),
    schema.Column('descripcion',types.Unicode(100),nullable=False),
    )



#Definicion de la tabla bitacora
bitacora_table = schema.Table('bitacora',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('mensaje',Unicode(144)),
    schema.Column('grupo',Unicode(100)),
    schema.Column('numcel',String(11)),
    schema.Column('timestamp',TIMESTAMP()),
    schema.Column('estatus',Boolean,default=False)
)

#Asociacion de las tablas al orm
class Mensajes(object): pass
class Contactos(object): pass
class Bitacora(object): pass
class Dispositivos(object):pass
class Grupos(object):pass

orm.mapper(Contactos, contactos_table)
orm.mapper(Mensajes,mensajes_table)
orm.mapper(Bitacora,bitacora_table)
orm.mapper(Dispositivos,dispositivos_table)
orm.mapper(Grupos,grupos_table)

