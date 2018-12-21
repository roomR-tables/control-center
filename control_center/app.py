import os
from configparser import ConfigParser
import json
import logging
import paho.mqtt.client as mqtt
import sqlite3

from commands import (status_command)
from helpers import settings_helper


def run():
    log = logging.basicConfig()
    config = ConfigParser()
    config.read(os.path.join(os.path.dirname(__file__), "../config.ini"))

    conn = sqlite3.connect('cc.db')
    conn.row_factory = sqlite3.Row

    # Init helpers
    settings = settings_helper.SettingsHelper(conn)

    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(mqtt_client, userdata, flags, rc):
        mqtt_client.subscribe("cc/" + settings.get('device_id') + "/cmd")

    # The callback for when a PUBLISH message is received from the server.
    def on_message(mqtt_client, userdata, msg):
        msg = msg.payload.decode("utf-8")

        try:
            msg_json = json.loads(msg)
        except json.JSONDecodeError as e:
            log.error("Error when decoding json: %s", e)
            return

        """
        A JSON message in the following response is expected:
        { "cmd": "calculate_movements", "payload": ... }
        """
        if msg_json["cmd"] == "request_status":
            status_command.StatusCommand(settings, mqtt_client, conn).execute()

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    try:
        client.connect(config.get("mqtt", "host"), int(config.get("mqtt", "port")), 60)
    except ConnectionError as e:
        log.error("Error when connecting to the MQTT broker: %s", e)
        exit(1)

    client.loop_forever()
