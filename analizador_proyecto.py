import os
from assistant import responder_pregunta

EXTENSIONES_RELEVANTES = [
    '.py', '.js', '.ts', '.java', '.c', '.cpp', '.cs',
    '.html', '.css', '.json', '.xml', '.yaml', '.yml',
    '.env', '.md'
]

PRIORIDAD = {
    'documentacion': ['readme'],
    'config': ['package', 'requirements', 'pom', 'docker', 'compose'],
    'entrada': ['main', 'index', 'server', 'app'],
    'codigo': ['controller', 'model', 'route'],
    'script': ['migrate', 'seed'],
    'test': ['test']
}

def clasificar_archivo(nombre_archivo):
    nombre = nombre_archivo.lower()
    for categoria, patrones in PRIORIDAD.items():
        for patron in patrones:
            if patron in nombre:
                return categoria
    return 'otro'

def leer_extractos(ruta_archivo):
    try:
        with open(ruta_archivo, 'r', encoding='utf-8', errors='ignore') as f:
            lineas = f.readlines()
            inicio = lineas[:20]
            final = lineas[-10:] if len(lineas) > 10 else []
            extracto = inicio + ['...\n'] + final
            return ''.join(extracto)
    except Exception as e:
        return f"[Error leyendo archivo: {e}]"

def analizar_proyecto(ruta_proyecto):
    archivos_detectados = []

    for carpeta_raiz, _, archivos in os.walk(ruta_proyecto):
        for archivo in archivos:
            ruta_completa = os.path.join(carpeta_raiz, archivo)
            nombre, extension = os.path.splitext(archivo)

            if extension in EXTENSIONES_RELEVANTES:
                categoria = clasificar_archivo(nombre)
                archivos_detectados.append({
                    'ruta': ruta_completa,
                    'nombre': archivo,
                    'extension': extension,
                    'categoria': categoria
                })

    prioridad_orden = ['documentacion', 'config', 'entrada', 'codigo', 'script', 'test', 'otro']
    archivos_ordenados = sorted(
        archivos_detectados,
        key=lambda x: prioridad_orden.index(x['categoria']) if x['categoria'] in prioridad_orden else len(prioridad_orden)
    )

    return archivos_ordenados

def generar_resumen_ai(archivos):
    listado = "\n".join([f"{a['categoria'].upper()}: {a['nombre']} ({a['extension']})" for a in archivos])

    prompt = f"""
Eres un arquitecto de software senior.

Te paso este listado de archivos detectados en un proyecto:

{listado}

🔷 Tu tarea es:

1. Seleccionar los archivos MÁS IMPORTANTES para:
   - Saber qué hace el proyecto.
   - Entender su arquitectura y flujo principal.

2. Explicar brevemente por qué cada archivo seleccionado es clave.

3. Generar un resumen profesional: ¿Para qué sirve este proyecto y cómo está estructurado?

Responde en Markdown profesional, claro y estructurado.
"""

    return responder_pregunta(prompt)

if __name__ == "__main__":
    ruta = input("📁 Ingresa la ruta del proyecto: ")
    archivos = analizar_proyecto(ruta)

    print("\n✅ Archivos detectados, generando resumen con AI...\n")

    resumen_ai = generar_resumen_ai(archivos)

    with open('resumen_ai_proyecto.md', 'w', encoding='utf-8') as f:
        f.write(resumen_ai)

    print("\n✅ Resumen AI generado y guardado en 'resumen_ai_proyecto.md'")
