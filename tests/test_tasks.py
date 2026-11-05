import unittest
from tasks import agregar_tarea, completar_tarea, eliminar_tarea, pendientes


class TestTasks(unittest.TestCase):

    def test_agregar_tarea(self):
        tareas = []
        tarea = agregar_tarea(tareas, "Leer documentación", "Estudio")
        self.assertEqual(tarea["titulo"], "Leer documentación")
        self.assertEqual(tarea["categoria"], "Estudio")
        self.assertFalse(tarea["completada"])

    def test_agregar_tarea_categoria_vacia(self):
        tareas = []
        with self.assertRaises(ValueError):
            agregar_tarea(tareas, "Leer documentación", "   ")

    def test_completar_tarea(self):
        tareas = []
        agregar_tarea(tareas, "Practicar", "Estudio")
        completar_tarea(tareas, 1)
        self.assertEqual(pendientes(tareas), [])

    def test_pendientes_filtra_por_categoria(self):
        tareas = []
        agregar_tarea(tareas, "Repasar Python", "Estudio")
        agregar_tarea(tareas, "Enviar correo", "Trabajo")
        agregar_tarea(tareas, "Leer artículo", "estudio")
        completar_tarea(tareas, 3)

        tareas_estudio = pendientes(tareas, "eSTuDio")

        self.assertEqual(len(tareas_estudio), 1)
        self.assertEqual(tareas_estudio[0]["titulo"], "Repasar Python")

    def test_pendientes_categoria_inexistente_devuelve_vacio(self):
        tareas = []
        agregar_tarea(tareas, "Repasar Python", "Estudio")
        agregar_tarea(tareas, "Enviar correo", "Trabajo")

        self.assertEqual(pendientes(tareas, "Personal"), [])

    def test_eliminar_tarea_por_id(self):
        tareas = []
        agregar_tarea(tareas, "Repasar Python", "Estudio")
        agregar_tarea(tareas, "Enviar correo", "Trabajo")

        tarea_eliminada = eliminar_tarea(tareas, 1)

        self.assertEqual(tarea_eliminada["titulo"], "Repasar Python")
        self.assertEqual(len(tareas), 1)
        self.assertEqual(tareas[0]["id"], 2)

    def test_eliminar_tarea_id_inexistente(self):
        tareas = []
        agregar_tarea(tareas, "Repasar Python", "Estudio")

        with self.assertRaises(ValueError):
            eliminar_tarea(tareas, 99)


if __name__ == "__main__":
    unittest.main()
