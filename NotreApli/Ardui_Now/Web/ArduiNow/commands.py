# -*- coding: utf-8 -*-
"""Click commands."""
import os
from glob import glob
from subprocess import call

import click
from flask import current_app
from flask.cli import with_appcontext
from werkzeug.exceptions import MethodNotAllowed, NotFound

from extensions import db
from flask_security.script import CreateUserCommand, AddRoleCommand
from flask.ext.security.utils import encrypt_password
from user.models import User, Role
from flask import current_app
from flask.cli import with_appcontext


@click.command()
@with_appcontext
def create_db():
    """
    Install a default admin user and add an admin role to it.
    """
    #check if admin exists
    db.create_all()


@click.command()
@with_appcontext
def install():
    """
    Install a default admin user and add an admin role to it.
    """
    #check if admin exists
    a = Role.query.filter(Role.name =='admin').first()

    if a is None:
        r = Role(name='admin')
        db.session.add(r)
        db.session.commit()
        m = click.prompt('Admin Email?', default='admin@localhost')
        n = click.prompt('Admin Name ?', default='arduinow')
        p = click.prompt('Admin Password (min 6 characters)?', default='aarduinow')
        u = User(email=m, username=n, password=p, active=1)
        u.roles.append(r)
        db.session.add(u)
        db.session.commit()
    else:
        print('Seems like an Admin is already installed')


@click.command()
@click.option('-e', '--email', prompt=True, default=None)
@click.option('-p', '--password', prompt=True, default=None)
@with_appcontext
def reset(email, password):
    """
    Reset a user password
    """
    try:
        pwd = encrypt_password(password)
        u = User.query.filter(User.email == email).first()
        u.password = pwd
        db.session.commit()
        print ('User password has been reset successfully.')
    except Exception as e:
        print ('Error resetting user password: %s' % e)


@click.command()
def clean():
    """Remove *.pyc and *.pyo files recursively starting at current directory.
    Borrowed from Flask-Script, converted to use Click.
    """
    for dirpath, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            if filename.endswith('.pyc') or filename.endswith('.pyo'):
                full_pathname = os.path.join(dirpath, filename)
                click.echo('Removing {}'.format(full_pathname))
                os.remove(full_pathname)
