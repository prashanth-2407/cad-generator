FROM continuumio/miniconda3

WORKDIR /app

# Create environment with cadquery
RUN conda create -n cadquery-env -c conda-forge python=3.11 cadquery -y

# Activate env
SHELL ["conda", "run", "-n", "cadquery-env", "/bin/bash", "-c"]

# Install other Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy code
COPY backend/ ./backend/

EXPOSE 8000

CMD uvicorn backend.main:app --host 0.0.0.0 --port 8000