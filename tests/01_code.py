import cadquery as cq

result = cq.Workplane("XY").box(10, 10, 10)

# Export instead of show
cq.exporters.export(result, 'box.step')

print("STL file generated!")