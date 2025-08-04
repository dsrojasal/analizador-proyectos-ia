import os

KEYWORDS = [
    "main", "app", "server", "index", "README", "readme",
    "config", "routes", "models", "controller", "assistant",
    "explorer", "diagram", "utils", "package", "docker", "vite",
    "webpack", "babel", "tsconfig", "vite.config", "eslint",
    "database", "db", "api"
]

PRIORITY_EXTENSIONS = [".py", ".js", ".ts", ".jsx", ".tsx", ".json", ".md", ".yml", ".yaml", ".env"]

def es_archivo_clave(nombre_archivo):
    nombre_lower = nombre_archivo.lower()
    extension = os.path.splitext(nombre_archivo)[1]

    puntaje = PRIORITY_EXTENSIONS.index(extension) + 1 if extension in PRIORITY_EXTENSIONS else 0

    for keyword in KEYWORDS:
        if keyword in nombre_lower:
            puntaje += 5

    return puntaje

def filtrar_archivos_clave(ruta_proyecto, top_n=20):
    archivos_importantes = []

    for root, dirs, files in os.walk(ruta_proyecto):
        for file in files:
            full_path = os.path.join(root, file)
            puntaje = es_archivo_clave(file)
            if puntaje > 0:
                archivos_importantes.append((file, puntaje, full_path))

    archivos_importantes.sort(key=lambda x: x[1], reverse=True)

    return archivos_importantes[:top_n]
