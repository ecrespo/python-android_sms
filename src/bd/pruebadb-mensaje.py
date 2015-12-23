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


#Insertar Mensajes:
mensaje1 = model.Mensajes()
mensajes = [{"num":1,"mensaje":u"Esta es una prueba inicial"},{"num":2,"mensaje":u"prueba 2"}]

mensaje1.id = mensajes[0]["num"]
mensaje1.texto = mensajes[0]["mensaje"]
session.add(mensaje1)
session.flush()
session.commit()

mensaje2 = model.Mensajes()
mensaje2.id = mensajes[1]["num"]
mensaje2.texto = mensajes[1]["mensaje"]
session.add(mensaje2)
session.flush()
session.commit()







#Se realiza una consulta a la tabla grupos

print "Consulta inicial de la tabla mensajes"

consulta = session.query(model.Mensajes).all()

for lista in consulta:

    print lista.id,lista.texto


#Borrar un contacto
#session.delete(contacto)

#session.flush()

#session.commit()


