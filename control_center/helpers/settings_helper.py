class SettingsHelper:
    def __init__(self, sqlite_conn):
        self.sqlite = sqlite_conn

    def get(self, name):
        c = self.sqlite.cursor()
        c.execute('SELECT * FROM `settings`')

        return c.fetchone()[name]

    def set(self, name, value):
        c = self.sqlite.cursor()
        c.execute('UPDATE `settings` SET `:name` = :value', {"name": name, "value": value})
