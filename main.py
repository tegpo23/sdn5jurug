from fastapi import FastAPI

app = FastAPI(
    title="SD School API",
    version="1.0.0",
    description="Aplikasi Web untuk Manajemen Sekolah Dasar"
)

@app.get("/")
def home():
    return {"message": "Welcome to SD School App!"}
