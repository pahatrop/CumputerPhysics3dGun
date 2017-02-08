# -*- coding: UTF-8 -*-
from Physic import *
import math
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


B = Body("test", 0.04, 45)
B.X0 = 100
B.Y0 = 100
# Пусть начальные координаты пушки (100, 100) в нормальных координатах.

xarray = []
yarray = []
dt = 0.01
v_max = 50

while(B.Y >= -0.01): # сначала получаем траекторию в плоскости XY (в кривых координатах);
	# здесь мы пока не учитываем начальные координаты пушки.
	vxold = B.VX 
	vyold = B.VY
	B.GetVelocities(v_max, dt)
	B.X = B.X + (vxold + B.VX)/2*dt # предиктор-корректор
	B.Y = B.Y + (vyold + B.VY)/2*dt
	xarray.append(B.X)
	yarray.append(B.Y)

# Переходим к полноценным (нормальным координатам).
rx = []
ry = []
rz = []

for i in range(len(yarray)):
	r = B.Rotate(xarray[i], yarray[i], 0, 45) # Поворачиваем точку из плоскости XY на угол 45°.
	rx.append(r[2] + B.X0) # И перемещаем точку траектории на начальные координаты пушки.
	ry.append(r[0] + B.Y0)
	rz.append(r[1])

# Получаем график траектории снаряда 
# для пушки, которая стреляет под углом 45° снарядом, массой 0.04 кг
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(rx, ry, rz)
plt.show()