#lampara
def poligonos(cil,con,tor,cub):
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(0,-2.27,0)
    mc.scale(11.73,0.15,11.072)    
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(-10,cil[1]/2,0)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(-8,cil[1]/2,-6)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(-0.05,cil[1]/2,-10)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(8,cil[1]/2,6)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(8,cil[1]/2,-6)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(10,cil[1]/2,0)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(0,cil[1]/2,10)
    
    mc.polyCylinder(n=cil[3],r=cil[0],
    h=cil[1],sa=cil[2])
    mc.move(-8,cil[1]/2,6)
      
    mc.polyCone(n=con[3],r=con[0],
    h=con[1],sa=con[2])
    mc.move(0,20,0)  
    mc.scale(1.1,0.27,1)
    
    mc.polyCone(n=con[3],r=con[0],
    h=con[1],sa=con[2])
    mc.move(0,-2.30,0)  
    mc.scale(1.161,0.27,1.1)
    mc.rotate(0,0,180)
    
    mc.polyTorus(n=tor[4],r=tor[0],
    sr=tor[1],sa=tor[2],sh=tor[3])
    mc.move(0,1.4,0)
    
    mc.polyCube(n=cub[3],w=cub[0],
    h=cub[1],d=cub[2])   
    mc.move(0,4,0)
    mc.scale(0.55,1,0.55)
    mc.select('.vtx[2:5]')
    mc.move(0,15,0)
  
    mc.polyCube(n=cub[3],w=cub[0],
    h=cub[1],d=cub[2])   
    mc.move(0,4,0)
    mc.scale(0.55,1,0.55)
    
    
datos = {'cil':[1,18,5,'cilindro_mesh'],
         'con':[10,16,8,'cono_mesh'],
         'tor':[6,2,18,8,'torus_mesh'],
         'cub':[8,8,8,'cubo_mesh']
         }
         
poligonos(**datos) 


#cerco
import maya.cmds as mc
import random
altura=random.randint(30,40)
print(altura)

limite=5
contador=0
while contador < limite:
    contador +=1
    rAlt = random.randint(16,19)
    mc.polyCube(w=6,h=rAlt,d=2,sw=2)
    rDist=random.randint(1,3)
    mc.move(contador*15+rDist,float(rAlt)/2,0)
    
mc.select('pCube1.vtx[4]','pCube1.vtx[7]')
mc.move(0,4,0,r=True)

mc.select('pCube2.vtx[4]','pCube2.vtx[7]')
mc.move(0,4,0,r=True)

mc.select('pCube3.vtx[4]','pCube3.vtx[7]')
mc.move(0,4,0,r=True)

mc.select('pCube4.vtx[4]','pCube4.vtx[7]')
mc.move(0,4,0,r=True)

mc.select('pCube5.vtx[4]','pCube5.vtx[7]')
mc.move(0,4,0,r=True)

cafe.polyCube(h=2,w=3,d=70)
cafe.rotate(-180,90,0)
cafe.move(46.35,3.98,0)

cafe.polyCube(h=2,w=3,d=70)
cafe.rotate(-180,90,0)
cafe.move(46.35,12.12,0)

#bicicleta
import maya.cmds
rad=5
maya.cmds.polyTorus(r=rad,sa=20,sh=8)
maya.cmds.rotate(90,0,0)
maya.cmds.move(5,5.5,0)

rad=5
maya.cmds.polyTorus(r=rad,sa=20,sh=8)
maya.cmds.rotate(90,0,0)
maya.cmds.move(-12,5.5,0)

import maya.cmds as mc
mc.polyCylinder(r=4.5,h=0.5,sc=1)
mc.rotate(90,0,0)
mc.move(5,5.5,0)

mc.polyCylinder(r=4.5,h=0.5,sc=1)
mc.rotate(90,0,0)
mc.move(-12,5.5,0)
#-----------------------

mc.polyCylinder(r=0.3,h=6,sc=1,sh=3)
mc.rotate(0,0,-15)
mc.move(-11.2,8.5,0.8)

mc.polyCylinder(r=0.3,h=6,sc=1,sh=3)
mc.rotate(0,0,-15)
mc.move(-11.2,8.5,-0.8)
#----------------------

mc.polyCylinder(r=0.3,h=2.20,sc=1,sa=3)
mc.rotate(90,0,0)
mc.move(-12,5.5,0)
#-----------------------

mc.polyCylinder(r=0.4,h=1,sc=1,sh=3)
mc.rotate(0,0,-15)
mc.move(-10.37,11.6,0.8)

mc.polyCylinder(r=0.4,h=1,sc=1,sh=3)
mc.rotate(0,0,-15)
mc.move(-10.37,11.6,-0.8)

#----------------------
import maya.cmds as cafe
cafe.polyCube(h=1,w=0.5,d=0.5)
cafe.rotate(90,0,-15)
cafe.move(-10.37,11.6,0)

#-----------------  
mc.polyCylinder(r=0.3,h=5.5,sc=1,sh=3)
mc.rotate(0,0,-15)
mc.move(-9.6,14.4,0)

#------------------
import maya.cmds as cafe
cafe.polyCube(h=1,w=0.5,d=0.5)
cafe.rotate(90,0,-15)
cafe.move(-8.923,17,0)

#-----------------

mc.polyCylinder(r=0.35,h=1,sc=1,sh=3)
mc.rotate(90,0,0)
mc.move(-8.923,17,0)

mc.polyCylinder(r=0.3,h=3,sc=1,sh=3)
mc.rotate(90,0,0)
mc.move(-8.923,17,1.85)

mc.polyCylinder(r=0.3,h=3,sc=1,sh=3)
mc.rotate(90,0,0)
mc.move(-8.923,17,-1.85)

#-------------
import maya.cmds as mc
mc.polyCylinder(r=0.3,h=6.5,sc=1,sh=3)
mc.rotate(0,0,38.174)
mc.move(-8,10.3,0)

mc.polyCylinder(r=0.3,h=4.5,sc=1,sh=3)
mc.rotate(0,0,90)
mc.move(-3.976,7.857,0)

mc.polyCylinder(r=0.3,h=10.5,sc=1,sh=3)
mc.rotate(0,0,164)
mc.move(-1.441,9.28,0)

#------------------- 

mc.polyCylinder(r=0.3,h=2.9,sc=1,sh=3)
mc.rotate(90,0,-15)
mc.move(-2.891,4.234,0)

mc.polyCylinder(r=0.3,h=2,sc=1,sh=3)
mc.rotate(0,0,164)
mc.move(-2.693,3.56,1.45)

mc.polyCylinder(r=0.3,h=2,sc=1,sh=3)
mc.rotate(0,0,164)
mc.move(-2.693,4.908,-1.45)

#-------------------

mc.polyCylinder(r=2,h=0.2,sc=1,sh=2)
mc.rotate(90,0,0)
mc.move(-2.889,4.234,-0.91)

mc.polyCylinder(r=2.05,h=0.08,sc=1,sh=1)
mc.rotate(90,0,0)
mc.move(-2.889,4.234,-0.91)

mc.polyCylinder(r=0.3,h=2.1,sc=1,sh=3)
mc.rotate(90,0,-15)
mc.move(-2.419,5.868,-2.2)

mc.polyCylinder(r=0.3,h=2.1,sc=1,sh=3)
mc.rotate(90,0,-15)
mc.move(-3.368,2.598,2.202)

#---------------- --

mc.polyCylinder(r=0.1,h=8,sc=1,sh=4)
mc.rotate(0,0,-80.635)
mc.move(1.192,4.896,0.695)

mc.polyCylinder(r=0.1,h=8,sc=1,sh=4)
mc.rotate(0,0,-80.635)
mc.move(1.192,4.896,-0.695)

mc.polyCylinder(r=0.15,h=8,sc=1,sh=5)
mc.rotate(0,0,-131.947)
mc.move(2.05,8.2,0.695)

mc.polyCylinder(r=0.15,h=8,sc=1,sh=5)
mc.rotate(0,0,-131.947)
mc.move(2.05,8.2,-0.695)


import maya.cmds as cafe
cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,0)
cafe.move(5,5.499,0)


cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,-15.505)
cafe.move(-0.989,10.838,0)
cafe.scale(1.186,0.936,1.186)

cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,0)
cafe.move(5,5.499,-0.572)
cafe.scale(1,0.514,1)

# silla
cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,-13.788)
cafe.move(-0.056,14.518,0)
cafe.scale(3.344,1,1)

cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,4.579)
cafe.move(-1.285,14.671,0)
cafe.scale(1.991,1,1)

cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,8.794)
cafe.move(-2.139,14.575,0)
cafe.scale(1.525,1,1)

cafe.polyCube(h=1.8,w=0.5,d=0.5)
cafe.rotate(90,0,12.146)
cafe.move(-2.875,14.44,0)
cafe.scale(1.525,1,1)