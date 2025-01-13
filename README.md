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
- (*Recomendado*) DBeaver para visualizar la base de datos (BBDD) 

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
9. Diviértete probando la aplicación en `http://127.0.0.1:8000/`

&nbsp;

## Detalles técnicos

- Para agilizar las operaciones CRUD se han utilizado tanto **ViewSets** como **API Views** para gestionar las tareas y los usuarios, escogiendo una u otra en función de las necesidades.
- Existe una **API View propia** para vincular los modelos de usuario y tarea. Permite devolver todas las tareas asociadas a un usuario específico.
- Se emplean herramientas para la creación y autenticación de usuarios.
- Se trata de un proyecto **portable**. Usando un archivo `.env` podemos configurar las credenciales de la BBDD de forma segura y flexible sin necesidad de modificar el código fuente. Además el fichero `requirements.txt` facilita la creación de entornos virtuales para la ejecución del proyecto en cualquier sistema.
- Además, la aplicación es **escalable** gracias a la capacidad de **MySQL**, que posibilita manejar tráfico y volumen de datos de manera más eficiente que SQLite.
- Se emplean los grupos Requester y Plantsitter, permitiendo así definir capacidades y permisos dentro del sistema en función del rol del usuario.

&nbsp;

## Ejemplos de uso

**Agregamos una tarea desde /admin a la BBDD**

![image](https://github.com/user-attachments/assets/e299da3a-d369-4105-b7b8-90cfc2ae6c39)



- Auth token?
