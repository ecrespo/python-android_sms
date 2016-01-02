#!/usr/bin/env python
# -*- coding: utf-8 -*-



import model
from sqlalchemy import orm
from sqlalchemy import create_engine

import datetime


def now():
	"""Retorna la fecha y hora actual"""

    return datetime.datetime.now()





class Crud(object):
	"""Clase que permite hacer las operaciones basicas en base de datos""" 
	def __init__(self,base_de_datos):
		self._db = base_de_datos
		#Se instancia el engine con la base de datos sms.db deshabilitando el eco.
		self._engine = create_engine('sqlite:///%s' %self._db,echo=False)
		#Se define el metadato y se crea
		model.metadata.bind = self._engine
		model.metadata.create_all()

		#Se crea la session
		sm = orm.sessionmaker(bind=self._engine, autoflush=True, autocommit=False, expire_on_commit=True)
		self._session = orm.scoped_session(self._sm)

	def __getattr__(self,attr):
		return None


	@property
	def db(self):
	    return self._db
	
	
    @db.setter
    def db(self,base_de_datos):
    	self._db = base_de_datos

	@staticmethod
	def consulta(tabla):
		"""Hace consulta en la 

			tabla"""
		if tabla == "Contactos":
			consulta = self._session.query(model.Contactos).all()
		elif
		 tabla == "Grupos":
			consulta = self._session.query(model.Grupos).all()
		elif tabla == "Mensajes":
			consulta = self._session.query(model.Mensajes).all()
		elif tabla == "Bitacora":
			consulta = self._session.query(model.Bitacora).all()

		return consulta

	@staticmethod
	def agregar(tabla,dato):
		"""Agrega datos a la tabla"""

		if tabla == "Contactos":
			contacto = model.Contactos()
			contacto.contacto = dato["contacto"]
			contacto.numcel = dato["numcel"]
			contacto.grupo = dato["grupo"]			
			self._session.add(contacto)

		elif tabla == "Grupos":
			grupos = model.Grupos()
			grupos.nombre = dato["nombre"]
			self._session.add(grupos)
			
		elif tabla == "Mensajes":
			mensajes = model.Mensajes()
			mensajes.texto = dato["texto"]
			self._session.add(mensajes)
		elif tabla == "Bitacora":
			bitacora = model.Bitacora()
			bitacora.mensaje = dato["mensaje"]
			bitacora.grupo = dato["grupo"]
			bitacora.numcel = dato["numcel"]
			bitacora.timestamp = dato["timestamp"]
			bitacora.estatus = dato["estatus"]
			self._session.add(bitacora)
		self._session.flush
		self._session.commit()

    @staticmethod
    def borrar_grupo_contactos(grupo):
    	"""Borra un grupo de contactos de la tabla grupo"""
        consulta = self._session.query(model.Contactos).filter(model.Contactos.grupo == grupo).all()
        for cons in consulta:
        	self._session.delete(cons)
        	self._session.flush()
        	self._session.commit()

	@staticmethod
	def borrar(tabla,dato):
		"""Borra un dato de una tabla"""
		if tabla == "Contactos":
			consulta = self._session.query(model.Contactos).filter(model.Contactos.contacto == dato["contacto"]).one()
		elif tabla == "Grupos":
			consulta = self._session.query(model.Grupos).filter(model.Grupos.nombre == dato["nombre"]).one()
		elif tabla == "Mensajes":
			consulta = self._session.query(model.Mensajes).filter(model.Mensajes.texto == dato["texto"]).one()
		elif tabla == "Bitacora":
			consulta = self._session.query(model.Bitacora).filter(model.Bitacora.numcel == dato["numcel"]).one()
		self._session.delete(consulta)
		self._session.flush()
		self._session.commit()

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


	#resultado = crud.Consulta("Contactos")
	#for lista in resultado:
	#	print lista.numcel,lista.contacto,lista.grupo

     #   resultado = crud.Consulta("Grupos")
	#for lista in resultado:
	#	print lista.nombre

	#resultado = crud.Consulta("Mensajes")
	#for lista in resultado:
	#	print lista.texto

	#resultado = crud.Consulta("Bitacora")
	#for lista in resultado:
	#	print lista.mensaje,lista.grupo, lista.numcel,lista.timestamp,lista.estatus

     #   crud.BorrarGrupoContactos("prueba")
	

	#contactos = model.Contactos()
	#contactos.contacto = contacto["contacto"]
	#contactos.numcel = contacto["numcel"]
	#session.add(contactos)
	#session.flush()
	#session.commit()
	#crud.Borrar("Contactos",{"contacto": u"Marisol Buela"})
	resultado = crud.Consulta("Contactos")
	for lista in resultado:
		print lista.numcel,lista.contacto,lista.grupo

