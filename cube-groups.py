import GEOM
import sys
import salome

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--dx", type=float, help="set dx length")
...
args = parser.parse_args()

geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)

Box_1 = geompy.MakeBoxDXDYDZ(args.dx, args.dy, args.dz)
Cylinder_1 = geompy.MakeCylinderRH(args.R, args.H)
geompy.TranslateDXDYDZ(Cylinder_1, args.dx/2., args.dy/2., -args.dz/4.)
Cut_1 = geompy.MakeCutList(Box_1, [Cylinder_1], True)

T = geompy.MakeVertex(0, 0, args.dz)
Top = geompy.GetShapesOnPlaneWithLocation(Cut_1, geompy.ShapeType["FACE"], OZ, T, GEOM.ST_ON)
GTop = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
geompy.UnionList(GTop, Top)
geompy.addToStudyInFather(Cut_1, GTop, "GTop")

Hole_Faces = geompy.GetShapesOnShape(Cylinder_1, Cut_1, geompy.ShapeType["FACE"], GEOM.ST_ONIN)
print(f"Len(faces)={len(Hole_Faces)}”)
HoleBord = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
faces_ids = [geompy.GetSubShapeID(Cut_1, sub_face) for sub_face in Hole_Faces]
geompy.UnionIDs(HoleBord, faces_ids)
Bord = geompy.CreateGroup(Cut_1, geompy.ShapeType["FACE"])
Faces = geompy.ExtractShapes(Cut_1, geompy.ShapeType["FACE"]) 
geompy.UnionList(Bord, Faces)
geompy.DifferenceList(Bord, Hole_Faces)
