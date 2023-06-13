import sqlite3


con = sqlite3.connect("quiz.db")
cur = con.cursor()
cur.execute(
    "CREATE TABLE if not exists preguntas(id_pregunta, texto, tema, nivel, correcta)")

def read_all():
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM preguntas")
        rows = res.fetchall()
        
        #Opción 1: Para cambiar los valores de la lista en tuplas (objetos)
        pregunta_list = []
        for row in rows:
            row = {"id_pregunta": row[0],
                "texto": row[1],
                "tema": row[2],
                "nivel": row[3],
                "correcta": row[4]
                }
            pregunta_list.append(row) #esto es para incluir en pregunta_list cada uno de las tuplas creadas (row)
            print("que es esto ", row)
        return pregunta_list
    except:
        None
    finally:
        con.close()

     #Opción 2: Para cambiar los valores de la lista en tuplas (objetos)
    """
    columnas = ["id_pregunta", "texto", "tema", "nivel", "correcta"]
    datos_dict[dict(zip(columnas, fila)) for fila in rows]
    return datos_dict
    """


def read(id_pregunta):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM preguntas WHERE id_pregunta=?", [id_pregunta])
        row = res.fetchone()

        pregunta = {"id_pregunta": row[0],
                "texto": row[1],
                "tema": row[2],
                "nivel": row[3],
                "correcta": row[4]
                }
        return pregunta
    except:
        None
    finally:
        con.close()

def create(quiz):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = "INSERT INTO preguntas VALUES(?, ?, ?, ?, ?)"
        valores = (quiz['id_pregunta'], quiz['texto'],
                quiz['tema'], quiz['nivel'], quiz['correcta'])
        cur.execute(res, valores)
        con.commit()
        # print("Esto es mi data quiz", quiz)
        # Esto es mi data quiz 
        # {'id_pregunta': '1', 'texto': '¿que es una p?', 'tema': 'html', 'nivel': '1', 'correcta': 'un parrafo'}
    except:
        None
    finally:
        con.close()

def remove_pregunta(id_pregunta):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        cur.execute("DELETE FROM preguntas WHERE id_pregunta=?", [id_pregunta])
        con.commit()
    except:
        None
    finally:
        con.close()

#Modificar
#def update(new_id_pregunta, new_texto, new_tema, new_nivel, new_correcta)
def update(new_id_pregunta, new_texto):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = "UPDATE preguntas SET texto = ? WHERE id_pregunta = ?"
        values = (new_texto, new_id_pregunta)
        cur.execute(res, values)
        con.commit()
    except:
        None
    finally:
        con.close()

#Esta función recoge la data que viene del Front

def update_pregunta_data(id_pregunta, data): #recoge los datos del front: data
    #Esta función hace dos tareas:
    #1. Guardar los valores que vienen del front en variables
    new_texto = data.get("texto")
    # new_tema = data.get("tema")
    # new_nivel = data.get("nivel")
    # new_correcta = data.gel("correcta")
    # print("este es el texto", new_texto)
    # print("esto es data", data) 
    # data {
    #  'texto': 'que es h1',  
    #  'tema': 'html', 
    #  'nivel': '1',
    #  'correcta': 'un titulo'
    #  }
    # update(id_pregunta, new_texto, new_tema, new_nivel, new_correcta)
    update(id_pregunta, new_texto)
    
    
#Editado porque se duplica la función
def read_all_1():
    con = sqlite3.connect("quiz.db")
    try:
       cur = con.cursor()
       res = cur.execute("SELECT * FROM respuestas")
       rows = res.fetchall()
        
        #Opción 1: Para cambiar los valores de la lista en tuplas (objetos)
       respuesta_list = []
       for row in rows:
            row = {"id_respuesta": row[0],
                    "texto_res": row[1],
                    "id_pregunta": row[2]
                     
                
                    }
            respuesta_list.append(row) #esto es para incluir en respuesta_list cada uno de las tuplas creadas (row)
            print("que es esto ", row)
       return respuesta_list
    except:
        None
    finally:
        con.close()

      #Opción 2: Para cambiar los valores de la lista en tuplas (objetos)
    """
    columnas = ["id_respuesta", "texto_res", "id_pregunta"]
    datos_dict[dict(zip(columnas, fila)) for fila in rows]
    return datos_dict
    """


def read(id_respuesta):
    con = sqlite3.connect("quiz.db")
    try:
        cur = con.cursor()
        res = cur.execute("SELECT * FROM respuestas WHERE id_respuesta=?", [id_respuesta])
        row = res.fetchone()

        respuesta = {"id_respuesta": row[0],
                "texto_res": row[1],
                "pregunta_id": row[2]
                 }
        return respuesta
    except:
         None
    finally:
         con.close()

def create(quiz):
     con = sqlite3.connect("quiz.db")
     try:
         cur = con.cursor()
         res = "INSERT INTO respuestas VALUES(?, ?, ?)"
         valores = (quiz['id_respuesta'], quiz['texto_res'],
                  quiz['id_pregunta'])
         cur.execute(res, valores)
         con.commit()
         # print("Esto es mi data quiz", quiz)
         # Esto es mi data quiz 
         # {'id_respuesta': '1', 'texto_res': 'un parrafo', 'id_pregunta': '1'}
     except:
         None
     finally:
         con.close()

#Editado porque se duplica la función
def remove_pregunta_1(id_respuesta):
     con = sqlite3.connect("quiz.db")
     try:
         cur = con.cursor()
         cur.execute("DELETE FROM respuestas WHERE id_respuesta=?", [id_respuesta])
         con.commit()
     except:
         None
     finally:
         con.close()

 #Modificar

#Editado porque se duplica la función
def update_1(new_id_respuesta, new_texto_res,  new_id_pregunta):
     con = sqlite3.connect("quiz.db")
     try:
         cur = con.cursor()
         res = "UPDATE preguntas SET pregunta_a = ?, pregunta_b = ?, pregunta_c = ?, id_pregunta = ? WHERE id_respuesta = ?"
         values = (new_texto_res, new_id_pregunta, new_id_respuesta)
         cur.execute(res, values)
         con.commit()
     except:
         None
     finally:
         con.close()

 #Esta función recoge la data que viene del Front

#Editado porque se duplica la función
def update_respuesta_data_1(id_respuesta, data): #recoge los datos del front: data
     #Esta función hace dos tareas:
     #1. Guardar los valores que vienen del front en variables
     new_texto_res = data.get("texto_res")
     new_id_pregunta = data.gel("id_pregunta")