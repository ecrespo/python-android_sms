#!/usr/bin/env python

"""
Script de pruebas de base de datos con sqlalchemy
Tabla bitacora
"""
import datetime

import model
from sqlalchemy import orm
from sqlalchemy import create_engine


#
def now():
    """Funcion que devuelve la hora en el momento que se ejecuta la funcion."""
    return datetime.datetime.now()



#Crear un engine y crear todas las tablas necesarias

#Se instancia el engine con la base de datos sms.db deshabilitando el eco.
engine = create_engine('sqlite:///sms.db', echo=False)

#Se define el metadato y se crea
model.metadata.bind = engine
model.metadata.create_all()

#Se crea la session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)
session = orm.scoped_session(sm)


#Insertar un responsable:
bitacora1 = model.Bitacora()
bitacora1.id = 1
bitacora1.mensaje = 1
bitacora1.grupo = 1
bitacora1.numcel = "04265673018"
bitacora1.contacto = 1
bitacora1.timestamp = now()
bitacora1.estatus = True


session.add(bitacora1)

session.flush()

session.commit()

#Insertar un responsable:
bitacora2 = model.Bitacora()
bitacora2.id = 2
bitacora2.mensaje = 2
bitacora2.grupo = 2
bitacora2.numcel = "04275673018"
bitacora2.contacto = 2
bitacora2.timestamp = now()
bitacora2.estatus = False


session.add(bitacora2)

session.flush()

session.commit()

#Insertar un responsable:
bitacora3 = model.Bitacora()
bitacora3.id = 3
bitacora3.mensaje = 3
bitacora3.grupo = 3
bitacora3.numcel = "04245673018"
bitacora3.contacto = 3
bitacora3.timestamp = now()
bitacora3.estatus = True


session.add(bitacora3)

session.flush()

session.commit()





#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla contactos"

consulta = session.query(model.Bitacora).all()

for lista in consulta:

    print lista.id,lista.mensaje,lista.grupo,lista.numcel,lista.contacto,lista.timestamp,lista.estatus
    

print "--------------------------------"





