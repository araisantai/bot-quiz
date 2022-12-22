#! /bin/bash
source venv/bin/activate
python3 manage.py runserver 0.0.0.0:9080
python3 bot.py
