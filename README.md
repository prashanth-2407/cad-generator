# CAD Generator

A web application for generating CAD models using FastAPI backend and React frontend.

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

### Backend

```powershell
cd backend
pip install -r ../requirements.txt
python main.py
```

The backend runs on `http://localhost:8000` and provides Swagger docs at `http://localhost:8000/docs`.