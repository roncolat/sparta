import vtk

# Crea punti
points = vtk.vtkPoints()
points.InsertNextPoint(0, 0, 0)
points.InsertNextPoint(1, 0, 0)
points.InsertNextPoint(0, 1, 0)

# Crea triangolo
triangles = vtk.vtkCellArray()
triangle = vtk.vtkTriangle()
triangle.GetPointIds().SetId(0, 0)
triangle.GetPointIds().SetId(1, 1)
triangle.GetPointIds().SetId(2, 2)
triangles.InsertNextCell(triangle)

# Crea polydata
polydata = vtk.vtkPolyData()
polydata.SetPoints(points)
polydata.SetPolys(triangles)

# Scrivi file
writer = vtk.vtkXMLPolyDataWriter()
writer.SetFileName("triangolo.vtp")
writer.SetInputData(polydata)
writer.Write()