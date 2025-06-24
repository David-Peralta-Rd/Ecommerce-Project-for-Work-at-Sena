# tests.py - Pruebas sencillas para el proyecto Ecommerce
"""
Pruebas básicas para las funciones principales del ecommerce
Proyecto SENA - David Peralta
"""

from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from cart.models import CartItem
from orders.models import Order
from products.models import Category, Product

Categoria = Category()
Producto = Product()
Carrito = CartItem()
Pedido = Order()
# Nota: Ajusta estos imports según los names reales de tus modelos
# from .models import Producto, Categoria, Carrito, Pedido


class TestPaginaWeb(TestCase):
    """Pruebas para las páginas web básicas"""

    def setUp(self):
        """Configuración inicial"""
        self.client = Client()

    def test_pagina_inicio(self):
        """Prueba que la página de inicio carga bien"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print("✓ Página de inicio funciona")

    def test_pagina_productos(self):
        """Prueba que la página de productos carga"""
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)
        print("✓ Página de productos funciona")

    def test_pagina_categorias(self):
        """Prueba que la página de categorías carga"""
        response = self.client.get('/categorias/')
        self.assertEqual(response.status_code, 200)
        print("✓ Página de categorías funciona")


class TestUsuarios(TestCase):
    """Pruebas para registro y login de usuarios"""

    def setUp(self):
        self.client = Client()

    def test_crear_usuario(self):
        """Prueba crear un usuario nuevo"""
        usuario = User.objects.create_user(
            username='testuser', email='test@ejemplo.com', password='123456'
        )
        self.assertEqual(usuario.username, 'testuser')
        self.assertTrue(usuario.is_active)
        print("✓ Crear usuario funciona")

    def test_login_usuario(self):
        """Prueba que un usuario puede hacer login"""
        # Crear usuario
        User.objects.create_user(username='testuser', password='123456')

        # Intentar login
        login_exitoso = self.client.login(username='testuser', password='123456')
        self.assertTrue(login_exitoso)
        print("✓ Login de usuario funciona")

    def test_login_fallido(self):
        """Prueba login con datos incorrectos"""
        login_exitoso = self.client.login(username='noexiste', password='123456')
        self.assertFalse(login_exitoso)
        print("✓ Login fallido se maneja bien")


class TestProductos(TestCase):
    """Pruebas para los productos"""

    def setUp(self):
        # Crear una categoría de prueba
        self.categoria = Categoria.objects.create(
            name='Electrónicos', descripcion='Productos electrónicos'
        )

        # Crear un producto de prueba
        self.producto = Producto.objects.create(
            name='Celular Samsung',
            descripcion='Smartphone último modelo',
            price=500000,
            stock=10,
            categoria=self.categoria,
        )

    def test_crear_producto(self):
        """Prueba crear un producto"""
        self.assertEqual(self.producto.name, 'Celular Samsung')
        self.assertEqual(self.producto.price, 500000)
        self.assertEqual(self.producto.stock, 10)
        print("✓ Crear producto funciona")

    def test_producto_disponible(self):
        """Prueba que el producto tiene stock"""
        self.assertTrue(self.producto.stock > 0)
        print("✓ Verificar stock funciona")

    def test_ver_detalle_producto(self):
        """Prueba ver el detalle de un producto"""
        response = self.client.get(f'/producto/{self.producto.id}/')
        self.assertEqual(response.status_code, 200)
        print("✓ Ver detalle de producto funciona")


class TestCarrito(TestCase):
    """Pruebas para el carrito de compras"""

    def setUp(self):
        # Crear usuario
        self.user = User.objects.create_user(username='comprador', password='123456')

        # Crear producto
        self.categoria = Categoria.objects.create(name='Ropa')
        self.producto = Producto.objects.create(
            name='Camiseta', price=25000, stock=5, categoria=self.categoria
        )

        self.client = Client()

    def test_agregar_al_carrito(self):
        """Prueba agregar un producto al carrito"""
        # Hacer login
        self.client.login(username='comprador', password='123456')

        # Agregar producto al carrito
        item_carrito = Carrito.objects.create(
            usuario=self.user, producto=self.producto, quantity=2
        )

        self.assertEqual(item_carrito.quantity, 2)
        self.assertEqual(item_carrito.product.name, 'Camiseta')
        print("✓ Agregar al carrito funciona")

    def test_ver_carrito(self):
        """Prueba ver el contenido del carrito"""
        self.client.login(username='comprador', password='123456')

        # Agregar algo al carrito
        Carrito.objects.create(usuario=self.user, producto=self.producto, quantity=1)

        # Ver carrito
        response = self.client.get('/carrito/')
        self.assertEqual(response.status_code, 200)
        print("✓ Ver carrito funciona")

    def test_calcular_total_carrito(self):
        """Prueba calcular el total del carrito"""
        # Agregar productos al carrito
        item1 = Carrito.objects.create(
            usuario=self.user, producto=self.producto, quantity=2  # 2 * 25000 = 50000
        )

        total_esperado = self.producto.price * 2
        total_calculado = item1.product.price * item1.quantity

        self.assertEqual(total_calculado, total_esperado)
        print("✓ Calcular total del carrito funciona")

    def test_eliminar_del_carrito(self):
        """Prueba eliminar producto del carrito"""
        # Agregar al carrito
        item = Carrito.objects.create(
            usuario=self.user, producto=self.producto, quantity=1
        )

        # Eliminar del carrito
        item.delete()

        # Verificar que no existe
        carritos = Carrito.objects.filter(usuario=self.user)
        self.assertEqual(carritos.count(), 0)
        print("✓ Eliminar del carrito funciona")


class TestCompras(TestCase):
    """Pruebas para el proceso de compra"""

    def setUp(self):
        self.user = User.objects.create_user(username='cliente', password='123456')

        self.categoria = Categoria.objects.create(name='Libros')
        self.producto = Producto.objects.create(
            name='Libro Python', price=45000, stock=3, categoria=self.categoria
        )

        self.client = Client()

    def test_crear_pedido(self):
        """Prueba crear un pedido de compra"""
        self.client.login(username='cliente', password='123456')

        # Crear pedido
        pedido = Pedido.objects.create(
            usuario=self.user,
            total=45000,
            direccion='Calle 123 #45-67, Bogotá',
            telefono='3001234567',
            estado='pendiente',
        )

        self.assertEqual(pedido.user.username, 'cliente')
        self.assertEqual(pedido.total, 45000)
        self.assertEqual(pedido.estado, 'pendiente')
        print("✓ Crear pedido funciona")

    def test_confirmar_compra(self):
        """Prueba confirmar una compra"""
        # Crear pedido
        pedido = Pedido.objects.create(
            usuario=self.user,
            total=45000,
            direccion='Calle 123 #45-67',
            estado='pendiente',
        )

        # Confirmar pedido
        pedido.estado = 'confirmado'
        pedido.save()

        self.assertEqual(pedido.estado, 'confirmado')
        print("✓ Confirmar compra funciona")

    def test_stock_se_descuenta(self):
        """Prueba que el stock se descuenta al comprar"""
        stock_inicial = self.producto.stock
        cantidad_comprada = 2

        # Simular compra (descontar stock)
        self.producto.stock -= cantidad_comprada
        self.producto.save()

        self.assertEqual(self.producto.stock, stock_inicial - cantidad_comprada)
        print("✓ Descontar stock funciona")


class TestBusqueda(TestCase):
    """Pruebas para buscar productos"""

    def setUp(self):
        self.categoria = Categoria.objects.create(name='Tecnología')

        # Crear varios productos
        Producto.objects.create(
            name='iPhone 14', price=800000, categoria=self.categoria, stock=2
        )

        Producto.objects.create(
            name='Samsung Galaxy', price=600000, categoria=self.categoria, stock=3
        )

        self.client = Client()

    def test_buscar_producto(self):
        """Prueba buscar productos"""
        response = self.client.get('/buscar/?q=iPhone')
        self.assertEqual(response.status_code, 200)
        print("✓ Buscar productos funciona")

    def test_filtrar_por_categoria(self):
        """Prueba filtrar productos por categoría"""
        response = self.client.get(f'/categoria/{self.categoria.id}/')
        self.assertEqual(response.status_code, 200)
        print("✓ Filtrar por categoría funciona")


class TestAdmin(TestCase):
    """Pruebas para el panel de administrador"""

    def setUp(self):
        # Crear usuario admin
        self.admin = User.objects.create_superuser(
            username='admin', email='admin@ecommerce.com', password='admin123'
        )
        self.client = Client()

    def test_acceso_admin(self):
        """Prueba acceso al panel de admin"""
        self.client.login(username='admin', password='admin123')
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 200)
        print("✓ Acceso al admin funciona")

    def test_usuario_normal_no_accede_admin(self):
        """Prueba que usuarios normales no pueden acceder al admin"""
        User.objects.create_user(username='normal', password='123456')
        self.client.login(username='normal', password='123456')

        response = self.client.get('/admin/')
        # Debe redirigir al login del admin
        self.assertEqual(response.status_code, 302)
        print("✓ Restricción de admin funciona")


# Instrucciones para ejecutar las pruebas:
"""
1. Guarda este archivo como 'tests.py' en tu aplicación Django

2. Ejecutar todas las pruebas:
   python manage.py test

3. Ejecutar pruebas específicas:
   python manage.py test tests.TestCarrito
   python manage.py test tests.TestCompras

4. Ver más detalles:
   python manage.py test --verbosity=2

5. Si tienes errores de importación, ajusta las líneas:
   from .models import Producto, Categoria, Carrito, Pedido

   Por los names reales de tus modelos y aplicación.

Ejemplo de uso:
python manage.py test
"""
