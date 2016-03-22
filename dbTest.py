import MySQLdb
import time

#        replace mysql.server with "localhost" if you are running via your own server!
#                        server     MySQL username	MySQL pass  Database name.
conn = MySQLdb.connect("localhost","root","","tweets")

c = conn.cursor()

username='kev_barasa'

tweet='Python is interesting'

c.execute("INSERT INTO test (time, username, tweet) VALUES (%s,%s,%s)",
            (time.time(), username, tweet))

conn.commit()