# CAD Generator

A web application for generating CAD models from natural language input. The backend uses FastAPI and a prompt-driven approach (no RAG) to interpret user queries and generate CAD code using CadQuery, while the frontend provides an interactive React-based UI.

---

## 🚀 Features

- Natural language → CAD model generation
- Prompt-based query interpretation (no RAG)
- FastAPI backend with REST API
- React frontend (Vite)
- Dockerized setup (backend + frontend)
- Simple and scalable architecture

---

## 🧠 How It Works

1. User enters a natural language prompt  
   *(e.g., "Create a cylinder with radius 10mm and height 50mm")*

2. Backend sends the prompt to an LLM with a predefined system prompt

3. The model generates **CadQuery code**

4. Backend executes the code and returns the result

---

## 🛠 Tech Stack

### Backend
- FastAPI
- Uvicorn
- CadQuery
- Python

### Frontend
- React 18
- Vite

### Deployment
- Docker
- Docker Compose
- Nginx

---

## 📁 Project Structure


## Project Structure

```
cad_generator/
├── backend/
│ ├── main.py
│ ├── routes.py
│ ├── services.py
│ ├── requirements.txt
│ ├── Dockerfile
│ └── .env.example
│
├── frontend/
│ ├── src/
│ │ ├── App.jsx
│ │ ├── main.jsx
│ │ └── index.css
│ ├── index.html
│ ├── package.json
│ ├── vite.config.js
│ ├── nginx.conf
│ ├── Dockerfile
│ └── .env
│
├── tests/
├── docker-compose.yml
├── .env
├── .gitignore
├── LICENSE
└── README.md
```


---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+
- Docker (optional but recommended)

---

## 🔧 Backend Setup (Local)

```bash
cd backend
cp .env.example .env
```

2. Edit `backend/.env` and add your Google API key.

3. Install dependencies and run:
```powershell
cd backend
pip install -r ../requirements.txt
python main.py
```

The backend runs on `http://localhost:8000` and provides Swagger docs at `http://localhost:8000/docs`.

### Frontend Setup

```powershell
cd frontend
npm install
npm run dev
```

The frontend runs on `http://localhost:5173`.

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/generate` | Generate CAD model from query |


## License

MIT