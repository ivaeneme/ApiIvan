from flask import jsonify, request
from app.utils.db import conexMysql

class Menu:
    def __init__(self, id_plato, nombre, precio, ingredientes, id_tipoPlato):
        self.id_plato = id_plato
        self.nombre = nombre
        self.precio = precio
        self.ingredientes = ingredientes
        self.id_tipoPlato = id_tipoPlato

    @staticmethod
    def obtener_menu():
        con = conexMysql()
        cursor = con.connection.cursor()
        query = "SELECT * FROM comidas"
        cursor.execute(query)

        resultado = cursor.fetchall()

        menu_items = []
        for row in resultado:
            post = {
                'nombre': row[1],
                'precio': row[2],
                'ingredientes': row[3],

            }
            menu_items.append(post)

        # Cerrar el cursor
        cursor.close()

        # Devolver los resultados como JSON
        return jsonify(menu_items)

    def insertar(self):
        try:
            dato = request.get_json()
            nombre = dato.get('nombre')
            precio = dato.get('precio')
            ingredientes = dato.get('ingredientes')
            id_tipoPlato = dato.get('id_tipoPlato')
            cursor = conexMysql.connection.cursor()
            cursor.execute("INSERT INTO comidas (nombre, precio, ingredientes, id_tipoPlato) VALUES (%s, %s, %s, %s)",
                           (nombre, precio, ingredientes, id_tipoPlato))
            conexMysql.connection.commit()
            cursor.close()

            return jsonify({"message": "Registro agregado exitossamente", "nombre": nombre}), 201
        except Exception as e:
            return jsonify({"error": f"No se pudo agregar el registro: {str(e)}"}), 400  # Respuesta de error