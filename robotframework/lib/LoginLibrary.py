#!/usr/bin/env python
# encoding=utf-8
import os.path
import subprocess
import sys


class LoginLibrary(object):
    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__), '..', 'login.py')
        self._status = ''

    def create_user(self, username, password):
        self._run_command('create', username, password)

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()
