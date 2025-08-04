# analyzer.py
from analyzers import (
    analizar_python, analizar_js, analizar_html,
    analizar_css, analizar_json, analizar_txt,
    analizar_php, analizar_java, analizar_cs,
    analizar_yaml, analizar_dockerfile,
    obtener_lineas_utiles
)

def analizar_archivo(archivo):
    contenido = obtener_lineas_utiles(archivo["ruta"], max_lineas=50)
    ext = archivo["extension"]

    if ext == ".py":
        return analizar_python(contenido)
    elif ext == ".js":
        return analizar_js(contenido)
    elif ext == ".html":
        return analizar_html(contenido)
    elif ext == ".css":
        return analizar_css(contenido)
    elif ext == ".json":
        return analizar_json(contenido)
    elif ext == ".txt":
        return analizar_txt(contenido)
    elif ext == ".php":
        return analizar_php(contenido)
    elif ext == ".java":
        return analizar_java(contenido)
    elif ext == ".cs":
        return analizar_cs(contenido)
    elif ext == ".yaml":
        return analizar_yaml(contenido)
    elif ext == "dockerfile":
        return analizar_dockerfile(contenido)
    else:
        return {
            "descripcion": f"No existe analizador implementado para archivos {ext}."
        }
