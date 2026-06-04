#!/usr/bin/env bash
set -e

pip install -r requirements.txt
python seed.py
uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-3001}
