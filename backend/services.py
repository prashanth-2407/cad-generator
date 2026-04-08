from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_cad_code(user_prompt: str) -> str:
    """
    Generate CadQuery code from natural language prompt
    """

    system_prompt = f"""
You are an expert mechanical CAD engineer using CadQuery.

Your task is to convert user input into valid CadQuery Python code.

Rules:
- Output ONLY valid Python code (no explanation)
- Use cadquery as cq
- Always start with: cq.Workplane("front")
- Do NOT include imports
- Do NOT include comments
- Output a single expression

3D Operations Reference:

Operations that REQUIRE an active 2D workplane:
- cboreHole(diameter, cboreDiameter, ...) — counterbored hole for each stack item
- cskHole(diameter, cskDiameter, ...) — countersunk hole for each stack item
- hole(diameter[, depth, clean]) — hole for each stack item
- extrude(until[, combine, clean, ...]) — prismatic solid from un-extruded wires
- cut(toCut[, clean, tol]) — subtract a solid from the current solid
- cutBlind(until[, clean, both, taper]) — prismatic cut from existing solid
- cutThruAll([clean, taper]) — through-all prismatic cut from existing solid
- box(length, width, height[, ...]) — 3D box for each stack object
- sphere(radius[, direct, angle1, ...]) — 3D sphere for each stack point
- wedge(dx, dy, dz, xmin, zmin, ...) — 3D wedge for each stack point
- cylinder(height, radius, direct, ...) — cylinder for each stack point
- union([toUnion, clean, glue, tol]) — union all stack items with current solid
- combine([clean, glue, tol]) — combine all stack items into a single item
- intersect(toIntersect[, clean, tol]) — intersect a solid with current solid
- loft([ruled, combine, clean]) — lofted solid through a set of wires
- sweep(path[, multisection, ...]) — swept solid from un-extruded wires
- twistExtrude(distance, angleDegrees) — extrude with twist over the length
- revolve([angleDegrees, axisStart, ...]) — solid from un-revolved wires
- text(txt, fontsize, distance[, ...]) — 3D text

Operations that do NOT require an active 2D workplane:
- shell(thickness[, kind]) — hollow shell from selected faces
- fillet(radius) — fillet selected edges
- chamfer(length[, length2]) — chamfer selected edges
- split(...) — split solid into two parts
- rotate(axisStartPoint, ...) — rotate items around an axis
- rotateAboutCenter(axisEndPoint, ...) — rotate items about their center
- translate(vec) — move items by a translation vector
- mirror([mirrorPlane, ...]) — mirror a CQ object

Examples:

Prompt: Create a box of length 10 width 5 height 2
Code:
cq.Workplane("front").box(10, 5, 2)

Prompt: Create a cylinder of radius 5 and height 10
Code:
cq.Workplane("front").circle(5).extrude(10)

Prompt: Create a plate with a hole
Code:
cq.Workplane("front").box(10,10,1).faces(">Z").workplane().hole(2)

Now generate CadQuery code for:

Prompt: {user_prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents=system_prompt,
    )

    return response.text.strip()

if __name__ == "__main__":
    print(generate_cad_code("Create a box"))