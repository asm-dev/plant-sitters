# Plant Sitters

Plant Sitters, es una plataforma para poner en contacto a personas que necesitan que algún vecino se pase a cuidar las plantas, dar de comer al gato, o a ahuyentar fantasmas, cuando se van de vacaciones. Plant sitters, cat sitters, house keepers... el lema es "Te cuidamos la casa cuando no estás".

Este repositorio alberga el ecosistema back necesario para hacer posible esta actividad.

Tecnologías empleadas:

- Django: framework principal para crear el servidor y la lógica de negocio
- REST Framework (DRF): permite crear los API endpoints y facilitar el manejo de peticiones
- MySQL: aunque por defecto se emplea SQLite, utilizamos una BBDD MySQL

##Requisitos previos

1. Python 3.9
2. MySQL instalado y en funcionamiento.

##Instalación y config

1. Clona el repositorio en tu máquina local
2. Crea un entorno virtual (si no lo tienes ya). Recomiend Anaconda, pero también puedes usar venv
3. Instala las dependencias `pip install -r requirements.txt`
4. Crea la BBDD MySQL:

```
mysql -u root -p
CREATE DATABASE plantsitters_db;
EXIT;
```

5. Crea un archivo .env en la raíz del proyecto

```
DB_USER=root
DB_PASSWORD=tu_contraseña_de_root
```

6. Aplica las migraciones para crear las tablas de la BBDD en MySQL: `python manage.py migrate`
7. Inicia el servidor de desarrollo `python manage.py runserver`
8. Diviértete probando la aplicación en `http://127.0.0.1:8000/`

---

## ES NECESARIO ENVIAR TOKEN EN LAS REQUESTS! [USUARIO MONSTERA ES SUPERUSUARIO]

##Detalles técnicos

- Para agilizar las operaciones CRUD se han utilizado ViewSets para gestionar las tareas, pero dos API View para gestionar usuarios
- Se emplean herramientas para la creación y autenticación de usuarios
- Se trata de un proyecto portable. Usando un archivo `.env` podemos configurar las credenciales de la BBDD de forma segura y flexible sin necesidad de modificar el código fuente. Además el ficherpo `requirements.txt` facilita la creación de entornos virtuales para la ejecución del proyecto en cualquier sistema.

##Posibles futuras iteraciones

- Generar una vista que permita a los usuarios buscar y asignar cuidadores
- Implementar un sistema de pago
- Desarrollar una interfaz visual para la aplicación (frontend)
- Implementar un sistema de notificaciones para avisar a usuarios cuando se asignen o completen tareas
