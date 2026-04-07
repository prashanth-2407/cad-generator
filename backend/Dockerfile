# filepath: backend/Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies for CadQuery/OpenCASCADE
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglu1-mesa \
    libfreetype6 \
    libxrender1 \
    libxkbcommon0 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first for caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
