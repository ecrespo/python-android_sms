# python-android_sms
Aplicación de envío de SMS con un celular Android conectado al equipo Debian


Cambios en la configuración del celular:
Nunca he logrado realizar el envío de SMS por comandos AT con un móvil Android, pero si lo haces como App debes hacer cambios al sistema, debido a que Android tiene un límite de 100 SMS por hora y si pasas el límite, la aplicacion teléfono se apaga. Por ello, para realizar un SMS Gateway App en Android y no sufrir de ese mal, debes realizar lo siguiente:
- Instalar el binario sqlite3 que me permitira trabajar con la base de datos.
- La base de datos que posee esta configuracion es la siguiente: /data/data/com.android.providers.settings/databases/settings.db
- El campo que estoy buscando es el siguiente sms_outgoing_check_max_count
- Si al campo anterior le quiero eliminar dicha limitacion colocandolo en 0.
- Y la consulta utilizando el comando sqlite3 es la siguiente:
INSERT INTO gservices (name, value) VALUES('sms_outgoing_check_max_count', 0);

