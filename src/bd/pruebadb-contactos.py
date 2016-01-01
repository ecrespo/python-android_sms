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


#Insertar un grupo:
grupo1 = model.Grupos()
grupo1.id = 1
grupo1.nombre = "Cenditel"
grupo1.descripcion = "Grupo de trabajo de cenditel"

session.add(grupo1)

session.flush()

session.commit()

grupo2 = model.Grupos()
grupo2.id = 2
grupo2.nombre = "Galba"
grupo2.descripcion = "Grupo de trabajo de galba"
session.add(grupo2)
session.flush()
session.commit()

grupo3 = model.Grupos()
grupo3.id = 3
grupo3.nombre = "DST"
grupo3.descripcion = "Grupo de trabajo de DST"
session.add(grupo3)
session.flush()
session.commit()





#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla contactos"

consulta = session.query(model.Grupos).all()

for lista in consulta:

    print lista.id,lista.nombre,lista.descripcion

print "--------------------------------"

#Agregar contactos.
contacto1 = model.Contactos()
contacto1.id = 1
contacto1.numcel = "04265673018"
contacto1.grupo = grupo1.id
contacto1.contacto = "Ernesto Crespo"
session.add(contacto1)
session.flush()
session.commit()

contacto2 = model.Contactos()
contacto2.id = 2
contacto2.numcel = "04265673019"
contacto2.grupo = grupo2.id
contacto2.contacto = "Dayana Ovalle"
session.add(contacto2)
session.flush()
session.commit()

contacto3 = model.Contactos()
contacto3.id = 3
contacto3.numcel = "04265673020"
contacto3.grupo = grupo3.id
contacto3.contacto = "Luissana Torres"
session.add(contacto3)
session.flush()
session.commit()

#Se realiza una consulta a la tabla contactos

print "Consulta inicial de la tabla contactos"

consulta = session.query(model.Contactos).all()

for lista in consulta:

    print lista.id,lista.numcel,lista.grupo,lista.contacto

print "--------------------------------"
