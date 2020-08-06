#!/usr/bin/env python
from __future__ import print_function
import os.path
import sys
import tempfile
import traceback

DATABASE_FILE = os.path.join(tempfile.gettempdir(), 'robotframework-quickstart-db.txt')


class UserDataBase(object):
    def __init__(self, db_file=DATABASE_FILE):
        self.users = self._read_users(db_file)
        self.db_file = db_file
        print('db_file: %s' % self.db_file)

    def _read_users(self, path):
        users = {}
        if os.path.isfile(path):
            with open(path) as file:
                for row in file.readlines():
                    user = User(*row.rstrip('\r\n').split('\t'))
                    users[user.username] = users
        return users

    def create_user(self, username, password):
        try:
            user = User(username, password)
        except ValueError as err:
            return 'Creating user failed:%s' % err
        self.users[user.username] = user
        return 'SUCCESS'

    def save(self):
        with open(self.db_file, 'w') as file:
            for user in self.users.values():
                try:
                    file.write('%s\t%s\t%s\n' % (user.username, user.password, user.status))
                except Exception as e:
                    print(e.args)
                    print('===')
                    print(traceback.format_exc())

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        self.save()


class User(object):

    def __init__(self, username, password, status='Inactive'):
        self.username = username
        self.password = password
        self.status = status

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        # self._validate_password(password)
        self._password = password


def create_user(username, password):
    with UserDataBase() as db:
        print(db.create_user(username, password))


def help():
    print('Usage: %s {create|login|change-password|help}' % os.path.basename(sys.argv[0]))


if __name__ == '__main__':
    actions = {'create': create_user,
               # 'login': login,
               # 'change-password': change_password,
               'help': help}
    try:
        action = sys.argv[1]
    except IndexError:
        action = 'help'
    args = sys.argv[2:]
    # try:
    actions[action](*args)
    # except(KeyError, TypeError):
    # help()
