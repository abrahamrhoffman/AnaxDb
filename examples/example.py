import anaxdb

# Wipe and build fresh database in local folder
#anaxdb.Database(bootstrap=True);
# Wipe and build fresh database in object storage
anaxdb.Database(bootstrap=True, object_storage=True);

# Local storage
#anax = anaxdb.Database()
# Object Storage
anax = anaxdb.Database(object_storage=True)

# Read a table
anax.tables()
anax.read("users")

# Create a table
my_numbers = [1,2,3,4,5]
my_table = {"my_numbers": my_numbers}
anax.create("my_table", my_table)
anax.tables()
anax.read("my_table")

# Anax Syntax :: Select
my_table = anax.read("my_table")
# "my_table" is now a Pandas Dataframe object!
# Use pandas syntax to interact with it.

# Pandas specific syntax
my_table[my_table.my_numbers == 3]

# More Pandas specific syntax
my_table.loc[my_table.my_numbers == 3,]

# SQL-like syntax with variables
num = 3
my_table.query("my_numbers == @num")

# Modify a table

# Change "3" to "13"
my_table.loc[my_table.my_numbers == 3,] = 13

# Write changes to database
anax.write(my_table, "my_table")

# Verify changes
anax.read("my_table")
