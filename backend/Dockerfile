FROM continuumio/miniconda3

WORKDIR /app

RUN conda create -n cadquery-env -c conda-forge python=3.11 cadquery -y

SHELL ["conda", "run", "-n", "cadquery-env", "/bin/bash", "-c"]

# Now this works because root context includes requirements.txt
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend folder
COPY backend/ ./backend/

EXPOSE 8080

CMD ["conda", "run", "--no-capture-output", "-n", "cadquery-env", "uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8080"]