from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse
import cadquery as cq
import zipfile


from backend.services import generate_cad_code

router = APIRouter()

class CADRequest(BaseModel):
    prompt: str

@router.post("/cad")
def generate_cad(request: CADRequest):
    
    # 🔥 Step 1: Generate code using LLM
    cad_code = generate_cad_code(request.prompt)

    try:
        # 🔥 Step 2: Execute safely
        result = eval(cad_code, {"cq": cq})

    except Exception as e:
        return {"error": str(e), "generated_code": cad_code}

    # 🔥 Step 3: Export files
    step_path = "model.step"


    cq.exporters.export(result, step_path)

    # 🔥 Step 4: Zip files
    zip_path = "model.zip"
    with zipfile.ZipFile(zip_path, "w") as z:
        z.write(step_path)

    return FileResponse(zip_path, media_type="application/zip", filename="model.zip")