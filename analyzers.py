# analyzers.py

def obtener_lineas_utiles(ruta, max_lineas=50):
    lineas_utiles = []
    with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
        for linea in f:
            linea_strip = linea.strip()
            if linea_strip and not linea_strip.startswith(("#", "//", "/*")):
                lineas_utiles.append(linea_strip)
            if len(lineas_utiles) >= max_lineas:
                break
    return "\n".join(lineas_utiles)

def analizar_python(contenido):
    lineas = contenido.splitlines()
    funciones = []
    for linea in lineas:
        if linea.strip().startswith("def "):
            nombre = linea.split("(")[0].replace("def", "").strip()
            funciones.append(nombre)
    descripcion = f"Archivo Python con {len(funciones)} funciones detectadas."
    return {"descripcion": descripcion, "funciones": funciones}

def analizar_js(contenido):
    lineas = contenido.splitlines()
    funciones = []
    for linea in lineas:
        if "function " in linea or "=>" in linea:
            funciones.append(linea.strip())
    descripcion = f"Archivo JavaScript con {len(funciones)} funciones detectadas."
    return {"descripcion": descripcion, "funciones": funciones}

# Para otros lenguajes, implementa similar:
def analizar_html(contenido):
    return {"descripcion": "Archivo HTML detectado.", "funciones": []}

def analizar_css(contenido):
    return {"descripcion": "Archivo CSS detectado.", "funciones": []}

def analizar_json(contenido):
    return {"descripcion": "Archivo JSON detectado.", "funciones": []}

def analizar_txt(contenido):
    return {"descripcion": "Archivo TXT detectado.", "funciones": []}

def analizar_php(contenido):
    return {"descripcion": "Archivo PHP detectado.", "funciones": []}

def analizar_java(contenido):
    return {"descripcion": "Archivo Java detectado.", "funciones": []}

def analizar_cs(contenido):
    return {"descripcion": "Archivo C# detectado.", "funciones": []}

def analizar_yaml(contenido):
    return {"descripcion": "Archivo YAML detectado.", "funciones": []}

def analizar_dockerfile(contenido):
    return {"descripcion": "Archivo Dockerfile detectado.", "funciones": []}
