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
