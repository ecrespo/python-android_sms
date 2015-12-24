#!/usr/bin/env python

"""
Script de pruebas de base de datos con sqlalchemy
"""
import model
from sqlalchemy import orm
from sqlalchemy import create_engine



#Crear un engine y crear todas las tablas necesarias

#Se instancia el engine con la base de datos sms.db deshabilitando el eco.
engine = create_engine('sqlite:///sms.db', echo=False)

#Se define el metadato y se crea
model.metadata.bind = engine
model.metadata.create_all()

#Se crea la session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)
session = orm.scoped_session(sm)


#Insertar dispositivos:
dispositivos = model.Dispositivos()

dispositivos.dispositivo = "0403725B09015010" 
dispositivos.descripcion = u"Celular motorola"
dispositivos.estatus = True


session.add(dispositivos)

session.flush()

session.commit()






#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla Dispositivos"

consulta = session.query(model.Dispositivos).all()

for lista in consulta:

    print lista.dispositivo,lista.descripcion,lista.estatus



