# AnaxDb
An encrypted non-linear database based on Pandas

<a href="https://asciinema.org/a/1Zedo6gkiRrp5M5FyKaRLVXpd"><img src="https://asciinema.org/a/1Zedo6gkiRrp5M5FyKaRLVXpd.png" width="836"/></a>

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

### Using the Database

Connect:

```
anax = anax.Database()
```

Show tables:

```
anax.tables()

['users']
```

Read a table:

```
anax.read("users")

                                uid username              email  password  admin
0  54c355db7d3d432ca8bfea093affb501    admin  admin@example.com  YWRtaW4=   True
```

There is much more to Anax. For examples and explanations click <a href="https://github.com/abrahamrhoffman/AnaxDb/tree/master/examples">here</a>.

