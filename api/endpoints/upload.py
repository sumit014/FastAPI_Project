from fastapi import APIRouter, UploadFile, File, HTTPException
from pydantic import BaseModel
import uuid
import os

router = APIRouter()

# Temporary storage for uploaded files (replace with proper storage in production)
UPLOAD_FOLDER = "./uploads"

# Ensure upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


class FileUploadResponse(BaseModel):
    message: str
    file_id: str


@router.post("/upload", response_model=FileUploadResponse)
async def upload_file(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())  # Generate a unique file ID
    file_path = os.path.join(UPLOAD_FOLDER, file_id + ".csv")

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"message": "File uploaded successfully", "file_id": file_id}
