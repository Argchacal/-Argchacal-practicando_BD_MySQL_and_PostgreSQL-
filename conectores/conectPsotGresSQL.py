#descargamos el conector pip psycopg2

import psycopg2

class ClassConexion:
    def ConexionBD():
        try:
            conexion = psycopg2.connect(
                                            user = 'postgres',
                                            password ='',
                                            host='127.0.0.1',
                                            database ='postgres',
                                            port='')
            print("Conectado a la base de datos")
        
        except Exception as error:
            #informa el error de coneccion a base de dato
            print("Error al conectarce a la base de datos{}".format(error))
    ConexionBD()
    


