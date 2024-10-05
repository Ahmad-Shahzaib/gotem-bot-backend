import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('game.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create the table "gamers" with additional fields "hookspeedtime" and "multipliertime"
cursor.execute('''
CREATE TABLE IF NOT EXISTS gamers (
    userid INTEGER PRIMARY KEY,  -- Unique identifier for each gamer
    hookspeed INTEGER,           -- Speed of the hook
    multiplier INTEGER,          -- Multiplier value for the gamer
    hookspeedtime INTEGER,       -- Time associated with hookspeed
    multipliertime INTEGER       -- Time associated with multiplier
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database 'game.db' and table 'gamers' created successfully.")
