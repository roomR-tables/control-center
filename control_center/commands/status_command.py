class StatusCommand:
    """
    Args:
        settings (helpers.settings_helper.Settings) Device settings
        mqtt_client (paho.mqtt.client.Client) MQTT client
        sqlite_conn (sqlite3.Connection) SQLite connection
    """
    def __init__(self, settings, mqtt_client, sqlite_conn):
        self.settings = settings
        self.mqtt_client = mqtt_client
        self.sqlite_conn = sqlite_conn

    def execute(self):
        status = self.settings.get('status')
        device_id = self.settings.get('device_id')

        self.mqtt_client.publish(topic="cc/" + device_id + "/status", payload=status, qos=1)
