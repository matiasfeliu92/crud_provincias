The backend of the project is a REST API that contains all the endpoints to perform different actions, such as obtaining all the provinces, cities and regions of Argentina, you can also obtain provinces, cities and regions by ID and create new ones.

For the database, PostgreSQL is used for production and Sqlite3 for development.

This was achieved using the following technologies.

- Python
- Django
- PostgreSql

To install the dependencies, you must first enter the server folder with "cd server" command, install the module to create virtual environments, executing the following command in the terminal:

```
pip install virtualenv
```

Then you have to create the environment with the following command:

```
virtualenv prov
```

Then you have to activate the virtual environment with the following command:

```
prov/Scripts/activate
```

Finally to execute the project we use the following command:

```
python manage.py runserver
```

To run the database migrations, we use the following command:

```
python manage.py makemigrations
```

then:

```
python manage.py migrate
```

To run the tests in the project, we do it with the following command:

```
python manage.py test provincesCrud
```

## Routes

**
All paths start with "/provinces/

|   Route   | HTTP Verb |   Description   |
|-----------|-----------|-----------------|
| `/`       |    GET    | Returns all provinces |
| `/cities` |    GET    | Return all cities |
| `/regions` |    GET    | Return all regions |
| `/<int:id>` |    GET    | Returns the province that contains that id |
| `/cities/<int:id>` |    GET    | Returns the province that contains that id |
| `/regions/<int:id>` |    GET    | Returns the region that contains that id |
| `/new_prov` |    POST    | Allows you to create a new province |