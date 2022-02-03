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