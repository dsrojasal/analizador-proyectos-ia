def generar_documentacion(archivos):
    """
    Genera documentación técnica en formato Markdown para todos los archivos detectados.
    Incluye: nombre, extensión, tipo, ruta, funciones detectadas y explicaciones.
    """
    doc = "# 📄 Documentación Técnica del Proyecto\n\n"
    
    for archivo in archivos:
        nombre = archivo["nombre"]
        extension = archivo["extension"]
        tipo = archivo["tipo"]
        ruta = archivo["ruta"]
        funciones = archivo.get("funciones", [])
        explicacion = archivo.get("explicacion", "")
        
        doc += f"## 🔹 {nombre} ({extension}, {tipo})\n"
        doc += f"📁 Ruta: `{ruta}`\n\n"

        if funciones:
            doc += "### ✅ Funciones detectadas:\n"
            for funcion in funciones:
                doc += f"- `{funcion}`\n"
        else:
            doc += "⚠️ No se detectaron funciones en este archivo.\n"

        if explicacion:
            doc += f"\n### 📝 Explicación:\n{explicacion}\n"

        doc += "\n---\n"
    
    return doc
