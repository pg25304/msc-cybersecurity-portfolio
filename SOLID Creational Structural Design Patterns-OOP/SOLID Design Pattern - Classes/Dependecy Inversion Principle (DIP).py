class Database:
    def connect(selfself):
        pass
class MySQLDatabase(Database):
    def connect(self):
        print("connect to MYSQL")

class App:
    def __init__(self, db: Database):
        self.db = db

app =App(MySQLDatabase())