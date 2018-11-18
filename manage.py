import os
import unittest


from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app.main.model import user
from app.main.model import family
from app.main.model import member
from app.main.model import item
from app.main.model import list

from app import blueprint

from app.main import create_app,create_page_routes,db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
create_page_routes(app)
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run(host='0.0.0.0')

@manager.command
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()