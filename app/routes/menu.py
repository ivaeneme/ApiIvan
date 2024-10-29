from flask import Blueprint, request, jsonify
from app.utils.db import conexMysql

bp = Blueprint('menu', __name__, url_prefix='/api')

@bp.route('/menu', methods=['GET'])
def obtener_menu():
    try:
        # Acceso a la conexión sin los paréntesis
        con = conexMysql
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
    except Exception as e:
        return jsonify({"error": f"Error al obtener el menú: {str(e)}"}), 500

@bp.route('/insertar', methods=['POST'])
def insertar():
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

@bp.route('/menu/<int:id_plato>', methods=['PUT'])
def actualizar_menu(id_plato):
    try:
        dato = request.get_json()
        nombre = dato.get('nombre')
        precio = dato.get('precio')
        ingredientes = dato.get('ingredientes')
        id_tipoPlato = dato.get('id_tipoPlato')

        cursor = conexMysql.connection.cursor()  # Asegúrate de que `conexMysql` esté bien configurado

        cursor.execute(
            "UPDATE comidas SET nombre = %s, precio = %s, ingredientes = %s, id_tipoPlato = %s WHERE id_plato = %s",
            (nombre, precio, ingredientes, id_tipoPlato, id_plato))
        conexMysql.connection.commit()
        cursor.close()

        return jsonify({"message": "Registro actualizado exitosamente", "id": id_plato}), 200
    except Exception as e:
        return jsonify({"error": f"No se pudo actualizar el registro: {str(e)}"}), 500
