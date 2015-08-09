#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
"""
Nombre:Interfaz
Descripción: Interfaz grafica de la aplicacion python-android-sms.
Versión:0.1
Licencia:GPLv3
Autor: Ernesto Crespo
correo: ecrespo@gmail.com

contacto = { grupo: "", nombre: "", descripcion: "", numcel : "" }
mensaje = { mensaje: ""}


bitacora= {grupo:"",mensaje:"", timestamp: timestamp, numcel: "", estatus: true}


"""
#Import gtk and webkit


import gtk
from use_config import config 
from validar_num import validar 

from bdd import *


#Importando el módulo android
#import android


    
#class App
class App:
    def __init__(self):
        sel.__bdd = Crud()
        self.__texto = ""
        self.__configFile = "../conf/python_android_sms.conf"
        self.__conf = config(self.__configFile)
        self.__host = self.__conf.ShowValueItem("wifi","ip")
        self.__puerto = self.__conf.ShowValueItem("wifi","puerto")
        self.__responsable_nombre = self.__conf.ShowValueItem("responsable","nombre")
        self.__responsable_celular = self.__conf.ShowValueItem("responsable","celular")
        self.__responsable_correo = self.__conf.ShowValueItem("responsable","correo")
        self.__contactos = {}
        self.__grupo = ""
        #Constructor
        #Se asocia el archivo glade al Builder
        self.glade_file = "../ui/interfaz.glade"
        self.glade = gtk.Builder()
        self.glade.add_from_file(self.glade_file)
        #Se asocia la ventana 
        self.window = self.glade.get_object('window1')
        self.window.set_default_size(600, 400)
        self.window.set_title("PyAndroidSMS")

        #Se asocia el botón salir
        self.bsalir1 = self.glade.get_object('bsalir1')
        #Widgets primera pestgna
        self.benviar = self.glade.get_object('benviar')
        self.eMensaje = self.glade.get_object('eMensaje')
        self.cbListaMensajes = self.glade.get_object('cbListaMensajes')
        self.rMensaje = self.glade.get_object('rMensaje')
        self.rListaMensajes = self.get_object('rListaMensajes')
        self.rCelular = self.get_object('rCelular')
        self.rGrupo = self.get_object('rGrupo')
        self.eCelular = self.get_object('eCelular')
        self.cbGrupo = self.get_object('cbGrupo')
        self.cbCelular = self.get_object('cbCelular')
        #widgets segunda pestagna
        #botones de radio
        self.rMensajeMasivo = self.get_object('rMensajeMasivo')
        self.rListaMensaje = self.get_object('rListaMensaje')

        self.eMensajeMasivo = self.get_object('eMensajeMasivo')
        self.cbListaMensajeMasivo = self.get_object('cbListaMensajeMasivo')

        #Agregar mensajes al combo
        self.__consulta = self.__bdd.Consulta("Mensajes")
        for lista in self.__consulta:
            self.cbListaMensajeMasivo.append_text(lista.texto)


        self.cbGrupoMasivo = self.get_object('cbGrupoMasivo')
        
        #Se agrega los grupos al combo
        self.__consulta = self.__bdd.Consulta("Grupos")
        for lista in self.__consulta:
            self.cbGrupoMasivo.append_text(lista.nombre)


        self.benviarmasivo = self.get_object('benviarmasivo')


        #widgets tercera pestagna
        self.eNombreGrupo = self.get_object('eNombreGrupo')
        self.eAgregarNumero = self.get_object('eAgregarNumero')
        self.eNombre = self.get_object('eNombre')
        self.lMensajeNumero = self.get_object('lMensajeNumero')
        self.cbGrupoEliminar = self.get_object('cbGrupoEliminar')

        #Se agrega los grupos al combo
        self.__consulta = self.__bdd.Consulta("Grupos")
        for lista in self.__consulta:
            self.cvGrupoEliminar.append_text(lista.nombre)

        self.bagregar = self.get_object('bagregar')
        self.bGuardarGrupo = self.get_object('bGuardarGrupo')
        self.bEliminarGrupo = self.get_object('bEliminarGrupo')
        #widgets cuarta pestagna
        self.eMensajeAgregar = self.get_object('eMensajeAgregar')
        self.cbMensajeEliminar = self.get_object('cbMensajeEliminar')
        #Se agrega los mensajes al combo
        self.__consulta = self.__bdd.Consulta("Mensajes")
        for lista in self.__consulta:
            self.cbMensajeEliminar.append_text(lista.texto)

        #Falta agregar los mensajes 
        self.bagregarmsg = self.get_object('bagregarmsg')
        self.bEliminarMensaje = self.get_object('bEliminarMensaje')
        #widgets quinta pestagna
        self.rWifi = self.get_object('rWifi')
        self.rUsb = self.get_object('rUsb')
        self.eHostIP = self.get_object('eHostIP')
        self.ePuertoHost = self.get_object('ePuertoHost')
        self.eNombreResponsable = self.get_object('eNombreResponsable')
        self.eCelularResponsable = self.get_object('eCelularResponsable')
        self.eCorreoResponsable = self.get_object('eCorreoResponsable')
        self.eHostIP.set_Text(self.__host)
        self.ePuertoHost.set_Text(self.__puerto)
        self.eNombreResponsable.set_Text(self.__responsable_nombre)
        self.eCelularResponsable.set_Text(self.__responsable_celular)
        self.eCorreoResponsable.set_Text(self.__responsable_celular)
        self.bguardarconf = self.get_object('bguardarconf')


        #Se asocia el evento destruir a la ventana principal.
        self.window.connect("destroy",self.window1_destroy_cb)
        #Se asocia el boton salir
        self.bsalir1.connect("clicked",self.bsalir1_clicked_cb)
        #Se asocia el boton enviar 
        self.benviar.connect("clicked",self.benviar_clicked_cb)
        #envio masivo
        self.benviarmasivo.connect("clicked",self.benviarmasivo_clicked_cb)
        #Se asocia el boton agnadir
        self.bagregar.connect("clicked",self.bagregar_clicked_cb)
        self.bGuardarGrupo.connect("clicked",self.bGuardarGrupo_clicked_cb)
        self.bEliminarGrupo.connect("clicked",self.bEliminarGrupo_clicked_cb)
        self.bagregarmsg.connect("clicked",self.bagregarmsg_clicked_cb)
        self.bEliminarMensaje.connect("clicked",self.bEliminarMensaje_clicked_cb)
        self.bguardarconf.connect("clicked",self.bguardarconf_clicked_cb)
        self.rWifi.connect("toggled",self.on_on_rWifi_toggled)
        self.rUsb.connect("toggled",self.on_rUsb_toggled)
        self.cbMensajeEliminar.connect("changed",self.cbMensajeEliminar_changed_cb)
        self.rMensajeMasivo.connect("toggled",self.rMensajeMasivo_toggled_cb)
        self.rListaMensaje.connect("toggled",self.rListaMensaje_toggled_cb)


        
        #Se muestra la ventana principal de la aplicación
        self.window.show_all()


    def benviarmasivo_clicked_cb(self):
        if self.rListaMensaje.get_active():
            self.__mensaje = self.cbListaMensajeMasivo.get_active_text()
        elif self.rMensajeMasivo.get_active():
            self.__mensaje = self.eMensajeMasivo.get_text()

        self.__grupo = self.cbGrupoMasivo.get_active_text()

        self.__enviarMensajes()
    
        

    def rListaMensaje_toggled_cb(self):
        if self.rListaMensaje.get_active():
            self.__mensaje = self.cbListaMensajeMasivo.get_active_text()
        else:
            self.__mensaje = self.eMensajeMasivo.get_text()


    def rMensajeMasivo_toggled_cb(self):
        if self.rMensajeMasivo.get_active():
            self.__mensaje = self.eMensajeMasivo.get_text()
        else:
            self.__mensaje = self.cbListaMensajeMasivo.get_active_text()
        


    # Agrega contactos a una libreta de telefonos
    def bagregar_clicked_cb(self):
        contacto = self.eNombre.get_text()
        telefono = self.eAgregarNumero.get_text()
        self.__grupo = self.eNombreGrupo.get_text()
        val = validar()
        if val.NumCel(telefono) == False:
            self.lMensajeNumero.set_Text(u"Número celular no válido")
        else:
            self.lMensajeNumero.set_Text(u"Número celular válido")
            self.__contactos[contacto] = telefono




    def bGuardarGrupo_clicked_cb(self):
        self.__grupo = self.eNombreGrupo.get_text()
        lista = self.__contactos.keys()
        for item for lista:
            self.__bdd.Agregar("Contactos",{"contacto":self.__contactos[item]}, "numcel": self.__contactos["numcel"],"grupo":self.__contactos["grupo"])
        

    def bEliminarGrupo_clicked_cb(self):
        self.__grupo = self.cbGrupoEliminar.get_active_text()
        self.__bdd.Borrar("Grupos",{"nombre": self.__grupo})
        self.__bdd.BorrarGrupoContactos(self.__grupo)
        

    
    def cbMensajeEliminar_changed_cb(self):
        self.__mensaje = self.cbMensajeEliminar.get_active_text()
        self.__bdd.Borrar("Mensajes",{"texto": self.__mensaje})
        



    def bagregarmsg_clicked_cb(self):
        self.__texto = self.eMensajeAgregar.get_text()
        self.__bdd.Agregar("Mensajes",{"texto": self.__texto})
        



    def bEliminarMensaje_clicked_cb(self):
        self.__bdd.Borrar("Mensajes",{"contacto": self.__texto})



    def window1_destroy_cb(self):
        self.__conf.write()
        gtk.main_quit()

    def bsalir1_clicked_cb(self):
        self.__conf.write()
        gtk.main_quit()

    def bguardarconf_clicked_cb(self):
        
        if self.rUsb.get_active() == True:
            self.__puerto = self.ePuertoHost.get_text()
            self.__conf.change("conexion","tipo","usb")
            self.__conf.change("usb","puerto",self.__puerto)
        elif self.rWifi.get_active() == True:
            self.__conf.change("conexion","tipo","wifi")
            self.__puerto = self.ePuertoHost.get_text()
            self.__host =  self.eHostIP.get_text()
            self.__conf.change("wifi","ip",self.__host)
            self.__conf.change("wifi","puerto",self.__puerto)
        if validar.NumCel(self.__responsable_celular) == 1:
            self.__responsable_nombre = self.eNombreResponsable.get_text()
            self.__responsable_celular = self.eCelularResponsable.get_text()
            self.__responsable_correo = self.eCorreoResponsable.get_text()
            
        else:
            self.__responsable_nombre = self.eNombreResponsable.get_text()
            self.__responsable_celular = ""
            self.__responsable_correo = self.eCorreoResponsable.get_text()
            
        
        self.__conf.change("responsable","nombre",self.__responsable_nombre)
        self.__conf.change("responsable","correo",self.__responsable_correo)
        self.__conf.change("responsable","celular",self.__responsable_celular)
        self.conf.write()






