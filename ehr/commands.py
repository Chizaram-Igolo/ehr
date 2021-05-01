import click
from flask.cli import with_appcontext

from ehr.create_db import db, Admin, Patient, Staff, DiagnoseTable

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()