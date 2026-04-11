from fastapi import APIRouter, BackgroundTasks
from pydantic import BaseModel
from fastapi.responses import FileResponse
import cadquery as cq
import zipfile
import os
import tempfile

from services import generate_cad_code

router = APIRouter()


# ✅ Request schema
class CADRequest(BaseModel):
    prompt: str


# ✅ Cleanup function
def cleanup_files(*paths):
    for path in paths:
        if os.path.exists(path):
            try:
                os.remove(path)
            except Exception as e:
                print(f"Cleanup failed for {path}: {e}")


# ✅ API Endpoint
@router.post("/cad")
def generate_cad(request: CADRequest, background_tasks: BackgroundTasks):

    # 🔥 Step 1: Generate CAD code using LLM
    cad_code = generate_cad_code(request.prompt)

    try:
        local_vars = {}

        # 🔥 Step 2: Execute generated CAD code
        exec(
            cad_code,
            {"cq": cq},   # restricted globals
            local_vars
        )

        result = local_vars.get("result")

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

    # 🔥 Step 3: Create temporary files
    step_file = tempfile.NamedTemporaryFile(delete=False, suffix=".step")
    zip_file = tempfile.NamedTemporaryFile(delete=False, suffix=".zip")

    step_path = step_file.name
    zip_path = zip_file.name

    try:
        # 🔥 Step 4: Export STEP file
        cq.exporters.export(result, step_path)

        # 🔥 Step 5: Zip the file
        with zipfile.ZipFile(zip_path, "w") as z:
            z.write(step_path, arcname="model.step")

    except Exception as e:
        return {
            "error": f"Export failed: {str(e)}",
            "generated_code": cad_code
        }

    finally:
        # ✅ Delete STEP file immediately
        if os.path.exists(step_path):
            try:
                os.remove(step_path)
            except Exception as e:
                print(f"STEP cleanup failed: {e}")

    # ✅ Schedule ZIP cleanup AFTER response
    background_tasks.add_task(cleanup_files, zip_path)

    # 🔥 Step 6: Return ZIP file
    return FileResponse(
        path=zip_path,
        media_type="application/zip",
        filename="model.zip"
    )