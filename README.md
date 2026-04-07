# CAD Generator

A web application for generating CAD models using natural language queries. The backend uses FastAPI with RAG (Retrieval Augmented Generation) to understand CAD-related queries, while the frontend provides a React-based interface for interacting with the system.

## Features

- Natural language to CAD model generation
- RAG-powered query handling using CadQuery documentation
- REST API with Swagger documentation
- React frontend with Vite build system
- CORS-enabled for local development

## Tech Stack

- **Backend**: FastAPI, Uvicorn, CadQuery
- **Frontend**: React 18, Vite
- **RAG**: FAISS index, sentence embeddings

## Project Structure

```
cad_generator/
├── backend/           # FastAPI backend
│   ├── main.py       # Application entry point
│   ├── routes.py     # API routes
│   ├── services.py   # Business logic
│   └── rag/          # RAG components for CAD query handling
├── frontend/         # React + Vite frontend
│   └── src/          # React components
├── tests/            # Test files
├── requirements.txt  # Python dependencies
└── README.md         # This file
```

## Getting Started

### Prerequisites

- Python 3.10+
- Node.js 18+

### Backend Setup

1. Copy the environment template:
```powershell
cp backend\.env.example backend\.env
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

## Testing

Run Python tests:
```powershell
cd tests
python 01_code.py
```

## License

MIT