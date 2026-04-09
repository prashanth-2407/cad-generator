FROM continuumio/miniconda3

WORKDIR /app

# Create conda environment with cadquery
RUN conda create -n cadquery-env -c conda-forge python=3.11 cadquery -y

# Use conda environment for all commands
SHELL ["conda", "run", "-n", "cadquery-env", "/bin/bash", "-c"]

# Install Python dependencies
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy all backend code
COPY . .

# Cloud Run requires this port
EXPOSE 8080

# Start FastAPI app
CMD ["conda", "run", "--no-capture-output", "-n", "cadquery-env", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]