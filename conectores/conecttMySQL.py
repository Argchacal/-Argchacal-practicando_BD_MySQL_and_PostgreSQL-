import mysql.connector

class ClassConexion:
    def ConexionBD():
        try:
            conexion = mysql.connector.connect(
                                            user = 'root',
                                            password ='',
                                            host='127.0.0.1',#es igual a localhost
                                            database ='',
                                            port='')#
            print("Conectado a la base de datos")
            return conexion
        except mysql.connector.Error as error:
            #informa el error de coneccion a base de dato
            print("Error al conectarce a la base de datos{}".format(error))
            return conexion
        
        finally:
            conexion.close()
            print("conexion finalizada")
        
    ConexionBD()