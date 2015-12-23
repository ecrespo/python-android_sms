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


responsable.responsable= u"Dayana Carolina"
responsable.correo = u"dayana@gmail.com"
responsable.celular = "04162737373"
session.add(responsable)
session.flush()
session.commit()

responsable2 = model.Responsables()
responsable2.responsable = u"Ernesto Crespo"

responsable2.celular = "04265673018"
responsable2.correo = "ecrespo@gmail.com"

session.add(responsable2)

session.flush()

session.commit()






#Se realiza una consulta a la tabla responsables

print ("Consulta inicial de la tabla responsables")

consulta = session.query(model.Responsables).all()

for lista in consulta:

    print lista.responsable,lista.celular,lista.correo

