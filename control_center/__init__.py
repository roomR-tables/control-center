import os
import sqlite3
import app

from helpers import serial_helper

if os.path.isfile('cc.db') is False:
    sqlinit = open('sql/schema.sql').read()

    conn = sqlite3.connect('cc.db')
    conn.executescript(sqlinit)

    # Import some basic settings
    serialnumber = serial_helper.getserial()
    conn.execute('UPDATE `settings` SET `device_id` = :serial', {"serial": serialnumber})

    conn.close()

app.run()
