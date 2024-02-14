@echo off

SET TEMP=temp

call venv\Scripts\activate

python.exe webui.py

pause
