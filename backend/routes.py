from fastapi import APIRouter
from pydantic import BaseModel
from fastapi.responses import FileResponse
import cadquery as cq
import zipfile
import uuid
import os

from backend.services import generate_cad_code

router = APIRouter()

class CADRequest(BaseModel):
    prompt: str


@router.post("/cad")
def generate_cad(request: CADRequest):

   
    cad_code = generate_cad_code(request.prompt)
    

    try:
        local_vars = {}

        exec(
            cad_code,
            {"cq": cq},   # restricted globals
            local_vars    # capture variables here
        )

        result = local_vars.get("result")
        print(result)

        if result is None:
            return {
                "error": "No 'result' object found in generated code",
                "generated_code": cad_code
            }

    except Exception as e:
        return {
            "error": str(e),
            "generated_code": cad_code
        }

    file_id = str(uuid.uuid4())

    step_path = f"{file_id}.step"
    zip_path = f"{file_id}.zip"

    try:
        # 🔥 Step 4: Export STEP file
        cq.exporters.export(result, step_path)

        # 🔥 Step 5: Zip the file
        with zipfile.ZipFile(zip_path, "w") as z:
            z.write(step_path)

    except Exception as e:
        return {
            "error": f"Export failed: {str(e)}",
            "generated_code": cad_code
        }

    finally:
        # Optional cleanup of STEP file after zipping
        if os.path.exists(step_path):
            os.remove(step_path)

    # 🔥 Step 6: Return ZIP file
    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="model.zip"
    )