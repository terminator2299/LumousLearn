# Use official Python slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend ./backend
COPY ml_pipeline ./ml_pipeline

# Expose ports for FastAPI and MLflow UI
EXPOSE 8000
EXPOSE 5000

# Start both FastAPI and MLflow servers using a simple script
COPY start.sh .
RUN chmod +x start.sh

CMD ["./start.sh"]
