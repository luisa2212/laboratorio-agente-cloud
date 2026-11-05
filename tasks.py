def agregar_tarea(tareas, titulo, categoria):
    titulo = titulo.strip()
    if not titulo:
        raise ValueError("El titulo es obligatorio")
    categoria = categoria.strip()
    if not categoria:
        raise ValueError("La categoria es obligatoria")
    tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo,
        "categoria": categoria,
        "completada": False
    }
    tareas.append(tarea)
    return tarea


def completar_tarea(tareas, tarea_id):
    for tarea in tareas:
        if tarea["id"] == tarea_id:
            tarea["completada"] = True
            return tarea
    raise ValueError("Tarea no encontrada")


def eliminar_tarea(tareas, tarea_id):
    for index, tarea in enumerate(tareas):
        if tarea["id"] == tarea_id:
            return tareas.pop(index)
    raise ValueError("Tarea no encontrada")


def pendientes(tareas, categoria=None):
    tareas_pendientes = [t for t in tareas if not t["completada"]]
    if categoria is None:
        return tareas_pendientes

    categoria_filtrada = categoria.strip().lower()
    if not categoria_filtrada:
        return tareas_pendientes

    return [t for t in tareas_pendientes if t["categoria"].lower() == categoria_filtrada]
