#!/usr/bin/env python
# -*- coding: utf-8 -*-



import model
from sqlalchemy import orm
from sqlalchemy import create_engine
from sqlalchemy import *

import datetime


def now():

    return datetime.datetime.now()



#Crear un engine y crear todas las tablas necesarias

engine = create_engine('sqlite:///sms.db', echo=False)

model.metadata.bind = engine

model.metadata.create_all()


#Se instancia el engine con la base de datos sms.db deshabilitando el eco.
engine = create_engine('sqlite:///sms.db', echo=False)

#Se define el metadato y se crea
model.metadata.bind = engine
model.metadata.create_all()

#Se crea la session
sm = orm.sessionmaker(bind=engine, autoflush=True, autocommit=False, expire_on_commit=True)
session = orm.scoped_session(sm)


class Crud:
	def __init__(self):
		pass

	def Consulta(self,tabla):
		if tabla == "Contactos":
			consulta = session.query(model.Contactos).all()
		elif tabla == "Mensajes":
			consulta = session.query(model.Mensajes).all()
		elif tabla == "Bitacora":
			consulta = session.query(model.Bitacora).all()

		return consulta

	def Agregar(self,tabla,dato):

		if tabla == "Contactos":
			contacto = model.Contactos()
			contacto.contacto = dato["contacto"]
			contacto.numcel = dato["numcel"]
			contacto.grupo = dato["grupo"]
			
			session.add(contacto)

		elif tabla == "Mensajes":
			mensajes = model.Mensajes()
			mensajes.texto = dato["texto"]
			session.add(mensajes)
		elif tabla == "Bitacora":
			bitacora = model.Bitacora()
			bitacora.mensaje = dato["mensaje"]
			bitacora.grupo = dato["grupo"]
			bitacora.numcel = dato["numcel"]
			bitacora.timestamp = dato["timestamp"]
			bitacora.estatus = dato["estatus"]
			session.add(bitacora)
		session.flush
		session.commit()

	def Borrar(self,tabla,dato):
		if tabla == "Contactos":
			consulta = session.query(model.Contactos).filter(model.Contactos.contacto == dato["contacto"]).one()
		elif tabla == "Mensajes":
			consulta = session.query(model.Mensajes).filter(model.Mensajes.texto == dato["texto"]).one()
		elif tabla == "Bitacora":
			consulta = session.query(model.Bitacora).filter(model.Bitacora.numcel == dato["numcel"]).one()
		session.delete(consulta)
		session.flush()
		session.commit()

if __name__ == "__main__":
	crud = Crud()
	#contacto = {"contacto": u"Marisol Buela" , "numcel": u"0555555555"}
	#mensaje = {"texto": u"Está es una prueba de envío de sms"}
	#grupo = {"nombre": u"prueba"}
	#bitacora = {"mensaje": mensaje["texto"],"grupo": grupo["nombre"],"numcel": contacto["numcel"], "timestamp": now(),"estatus": True}
	
	#crud.Agregar("Contactos",contacto)
	#crud.Agregar("Grupos",grupo)
	#crud.Agregar("Mensajes", mensaje)
	#crud.Agregar("Bitacora",bitacora)


	resultado = crud.Consulta("Contactos")
	for lista in resultado:
		print lista.numcel,lista.contacto, lista.grupo

  
	resultado = crud.Consulta("Mensajes")
	for lista in resultado:
		print lista.texto

	resultado = crud.Consulta("Bitacora")
	for lista in resultado:
		print lista.mensaje,lista.grupo, lista.numcel,lista.timestamp,lista.estatus


	#crud.Borrar("Contactos",{"contacto": u"Marisol Buela"})
	#resultado = crud.Consulta("Contactos")
	#for lista in resultado:
	#	print lista.numcel,lista.contacto

