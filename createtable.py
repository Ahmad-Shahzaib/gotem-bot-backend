import sqlite3

# Define the database file name
db_file = 'mydatabase2.db'

# Establish a connection to the database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Define the SQL command to create a table with the specified columns
create_table_query = '''
CREATE TABLE IF NOT EXISTS Users (
  UserId TEXT PRIMARY KEY,
    Username TEXT,
    Refertotal TEXT,
  
    X TEXT,
    alreadydailyclaimed INTEGER,
    claimedtotal INTEGER,
    dailyclaimedtime INTEGER,
    dailycombotime INTEGER,
    discord TEXT,
    facebook TEXT,
    instagram TEXT,
    invitedby TEXT,
    miningstarttime TEXT,
    rate TEXT,
    telegram TEXT,
    timeinminute TEXT,
    totalcollectabledaily TEXT,
    totalgot REAL,
    youtube TEXT,
    walletid TEXT
);
'''

# Execute the SQL command
cursor.execute(create_table_query)

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Database '{db_file}' created with the specified table and columns.")