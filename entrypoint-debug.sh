#! /bin/bash
pip install -U debugpy
python -m debugpy --listen 0.0.0.0:5678 main.py