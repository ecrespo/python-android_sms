#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Se importa detatime
import datetime
#Se importa schema y tupes de sqlalchemy
from sqlalchemy import schema, types,ForeignKey, Boolean,TIMESTAMP
from sqlalchemy import orm
from sqlalchemy.orm import validates

#Se define metadato.
metadata = schema.MetaData()

#
def now():
    """Se define la funcion que devuelve la hora en el momento de ejecutar"""

    return datetime.datetime.now()

#Definicion  de la tabla mensajes
mensajes_table = schema.Table('mensajes',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('texto',types.Unicode(100),nullable=False),
    )

responsables_table = schema.Table('responsables',metadata,
    schema.Column('responsable',types.Unicode(100),nullable=False,primary_key=True),
    schema.Column('correo',types.String(60),key='email'),
    schema.Column('celular',types.String(11),nullable=False)
    )
#Definicion  de la tabla dispositivos
dispositivos_table = schema.Table('dispositivos',metadata,
    schema.Column('dispositivo',types.String(16),primary_key=True),
    schema.Column('descripcion',types.Unicode(100)),
    schema.Column('estatus',Boolean,default=False)
    )



#Definicion de la tabla contactos
contactos_table = schema.Table('contactos',metadata,
    schema.Column('id',types.Integer,primary_key=True),
    schema.Column('numcel',types.String(11),nullable=False),
    schema.Column('grupo',ForeignKey("grupos.id")),
    schema.Column('contacto',types.Unicode(100),nullable=False),
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
    schema.Column('mensaje',ForeignKey("mensajes.id")),
    schema.Column('grupo',ForeignKey("grupos.id")),
    schema.Column('numcel',types.String(11),nullable=False),
    schema.Column('contacto',ForeignKey("contactos.id")),
    schema.Column('timestamp',TIMESTAMP()),
    schema.Column('estatus',Boolean,default=False)
)

#Asociacion de las tablas al orm
class Mensajes(object):
    """Clase Mensajes"""
    pass
class Contactos(object):
    """Clase contactos"""
    pass

class Bitacora(object):
    """Clase Bitacora"""
    pass
class Dispositivos(object):
    """Clase dispositivos"""
    pass
class Grupos(object):
    """Clase grupos"""
    pass
class Responsables(object):
    """clase responsables"""
    pass

orm.mapper(Contactos, contactos_table)
orm.mapper(Mensajes,mensajes_table)
orm.mapper(Bitacora,bitacora_table)
orm.mapper(Dispositivos,dispositivos_table)
orm.mapper(Grupos,grupos_table)
orm.mapper(Responsables,responsables_table)

