@echo off
call ./venv/Scripts/activate.bat
cd "Software Engineering/GUI Design/GIF Editor/""
call python main.py
cd ../../../
call deactivate
