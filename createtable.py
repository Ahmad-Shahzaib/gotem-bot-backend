# import sqlite3

# # Define the database file name
# db_file = 'mydatabase2.db'

# # Establish a connection to the database (it will be created if it doesn't exist)
# conn = sqlite3.connect(db_file)
# cursor = conn.cursor()

# # Define the SQL command to crseate a table with the specified columns
# create_table_query = '''
# CREATE TABLE IF NOT EXISTS Users (
#   UserId TEXT PRIMARY KEY,
#     Username TEXT,
#     Refertotal TEXT,
  
#     X TEXT,
#     alreadydailyclaimed INTEGER,
#     claimedtotal INTEGER,
#     dailyclaimedtime INTEGER,
#     dailycombotime INTEGER,
#     discord TEXT,
#     facebook TEXT,
#     instagram TEXT,
#     invitedby TEXT,
#     miningstarttime TEXT,
#     rate TEXT,
#     telegram TEXT,
#     timeinminute TEXT,
#     totalcollectabledaily TEXT,
#     totalgot REAL,
#     youtube TEXT,
#     walletid TEXT,
#     referrewarded INTEGER
# );
# '''

# # Execute the SQL cosrmmand
# cursor.execute(create_table_query)

# # Commit the changes and close the conection
# conn.commit()
# conn.close()

# print(f"Database '{db_file}' created with the specified table and columns.")


# ..................................................................
# ..................................................................

# new_task_table

# ..................................................................



# import sqlite3

# # Connect to SQLite (or create the database if it doesn't exist)
# connection = sqlite3.connect('Tasks.db')

# # Create a cursor object to interact with the database
# cursor = connection.cursor()

# # Create the Taskdetails table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Taskdetails (
#     taskid INTEGER PRIMARY KEY,  -- Unique ID for each task
#     taskimage TEXT,              -- Link to the task image
#     taskreward INTEGER,          -- Reward associated with the task
#     tasktitle TEXT,               -- Title of the task
#     tasklink TEXT
# );
# ''')

# # Create the Taskdone table
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS Taskdone (
#     userid INTEGER PRIMARY KEY,  -- Unique ID for each user
#     tasks TEXT                   -- Tasks completed by the user, stored as comma-separated values
# );
# ''')

# # Commit changes and close the connection
# connection.commit()
# connection.close()

# print("Database and tables created successfully.")



# ..................................................................
# ..................................................................

# game_db

# ..................................................................


# import sqlite3

# # Connect to SQLite database (or create it if it doesn't exist)
# conn = sqlite3.connect('game.db')

# # Create a cursor object to execute SQL queries
# cursor = conn.cursor()

# # Create the table "gamers" with additional fields "hookspeedtime" and "multipliertime"
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS gamers (
#     userid INTEGER PRIMARY KEY,  -- Unique identifier for each gamer
#     hookspeed INTEGER,           -- Speed of the hook
#     multiplier INTEGER,          -- Multiplier value for the gamer
#     hookspeedtime INTEGER,       -- Time associated with hookspeed
#     multipliertime INTEGER
# )
# ''')

# # Commit the changes and close the connection
# conn.commit()
# conn.close()

# print("Database 'game.db' and table 'gamers' created successfully.")



import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('game.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Add the columns "startime" and "starmultiplier" to the "gamers" table
try:
    cursor.execute("ALTER TABLE gamers ADD COLUMN startime INTEGER")  # Add startime column
    cursor.execute("ALTER TABLE gamers ADD COLUMN starmultiplier INTEGER")  # Add starmultiplier column
    print("Columns 'startime' and 'starmultiplier' added successfully to the 'gamers' table.")
except sqlite3.OperationalError as e:
    print(f"An error occurred: {e}")

# Commit the changes and close the connection
conn.commit()
conn.close()