import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

# import Cut_1 from Xao or use previous scripts

Mesh_1 = smesh.Mesh(Cut_1)
NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D)
NETGEN_3D_Simple_Parameters_1 = NETGEN_1D_2D_3D.Parameters(smeshBuilder.SIMPLE)
NETGEN_3D_Simple_Parameters_1.SetNumberOfSegments( 15 )
Box_1_1 = Mesh_1.GroupOnGeom(Cut_1,'Cut_1',SMESH.VOLUME)
Face_1_1 = Mesh_1.GroupOnGeom(GTop,'Face_1',SMESH.FACE)
…
isDone = Mesh_1.Compute()
[ Box_1_1, Face_1_1, Face_2_1, Face_3_1, Face_4_1, Face_5_1, Face_6_1 ] = Mesh_1.GetGroups()

## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
smesh.SetName(NETGEN_3D_Simple_Parameters_1, 'NETGEN 3D Simple Parameters_1')
smesh.SetName(Face_1_1, 'Face_1')
…
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Box_1_1, 'Cut_1')
