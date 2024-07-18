from fastapi import APIRouter, HTTPException, Query
from api.utils.visualisation import generate_histogram, generate_scatter_plot
from fastapi.responses import StreamingResponse
import pandas as pd
import os
import io

router = APIRouter()

UPLOAD_FOLDER = "./uploads"


@router.get("/visualise/{file_id}")
async def visualize_data(file_id: str, chart_type: str = Query(...), columns: list = Query([])):
    file_path = os.path.join(UPLOAD_FOLDER, file_id + ".csv")

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading file: {str(e)}")

    if chart_type == "histogram":
        if not columns:
            raise HTTPException(status_code=400, detail="Columns must be specified for histogram")
        plot_bytes = generate_histogram(df, columns)

    elif chart_type == "scatter":
        if len(columns) != 2:
            raise HTTPException(status_code=400, detail="Scatter plot requires exactly 2 columns")
        plot_bytes = generate_scatter_plot(df, columns[0], columns[1])

    else:
        raise HTTPException(status_code=400, detail="Unsupported chart type")

    return StreamingResponse(io.BytesIO(plot_bytes), media_type="image/png")
