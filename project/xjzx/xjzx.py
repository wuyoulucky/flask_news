from app import create_app
from flask_script import Manager
from config import DevelopConfig
from flask_migrate import MigrateCommand,Migrate
from models import db
app=create_app(DevelopConfig)
manager=Manager(app)
db.init_app(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)
if __name__ == '__main__':
    manager.run()