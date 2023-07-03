import gmsh
import math
import sys

gmsh.initialize()

gmsh.model.add("t16")

# We can log all messages for further processing with:
gmsh.logger.start()

v_b = [0.0, 0.0, 0.0]
# lens = [2.0, 2.4]

# 长宽高
len_dx = 1.0
len_dy = 1.0
len_dz = 1.0
rb = False

# n_dx nd_y nd_z 每层的划分数
# h_dx h_dy h_dz 每层的高度（累计高度，归一化）

n_dx = [1, 1]
h_dx = [0.5, 1.0]
n_dy = [1, 1]
h_dy = [0.5, 1.0]
n_dz = [1, 1, 1]
h_dz = [0.3, 0.7, 1.0]

# n_dx = [1, 1]
# h_dx = [0.5, 1.0]
# n_dy = [1, 1]
# h_dy = [0.5, 1.0]
# n_dz = [1, 1]
# h_dz = [0.5, 1.0]

# We first create a cuboid:
# rec = gmsh.model.occ.addRectangle(v_b[0], v_b[1], v_b[2], lens[0], lens[1])

v_l = [] # 点集合
c_l = [] # 曲线集合
dt_l = [] # dimtags集合

v = gmsh.model.occ.add_point(v_b[0], v_b[1], v_b[2])
# v_l.append(v)

dimtags = gmsh.model.occ.extrude([(0, v)], len_dx, 0, 0, n_dx, h_dx) # heights 层高（百分比，累计高度）
dt_l.append(dimtags)
# print(dimtags)
dimtags = gmsh.model.occ.extrude([(1, dimtags[1][1])], 0, len_dy, 0, n_dy, h_dy, recombine=rb) # heights 层高（百分比，累计高度）
dt_l.append(dimtags)
# print(dimtags)
dimtags = gmsh.model.occ.extrude([(2, dimtags[1][1])], 0, 0, len_dz, n_dz, h_dz, recombine=rb) # heights 层高（百分比，累计高度）
dt_l.append(dimtags)
print(dimtags)

# gmsh.model.occ.addBox(0, 0, 0, 1, 1, 1, 1)
gmsh.model.occ.synchronize()

gmsh.model.mesh.generate(3)
# gmsh.write("cuboid_aniso.mesh")
# gmsh.write("cuboid_aniso2.mesh")
gmsh.write("cuboid_aniso3_tet.mesh")

if '-nopopup' not in sys.argv:
    gmsh.fltk.run()

gmsh.finalize()