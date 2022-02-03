import maya.cmds as cafe
cafe.polyCube(h=2,w=41,d=3)
 
def tabla(name,alt,ubic):
    mc.polyCube(n=name,w=1,h=alt,d=15,sx=2,sy=2,sz=02)
    mc.move(ubic,alt/2,8)

tabla('ddd',1,0)
tabla('fff',1,2)    
tabla('ggg',1,4)   
tabla('aaa',1,6)
tabla('www',1,8)    
tabla('qqq',1,10)
tabla('ddd',1,12)
tabla('fff',1,14)    
tabla('ggg',1,16)
tabla('fff',1,18)    
tabla('ggg',1,20)
