import os
import sqlite3
import app

from helpers import serial_helper

if os.path.isfile('cc.db') is False:
    here = os.path.dirname(__file__)
    sqlinit = open(os.path.join(here, 'sql/schema.sql')).read()

    conn = sqlite3.connect('cc.db')
    conn.executescript(sqlinit)

    # Import some basic settings
    serialnumber = serial_helper.getserial()

    conn.execute("""UPDATE settings SET device_id = :serial""", {"serial": serialnumber})
    conn.commit()

    conn.close()

app.run()
