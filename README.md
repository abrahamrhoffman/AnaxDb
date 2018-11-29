# AnaxDb
An encrypted non-linear Pandas database

### Install AnaxDb

```
pip install anax
```

### Getting Started

```
import anax
```

Next, bootstrap a new database.

```
anax.Database(bootstrap=True);
```

The database is set up!

### Connect to the Database

Connect to the database:

```
anax = anax.Database()
```

Show tables.

```
anax.tables()

['users']
```

Read a table.

```
anaxdb.read("users")

                                uid username              email  password  admin
0  54c355db7d3d432ca8bfea093affb501    admin  admin@example.com  YWRtaW4=   True
```

There is much more to Anax. For more examples click <a href="https://github.com/abrahamrhoffman/AnaxDb/tree/master/examples">here</a>.

