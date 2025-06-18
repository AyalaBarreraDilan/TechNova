from django.test import TestCase
from .models import Producto

class ProductoModelTest(TestCase):
    def test_crear_producto(self):
        producto = Producto.objects.create(
            nombre="Teclado",
            descripcion="Teclado mecánico RGB",
            precio=199.99,
            stock=10
        )
        self.assertEqual(producto.nombre, "Teclado")
