FROM continuumio/miniconda3

WORKDIR /app

# Create conda environment
RUN conda create -n cadquery-env -c conda-forge python=3.11 cadquery -y

# Use conda env for all commands
SHELL ["conda", "run", "-n", "cadquery-env", "/bin/bash", "-c"]

# Install Python dependencies
COPY backend/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ ./backend/

# Expose correct port
EXPOSE 8080

# Start FastAPI (exec form ✅)
CMD ["conda", "run", "--no-capture-output", "-n", "cadquery-env", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]