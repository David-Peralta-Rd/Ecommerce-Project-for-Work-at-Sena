# Proyecto Ecommerce.
Desarrollado con:
1. Python 3.13.3
2. Django
3. Html y Css

# Pasos para instalar.
1. Clonar repositorio y dirigirte al proyecto.
```bash
git clone https://github.com/David-Peralta-Rd/Proyecto-Ecommerce-Para-Trabajo-Sena.git
cd Proyecto-Ecommerce-Para-Trabajo-Sena
```
2. Crear y activar entorno virtual.
```bash   
# Crear entorno (Windows/Linux/Mac)
python -m venv venv

# Activar (Windows)
.\venv\Scripts\activate

# Activar (Linux/Mac)
source venv/bin/activate
```
3. Instalar dependencias y Activar cambios del proyecto.
```bash
# Instalar dependencias.
pip install -r requeriments.txt

# Activar cambios en base de datos.
python manage.py makemigrations

# Migrar modelos a la base de datos.
python manage.py migrate
```
4. Por ultimo activaremos nuestro proyecto y crearemos un usuario admin-
```bash
# Activar el proyecto en el puerto 8000 o cualquiera
python manage.py runserver

# Si lo quieres activar en otro puerto pon:
python manage.py runserver 3000 # Puede ser cualquier puerto, en mi caso puse 3000.

# Crear usuario Admin, rellenas los datos y ya tienes un super usuario.
python manage.py createsuperuser
```
# Acceder a la web montada localmente:
http://localhost:8000/

# Acceder como admin
http://localhost:8000/admin/

# Fin
Ese seria mi proyecto para un proyecto del sena, aclaro que este es un proyecto que no aseguro su uso de manera seria,
es algo sencillo y directo al punto.

LICENCE: Mit

@Creado por David Peralta✌️.




