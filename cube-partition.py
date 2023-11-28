from salome.geom import geomBuilder
import sys
import math
import GEOM
import SALOMEDS

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

Fuse_1 = geompy.MakeFuseList([Box_1, Cylinder_1], True, True)
Partition_1 = geompy.MakePartition([Box_1, Cylinder_1], [], [], [], geompy.ShapeType["SOLID"], 0, [], 0)

