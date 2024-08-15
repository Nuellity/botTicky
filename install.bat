@echo off
echo Installing dependencies...
python -m venv .venv
call .venv\Scripts\activate
pip install -r requirements.txt