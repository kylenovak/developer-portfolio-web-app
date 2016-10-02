from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import os

from kylejnovak import app, db


app.config.from_object(os.environ['APP_SETTINGS'])

migrate = Migrate(app, db)
manager = Manager(app)

# to run this command do: python manage.py db [init | migrate | upgrade | downgrade]
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
