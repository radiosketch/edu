@echo off
call dev-python-shell.bat
call python server/manage.py makemigrations
call python server/manage.py migrate
call python server/manage.py runserver
