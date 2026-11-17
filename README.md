# Plant Sitters

<div align="center"><img src="https://github.com/user-attachments/assets/f9d8afe0-76c4-4a78-81b0-77726e68663c"/></div>

&nbsp;

Plant Sitters is a platform that connects people who need a neighbor to drop by to water the plants, feed the cat, or chase away ghosts while they are on vacation. _Plant sitters, cat sitters, house keepers_... our motto is "We look after your home when you're away".

This repository hosts the back-end ecosystem needed to make this activity possible. We use **Django** as the main framework to build the server, together with **REST** (DRF) for the API endpoints and **MySQL** as the database.

&nbsp;

## Prerequisites

- Python 3.9
- MySQL installed and running
- (_Recommended_) DBeaver to view the DB

&nbsp;

## Installation and config

1. **Clone** the repository to your local machine
2. Create a **virtual environment** (if you don't have one already). I recommend Anaconda, but you can also use venv
3. Install the **dependencies** `pip install -r requirements.txt`
4. Create the MySQL **database** (DB):

```
mysql -u root -p
CREATE DATABASE plantsitters_db;
EXIT;
```

(_Optional_) You should be able to access the DB with your root user. However, we recommend creating a specific user to manage it:

```
mysql -u root -p
CREATE USER 'ejemplo_de_usuario'@'localhost' IDENTIFIED BY 'contraseña_que_decidas';
GRANT ALL PRIVILEGES ON plantsitters_db.* TO 'ejemplo_de_usuario'@'localhost';
FLUSH PRIVILEGES
```

5. Update the **environment** from the `.env` file in the project root with the details of a user who has permissions on the DB. That is, the root user, or the one you created in the previous step.

```
DB_USER=root
DB_PASSWORD=contraseña_del_usuario_root
```

6. Apply the **migrations** to create the DB tables in MySQL: `python manage.py migrate`
7. Create a Django **superuser**. You can do it manually from the shell or with `python manage.py createsuperuser`, but we have created a custom command that can help you if you want no hassle: `python manage.py create_super_user`
8. **Start the development server** `python manage.py runserver`
9. Have fun testing the server at `http://127.0.0.1:8000/`

&nbsp;

> Note: To manage tasks you need to be authenticated. To do so, you will have to add a **token** to your requests to the server. You can easily get one by entering your user details at `api-token-auth/`. Also keep in mind that to delete tasks, you must be an admin or the user who created them.

&nbsp;

## Key technical details

- To speed up CRUD operations, both **ViewSets** and **generic views** have been used to manage tasks and users.
- There is a **custom API View** that links the user and task models. It returns all the tasks associated with a specific user.
- This is a **portable** project. Using a `.env` file we can configure the DB credentials securely and flexibly without modifying the source code. In addition, the `requirements.txt` file makes it easy to create virtual environments to run the project on any system.
- The application is **scalable** thanks to the capabilities of **MySQL**, which can handle traffic and data volume more efficiently than SQLite.
- Tools are used for creating and authenticating users. There are also two **user groups**, Requester and Plantsitter, which make it possible to define capabilities and permissions within the system depending on the user's role.

&nbsp;

## Usage examples

_Creating "tasks" in the DB from `/admin`_

![image](https://github.com/user-attachments/assets/e299da3a-d369-4105-b7b8-90cfc2ae6c39)

_Testing the endpoint to update tasks from `/api`_

![image](https://github.com/user-attachments/assets/19d2bcb6-42a3-49f1-b7c7-5484bcbb599e)
