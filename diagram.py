def generar_diagrama(archivos):
    """
    Genera un diagrama general de los archivos detectados en formato Mermaid.
    """
    diagrama = "graph TD\n"
    for archivo in archivos:
        nombre = archivo["nombre"]
        tipo = archivo["tipo"]
        diagrama += f'{nombre}["{nombre}\\n({tipo})"]\n'
    return diagrama


def generar_diagrama_uml(archivos):
    """
    Genera un diagrama UML simplificado en formato Mermaid.
    Muestra clases, funciones detectadas y su relación con el archivo.
    """
    uml = "classDiagram\n"
    for archivo in archivos:
        nombre = archivo["nombre"].replace(".py", "")
        funciones = archivo.get("funciones", [])

        # Definir clase por cada archivo
        uml += f"class {nombre} {{\n"
        for funcion in funciones:
            uml += f"    + {funcion}()\n"
        uml += "}\n"

    return uml
