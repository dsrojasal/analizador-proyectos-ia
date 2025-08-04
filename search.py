def buscar_archivos(archivos, query):
    """
    Filtra archivos cuyo nombre o tipo coincidan con el query.
    """
    query = query.lower()
    resultados = []

    for archivo in archivos:
        if query in archivo["nombre"].lower() or query in archivo["tipo"].lower():
            resultados.append(archivo)

    return resultados
