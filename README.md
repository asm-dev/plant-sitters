# Plant Sitters

<div align="center"><img src="https://github.com/user-attachments/assets/f9d8afe0-76c4-4a78-81b0-77726e68663c"/></div>

&nbsp;

Plant Sitters, es una plataforma para poner en contacto a personas que necesitan que algún vecino se pase a cuidar las plantas, dar de comer al gato, o a ahuyentar fantasmas cuando se van de vacaciones. _Plant sitters, cat sitters, house keepers_... el lema es "Te cuidamos la casa cuando no estás".

Este repositorio alberga el ecosistema back necesario para hacer posible esta actividad. Empleamos **Django** como framework principal para crear el servidor, junto con **REST** (DRF) para los API endpoints y **MySQL** como base de datos.

&nbsp;

## Requisitos previos

- Python 3.9
- MySQL instalado y en funcionamiento
- (_Recomendado_) DBeaver para visualizar la BBDD

&nbsp;

## Instalación y config

1. **Clona** el repositorio en tu máquina local
2. Crea un **entorno virtual** (si no lo tienes ya). Recomiendo Anaconda, pero también puedes usar venv
3. Instala las **dependencias** `pip install -r requirements.txt`
4. Crea la **base de datos** (BBDD) MySQL:

```
mysql -u root -p
CREATE DATABASE plantsitters_db;
EXIT;
```

(_Opcional_) Deberías poder acceder a la BBDD con tu usuario root. No obstante, recomendamos crear un usuario específico para el manejo de la misma:

```
mysql -u root -p
CREATE USER 'ejemplo_de_usuario'@'localhost' IDENTIFIED BY 'contraseña_que_decidas';
GRANT ALL PRIVILEGES ON plantsitters_db.* TO 'ejemplo_de_usuario'@'localhost';
FLUSH PRIVILEGES
```

5. Actualiza el **environment** desde el fichero `.env` en la raíz del proyecto con los datos de un usuario que tenga permisos para la BBDD. Es decir, el usuario root, o el que hayas creado en el paso anterior.

```
DB_USER=root
DB_PASSWORD=contraseña_del_usuario_root
```

6. Aplica las **migraciones** para crear las tablas de la BBDD en MySQL: `python manage.py migrate`
7. Crea un **superusuario** Django. Puedes hacerlo manualmente desde la shell o `python manage.py createsuperuser`, pero hemos creado un comando personalizado que puede ayudarte si no quieres complicaciones: `python manage.py create_super_user`
8. **Inicia el servidor** de desarrollo `python manage.py runserver`
9. Diviértete probando el servidor en `http://127.0.0.1:8000/`

&nbsp;

> Nota: Para poder gestionar tareas es necesario estar autenticado. Para ello, habrás de añadir un **token** en tus solicitudes al servidor. Puedes conseguirlo facilmente ingresando tus datos de usuario en `api-token-auth/`. También ten en cuenta que para poder destruirlas, será necesario ser admin o el usuario que haya creado las tareas.

&nbsp;

## Detalles técnicos clave

- Para agilizar las operaciones CRUD se han utilizado tanto **ViewSets** como **vistas genéricas** para gestionar tareas y usuarios.
- Existe una **API View propia** que vincula los modelos de usuario y tarea. Permite devolver todas las tareas asociadas a un usuario específico.
- Se trata de un proyecto **portable**. Usando un archivo `.env` podemos configurar las credenciales de la BBDD de forma segura y flexible sin necesidad de modificar el código fuente. Además el fichero `requirements.txt` facilita la creación de entornos virtuales para la ejecución del proyecto en cualquier sistema.
- La aplicación es **escalable** gracias a la capacidad de **MySQL**, que posibilita manejar tráfico y volumen de datos de manera más eficiente que SQLite.
- Se emplean herramientas para la creación y autenticación de usuarios. Además, existen dos **grupos de usuarios** Requester y Plantsitter, permitiendo así definir capacidades y permisos dentro del sistema en función del rol del usuario.

&nbsp;

## Ejemplos de uso

_Creación de "tareas" desde `/admin` a la BBDD_

![image](https://github.com/user-attachments/assets/e299da3a-d369-4105-b7b8-90cfc2ae6c39)

_Prueba de uso de endpoint para updatar tareas desde `/api`_

![image](https://github.com/user-attachments/assets/19d2bcb6-42a3-49f1-b7c7-5484bcbb599e)
