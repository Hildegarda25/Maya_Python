#hamburguesa condicionales

import maya.cmds #Es la libreria de creacion de objetos
#Mayormente se usa para polyTorus - polySphere   
rad = 12
maya.cmds.polySphere(radius=rad,sa=10,sh=10)
maya.cmds.move(0,14,0)
maya.cmds.scale(1,0.75,1)#Escala el tamaño del objeto
maya.cmds.select('.vtx[30:39]')#Seleciona los vertices
maya.cmds.move(0,14,0)

import maya.cmds as mc #Es la libreria para creacion de objetos
#Mayormente se usa para polyPlane - polyCylinder
mc.polyCylinder(r=6.5,h=1.8,sc=0)
mc.move(-1.86,13.1,-6.5)
mc.polyCylinder(r=6.5,h=1.8,sc=0,sa=10)
mc.move(6.85,13.1,2.30)
mc.polyCylinder(r=6.5,h=1.8,sc=0,sa=10)
mc.move(-4.77,13.1,5.42)

cmds.polyCube(sx=8,sz=8,h=0.8,w=25,d=25)
cmds.move(0,11.80,0)

maya.cmds.polyTorus(r=11,sr=3,sa=20,sh=8)
#El polyTorus es un objeto en forma de aro
maya.cmds.move(0,8.5,0)

import maya.cmds 
rad = 12
maya.cmds.polySphere(radius=rad,sa=10,sh=10)
maya.cmds.move(0,5,0)
maya.cmds.scale(1,0.518,1)
maya.cmds.select('.vtx[50:59]')
maya.cmds.move(0,5,0)

cmds.polyCube(sx=8,sz=8,h=0.8,w=24,d=24)
cmds.move(0,5.25,0)
