import click
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3

# get database
def get_db():
    # g is a special object that is unique for each request
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # return rows that behave like dicts (columns)
        g.db.row_factory = sqlite3.Row

    return g.db

# checks if connection made by checking g.db was set
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

###

# run sql commands
def init_db():
    db = get_db()
    # to open file relative to flaskr package
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    # defines a command line command called init-db that calls the init_db
    # function and shows a success message to the user. 
    click.echo('Initialized the database.')


###

# register functions with application instance
def init_app(app):
    app.teardown_appcontext(close_db) # call close_db when cleaning up
    app.cli.add_command(init_db_command) # new command