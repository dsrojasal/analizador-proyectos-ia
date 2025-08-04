import os

# Extensiones relevantes para lógica importante
EXTENSIONES_RELEVANTES = ['.py', '.js', '.ts', '.html', '.css', '.java', '.json']

# Carpetas o archivos poco importantes a evitar
NOMBRES_NO_RELEVANTES = [
    'test', 'tests', 'example', 'sample', '__init__', 'setup', 'config', 'env', '.venv', 'venv', 'node_modules', '.git'
]

def es_relevante(nombre):
    nombre = nombre.lower()
    return not any(p in nombre for p in NOMBRES_NO_RELEVANTES)

def es_archivo_relevante(nombre_archivo):
    return any(nombre_archivo.endswith(ext) for ext in EXTENSIONES_RELEVANTES)

def obtener_archivos_importantes(directorio, limite=15):
    archivos_clave = []
    for root, dirs, files in os.walk(directorio):
        dirs[:] = [d for d in dirs if es_relevante(d)]
        for archivo in files:
            if not es_relevante(archivo):
                continue
            ruta = os.path.join(root, archivo)
            if es_archivo_relevante(archivo):
                archivos_clave.append(ruta)
    return archivos_clave[:limite]

def resumir_contenido(archivos):
    resumen = ""
    for ruta in archivos:
        try:
            with open(ruta, 'r', encoding='utf-8', errors='ignore') as f:
                contenido = f.read()
                lineas = contenido.strip().splitlines()
                primeras_lineas = "\n".join(lineas[:10])
                resumen += f"\nArchivo: {os.path.basename(ruta)}\n{primeras_lineas}\n\n"
        except Exception:
            continue
    return resumen.strip()

def generar_arbol_archivos(rutas_archivos, base_dir):
    from collections import defaultdict

    def insertar_en_arbol(arbol, partes):
        if not partes:
            return
        cabeza = partes[0]
        if cabeza not in arbol:
            arbol[cabeza] = {}
        insertar_en_arbol(arbol[cabeza], partes[1:])

    def imprimir_arbol(arbol, nivel=0):
        salida = ""
        for nombre in sorted(arbol):
            prefijo = "    " * nivel + ("📁 " if arbol[nombre] else "📄 ")
            salida += f"{prefijo}{nombre}\n"
            if arbol[nombre]:
                salida += imprimir_arbol(arbol[nombre], nivel + 1)
        return salida

    estructura = {}
    for ruta in rutas_archivos:
        rel_path = os.path.relpath(ruta, base_dir)
        partes = rel_path.split(os.sep)
        insertar_en_arbol(estructura, partes)

    return imprimir_arbol(estructura).strip()

def analizar_proyecto(ruta):
    archivos = obtener_archivos_importantes(ruta)
    resumen = resumir_contenido(archivos)
    arbol = generar_arbol_archivos(archivos, ruta)
    return resumen, arbol
