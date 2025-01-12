# Plant Sitters

<div align="center"><img src="https://github.com/user-attachments/assets/f9d8afe0-76c4-4a78-81b0-77726e68663c"/></div>

&nbsp;

Plant Sitters, es una plataforma para poner en contacto a personas que necesitan que algún vecino se pase a cuidar las plantas, dar de comer al gato, o a ahuyentar fantasmas cuando se van de vacaciones. _Plant sitters, cat sitters, house keepers_... el lema es "Te cuidamos la casa cuando no estás".

Este repositorio alberga el ecosistema back necesario para hacer posible esta actividad. Empleamos **Django** como framework principal para crear el servidor, junto con **REST** (DRF) para los API endpoints y **MySQL** como base de datos. 

&nbsp;

## Instalación y config

**Requisitos previos**: 

- Python 3.9
- MySQL instalado y en funcionamiento

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
   
&nbsp;

## Detalles técnicos

- Para agilizar las operaciones CRUD se han utilizado ViewSets para gestionar las tareas, pero dos API View para gestionar usuarios
- Se emplean herramientas para la creación y autenticación de usuarios
- Se trata de un proyecto **portable**. Usando un archivo `.env` podemos configurar las credenciales de la BBDD de forma segura y flexible sin necesidad de modificar el código fuente. Además el ficherpo `requirements.txt` facilita la creación de entornos virtuales para la ejecución del proyecto en cualquier sistema.
- Además, la aplicación es **escalable** gracias a la capacidad de MySQL, que posibilita manejar tráfico y volumen de datos de manera más eficiente que SQLite
   
&nbsp;

## Posibles futuras iteraciones

- Generar una vista que permita a los usuarios buscar y asignar cuidadores
- Implementar un sistema de pago
- Desarrollar una interfaz visual para la aplicación (frontend)
- Implementar un sistema de notificaciones para avisar a usuarios cuando se asignen o completen tareas
