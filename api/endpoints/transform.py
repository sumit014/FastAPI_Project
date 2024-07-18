from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
import uuid
from typing import Dict, Any

router = APIRouter()

# Temporary storage for uploaded files (replace with proper storage in production)
UPLOAD_FOLDER = "./uploads"


class FileUploadResponse(BaseModel):
    message: str
    file_id: str


class TransformationRequest(BaseModel):
    transformations: Dict[str, Any]


@router.post("/transform/{file_id}", response_model=FileUploadResponse)
async def transform_data(file_id: str, request: TransformationRequest):
    file_path = os.path.join(UPLOAD_FOLDER, file_id + ".csv")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

    transformations = request.transformations

    # Example transformations: normalize and fill missing values
    if "normalize" in transformations:
        for column in transformations["normalize"]:
            df[column] = (df[column] - df[column].mean()) / df[column].std()

    if "fill_missing" in transformations:
        for column, value in transformations["fill_missing"].items():
            df[column].fillna(value, inplace=True)

    transformed_file_id = str(uuid.uuid4())
    transformed_file_path = os.path.join(UPLOAD_FOLDER, transformed_file_id + ".csv")

    df.to_csv(transformed_file_path, index=False)

    return {"message": "Transformations applied successfully", "file_id": transformed_file_id}
