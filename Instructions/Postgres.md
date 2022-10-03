How to connect postgresDB to flask
https://towardsdatascience.com/sending-data-from-a-flask-app-to-postgresql-database-889304964bf2
```python
    pip install flask_sqlalchemy
    pip install psycopg2-binary #for using postgres
```

The SQLALCHEMY_DATABASE_URI is a string describing our database connection. For the puposes of this article that connection is local, and can be described as follows:

```
engine:[//[user[:password]@][host]/[dbname]]
engine -> postgresql
user -> postgres (see `owner` field in previous screenshot)
password -> password (my db password is the string, `password`)
host -> localhost (because we are running locally on out machine)
dbname -> flasksql (this is the name I gave to the db in the previous step)

```