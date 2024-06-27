import os
from flask import Flask, request
from flask_cors import CORS
from flask.json import jsonify
from xml.etree import ElementTree as ET
import json
from ClaseLibro import Libro

#CREANDO API
app = Flask(__name__)
cors = CORS(app)

#LISTAS GLOBALES
lista_de_libros = []
lista_de_ids = []

#ENDPOINT DE INICIO
@app.route('/')
def index():
    return "<h1> API INICIADA CORRECTAMENTE! </h1><br\\>"

#ENDPOINT CARGA DE LIBROS --------------------------------------------------------------------------------------------------------------
@app.route('/cargarLibros', methods=['POST'])
def cargar_libros():
    try:
        xml_entrada = request.data.decode('utf-8')
        if xml_entrada == '':
            return jsonify({
                'message' : 'El XML está vacio!',
                'status' : 404 
            }), 404
        xml_entrada = xml_entrada.replace('\n', '')
        root = ET.fromstring(xml_entrada)
        for libro in root:
            id = libro.attrib['id']
            titulo = ''
            autor = ''
            idioma = ''
            categoria = ''
            editorial = ''
            copias = ''
            for sublibro in libro:
                if sublibro.tag == 'titulo':
                    titulo = sublibro.text
                if sublibro.tag == 'autor':
                    autor = sublibro.text
                if sublibro.tag == 'idioma':
                    idioma = sublibro.text
                if sublibro.tag == 'categoria':
                    categoria = sublibro.text
                if sublibro.tag == 'editorial':
                    editorial = sublibro.text
                if sublibro.tag == 'copias':
                    copias = sublibro.text
            nuevo = Libro(id, titulo, autor, idioma, categoria, editorial, copias)
            lista_de_libros.append(nuevo)
        #print(str(lista_de_libros)) IMPRIMIR VALORES DE LA LISTA
        if os.path.exists('./libros.xml'):
            print("El archivo ya existe!")
        if not os.path.exists('./libros.xml'):
            with open('./libros.xml', 'w', encoding='utf-8') as file:
                file.write(xml_entrada)
                file.close()
        return jsonify({
            'message' : 'Libros cargados correctamente',
            'status' : 200
        }), 200

    except Exception as e:
        return jsonify({
            'message' : f'ERROR al cargar los libros: {e}',
            'status' : 404
        }), 404

#ENDPOINT DE VER LIBROS --------------------------------------------------------------------------------------------------------------
@app.route('/verLibros', methods=['GET'])
def ver_libros():
    diccionario_salida = {
        'mensaje' : 'Libros encontrados',
        'libros' : [],
        'status' : 200
    }

    for libro in lista_de_libros:
        diccionario_salida['libros'].append({
            'id' : libro.id,
            'titulo' : libro.titulo,
            'autor' : libro.autor,
            'idioma' : libro.idioma,
            'categoria' : libro.categoria,
            'editorial' : libro.editorial,
            'copias' : libro.copias
        })
        lista_de_ids.append(libro.id)

    crear_json(diccionario_salida)

    return jsonify(diccionario_salida), 200

def crear_json(datos):
    with open('./temp/Salida.json', 'w', encoding='utf-8') as file:
        json.dump(datos, file, ensure_ascii=False, indent=4)

#ENDPOINT DE VER LIBRO POR ID ----------------------------------------------------------------------------------------------------
@app.route('/verLibro/<string:id>', methods=['GET'])
def buscar_libro(id):

    with open('./temp/Salida.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    libro = next((item for item in data['libros'] if item['id'] == id), None)
    libroRaw = str(libro)
    print(libroRaw)

    if libroRaw == "None":
        return jsonify({
            'message' : 'La ID no existe!',
            'status' : 404
        }), 404
    else:
        xml_resultado = json_a_xml(libro, root_tag='Libro')

        return f"<?xml version='1.0' encoding='UTF-8'?> \n {xml_resultado}" , 200
    
def json_a_xml(json_data, root_tag='root'):
    root = ET.Element(root_tag)

    def construir_xml(elemento, data):
        if isinstance(data, dict):
            for clave, valor in data.items():
                sub_elemento = ET.SubElement(elemento, clave)
                construir_xml(sub_elemento, valor)
        elif isinstance(data, list):
            for item in data:
                sub_elemento = ET.SubElement(elemento, 'libro')
                construir_xml(sub_elemento, item)
        else:
            elemento.text = str(data)

    construir_xml(root, json_data)

    tree = ET.ElementTree(root)

    xml_str = ET.tostring(root, encoding='unicode')

    return xml_str
    
#ENDPOINT DE VER CATEGORIA ----------------------------------------------------------------------------------------------------------------------------------
@app.route('/libros/<string:categoria>', methods=['GET'])
def buscar_categoria(categoria):

    libros_encontrados = []

    with open('./temp/Salida.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    for libro in data['libros']:
        if libro['categoria'].lower() == categoria.lower():
            libros_encontrados.append(libro)

    if libros_encontrados:
        return jsonify(libros_encontrados)
    else:
        return jsonify({
            'message' : 'ERROR Categoria no encontrada',
            'status' : 404
        }), 404

#MANEJO GENERICO DE ERRORES------------------------------------------------------------------------------------------------------
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({
        ' [ ERROR ] ' : 'Ruta no encontrada! ',
        'status' : 404
    }), 404

@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({
        ' [ ERROR ] ' : 'Metodo NO permitido! ',
        'status' : 405
    }), 405

if __name__ == "__main__":
    app.run(host="localhost", port="4000", debug=True)