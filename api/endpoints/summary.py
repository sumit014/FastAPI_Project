from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from api.utils.data_operations import perform_data_analysis
import pandas as pd
import os

router = APIRouter()

# Temporary storage for uploaded files (replace with proper storage in production)
UPLOAD_FOLDER = "./uploads"


class SummaryResponse(BaseModel):
    summary: dict


@router.get("/summary/{file_id}", response_model=SummaryResponse)
async def get_summary(file_id: str):
    file_path = os.path.join(UPLOAD_FOLDER, file_id + ".csv")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

    summary_dict = perform_data_analysis(df)

    return {"summary": summary_dict}
