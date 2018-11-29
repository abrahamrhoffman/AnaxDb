# AnaxDb
<i>An encrypted non-linear database based on Pandas</i>

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
Created: '{pwd}/config.ini'
```

Anax controls the database parameters through a config file: 'config.ini' By default, Anax will look in '{pwd}/config.ini' and,  if not present, generate the file for you. You can override this behavior with `config_path="<some_path>"`.

The database is set up!

### Connect to the Database

Create a new database connection:

```
anax = anax.Database()
```

You are now connected.

```
anax.tables()

['users']
```

```
anaxdb.read("users")

                                uid username              email  password  admin
0  54c355db7d3d432ca8bfea093affb501    admin  admin@example.com  YWRtaW4=   True
```

There is much more to Anax. For more examples click <a href="https://github.com/abrahamrhoffman/AnaxDb/tree/master/examples">here</a>.

