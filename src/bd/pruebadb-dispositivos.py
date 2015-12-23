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


#Insertar un responsable:
responsable = model.Responsables()

responsable.responsable = u"Ernesto Crespo"

responsable.celular = u"04265673018"
responsable.correo = u"ecrespo@gmail.com"
print (type(responsable))

session.add(responsable)

session.flush()

session.commit()






#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla contactos"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.contacto,lista.numcel

print "--------------------------------"





#Agregar un contacto

contacto = model.Contactos()

contacto.contacto = u"Luisa Gonzalez"

contacto.numcel = u"04155555555"
print (type(contacto))

session.add(contacto)

session.flush()

session.commit()


#Se realiza una consulta a la tabla grupos

print "Consulta la tabla contactos con el dato incorporado"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.contacto,lista.numcel

print "--------------------------------"







#Borrar un contacto
#session.delete(contacto)

#session.flush()

#session.commit()

