import sqlite3

#conn = sqlite3.connect(':memory:')

# Connect to database || create database
conn = sqlite3.connect('list.db')

# Create a Cursor
c = conn.cursor()

# # Create a Table
c.execute("""CREATE TABLE list (
        ip text,
        url text,
        description text,
        category text,
        block boolean
        )""")

# Seed Data
many_items = [
    ('172.100.101.1', 'www.hax.com', 'Malicious Page', 'Website', 'True'),
    ('172.100.101.2', 'www.hax.com', 'Malicious Page', 'Website', 'True'),
    ('172.100.101.3', 'www.hax.com', 'Malicious Page', 'Website', 'True'),
]



# Insert into Table
# Insert Single Item
# c.execute("INSERT INTO list VALUES ('10.100.101.3', 'www.examples.com.au', 'Malicious Page', 'Website', 'True')")
# Insert Many Items (above)
c.executemany("INSERT INTO list VALUES (?,?,?,?,?)", many_items)

print("Command executed!")

# Query The Database
# Fetch all
# print(c.fetchall())
c.execute("SELECT * FROM list")
# Fetch one
# c.fetchone()
# Fetch many speicified
# c.fetchmany(5)


items = c.fetchall()
print("IP Address:    " + "     URL:   " + "   Description:   " + "Category:  " + "Block? ")
print("~~~~~~~~~~~    " + "     ~~~~   " + "   ~~~~~~~~~~~~   " + "~~~~~~~~~  " + "~~~~~ ")

for item in items:
    print(item[0] + ", " + item[1] + ", " + item[2] + ", " + item[3] + ", " +item[4])


# Commit out command
conn.commit()

# Close our connection
conn.close()