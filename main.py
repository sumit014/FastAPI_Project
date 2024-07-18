from fastapi import FastAPI
from api.endpoints import upload, summary, transform, visualise
from fastapi.staticfiles import StaticFiles
from pathlib import Path

app = FastAPI()
# Define the directory where static files are located
static_dir = Path(__file__).parent / 'static'  # Adjust 'static' to your actual directory name

# Mount the directory to serve static files
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Include routers from each endpoint
app.include_router(upload.router, prefix="/api")
app.include_router(summary.router, prefix="/api")
app.include_router(transform.router, prefix="/api")
app.include_router(visualise.router, prefix="/api")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

