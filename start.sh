#!/bin/bash

# Start MLflow server in background
mlflow ui --host 0.0.0.0 --port 5000 &

# Start FastAPI backend
uvicorn backend.main:app --host 0.0.0.0 --port 8000
