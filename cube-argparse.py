from salome.geom import geomBuilder
import math
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
Cylinder_1 = geompy.MakeCylinder(O, OZ, 80, 300)
geompy.TranslateDXDYDZ(Cylinder_1, 100, 100, -50)
Cut_1 = geompy.MakeCutList(Box_1, [Cylinder_1], True)

geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( Box_1, 'Box_1' )
geompy.addToStudy( Cylinder_1, 'Cylinder_1' )
geompy.addToStudy( Cut_1, 'Cut_1' )

if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
