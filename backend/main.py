import uvicorn

from fastapi.middleware.cors import CORSMiddleware

print("🔥 Starting app...")

from fastapi import FastAPI
from routes import router

print("🔥 Starting app...")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

print("🚀 App ready")

@app.get("/")
def root():
    return {"status": "ok"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
