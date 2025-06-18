import pytest
from productos.models import Producto

@pytest.mark.django_db
def test_creacion_producto():
    producto = Producto.objects.create(
        nombre="Laptop",
        descripcion="Portátil Lenovo",
        precio=1500000,
        stock=10
    )
    assert producto.nombre == "Laptop"
    assert producto.precio == 1500000
    assert producto.stock == 10
    
    
@pytest.mark.django_db
def test_actualizar_producto():
    producto = Producto.objects.create(nombre="Teclado", descripcion="Teclado mecánico", precio=100000, stock=5)
    producto.precio = 120000
    producto.save()

    producto_actualizado = Producto.objects.get(nombre="Teclado")
    assert producto_actualizado.precio == 120000
    
    
@pytest.mark.django_db
def test_actualizar_producto():
    producto = Producto.objects.create(nombre="Teclado", descripcion="Teclado mecánico", precio=100000, stock=5)
    producto.precio = 120000
    producto.save()

    producto_actualizado = Producto.objects.get(nombre="Teclado")
    assert producto_actualizado.precio == 120000
    
    
    
    
@pytest.mark.django_db
def test_eliminar_producto():
    producto = Producto.objects.create(nombre="Monitor", descripcion="Monitor 24''", precio=600000, stock=3)
    producto.delete()

    productos = Producto.objects.filter(nombre="Monitor")
    assert productos.count() == 0



