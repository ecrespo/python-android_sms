#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import sqlalchemy
import datetime
from sqlalchemy import schema, types,ForeignKey
from sqlalchemy.orm import validates
from sqlalchemy import orm
from sqlalchemy import create_engine,MetaData,Table,Column
from sqlalchemy.types import Integer,Unicode,String,TIMESTAMP,Boolean

#Se crea la instancia de la base de datos.
db = create_engine('sqlite:///sms.db')
#Se desactiva el eco.
db.echo = False

#Se instancia metadato.
metadata = MetaData(db)

#
def now():
    """Funcion que devuelve la hora en el momento que se ejecuta la funcion."""
    return datetime.datetime.now()



#Se crea la tabla contactos tal cual el mismo ejemplo de
#sqlite.

mensajes = Table(
    'mensajes',metadata,
    Column('id',Integer,primary_key=True),
    Column('texto',Unicode(144))
    )

responsables = Table(
    'responsables',metadata,
    Column('responsable',Unicode(100),nullable=False,primary_key=True),
    Column('correo',String(60)),
    Column('celular',types.String(11),nullable=False)
    )

dispositivos = Table(
    'dispositivos',metadata,
    Column('id',Integer,primary_key=True),
    Column('dispositivo',Integer),
    Column('descripcion',Unicode(100),nullable=False),
    Column('estatus',Boolean,default=False)
    )


grupos = Table(
    'grupos',metadata,
    Column('id',Integer,primary_key=True),
    Column('nombre',Unicode(100)),
    Column('descripcion',Unicode(100),nullable=False)
    )


contactos = Table(
    'contactos',metadata,
    Column('id',Integer,primary_key=True),
    Column('numcel',String(11),nullable=False),
    Column('grupo',ForeignKey("grupos.id")),
    Column('contacto',Unicode(100),nullable=False),
    )


bitacora = Table(
    'bitacora',metadata,
    Column('id',Integer,primary_key=True),
    Column('mensaje',ForeignKey("mensajes.id")),
    Column('grupo',ForeignKey("grupos.id")),
    Column('numcel',String(11),nullable=False),
    Column('contacto',ForeignKey("contactos.id")),
    Column('timestamp',TIMESTAMP()),
    Column('estatus',Boolean,default=False)
)




#Se crea todas las tablas.
metadata.create_all()

