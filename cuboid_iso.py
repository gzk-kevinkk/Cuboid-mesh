import gmsh
import math
import sys

gmsh.initialize()

gmsh.model.add("t16")

# We can log all messages for further processing with:
gmsh.logger.start()

v_b = [-1.0, -1.2, -1.5]
lens = [2.0, 2.4, 3.0]
n = 4

# We first create a cuboid:
cuboid = gmsh.model.occ.addBox(v_b[0], v_b[1], v_b[2], lens[0], lens[1], lens[2])
# gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1, 1)
gmsh.model.occ.synchronize()

for i in range(1, 13):
    gmsh.model.mesh.setTransfiniteCurve(i, n) # 将曲线均匀划分

for i in range(1, 7):
    gmsh.model.mesh.setTransfiniteSurface(i) # 将曲面划分
    gmsh.model.mesh.setRecombine(2, i) # recombine 得到四边形网格

gmsh.model.mesh.setTransfiniteVolume(cuboid) # 将实体划分

gmsh.model.mesh.generate(3)
gmsh.write("cuboid_iso.mesh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()