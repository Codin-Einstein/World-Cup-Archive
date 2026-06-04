#!/usr/bin/env bash
set -e

pip install -r server/requirements.txt
cd server && uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-3001}
