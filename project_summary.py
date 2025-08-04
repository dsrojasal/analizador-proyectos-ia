# project_summary.py

from analyzer import analizar_archivo

def resumen_proyecto(archivos):
    resumen = []
    for archivo in archivos:
        try:
            analisis = analizar_archivo(archivo)
            resumen.append({
                "nombre": archivo["nombre"],
                "extension": archivo["extension"],
                "ruta": archivo["ruta"],
                "descripcion": analisis.get("descripcion", "Sin descripción generada."),
                "funciones": analisis.get("funciones", [])
            })
        except Exception as e:
            resumen.append({
                "nombre": archivo["nombre"],
                "error": str(e)
            })
    return resumen
