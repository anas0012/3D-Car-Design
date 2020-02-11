import maya.cmds as cmds

def tire_creation_function(tx, ty, tz, rx, ry, rz, sx, sy, sz, i):
    cmds.polyCylinder(name="car_tire_0{}".format(str(i)))
    cmds.setAttr('car_tire_0{}.t'.format(str(i)), tx, ty, tz, type='double3')
    cmds.setAttr('car_tire_0{}.r'.format(str(i)), rx, ry, rz, type='double3')
    cmds.setAttr('car_tire_0{}.s'.format(str(i)), sx, sy, sz, type='double3')



if __name__ == "__main__":
    tire_creation_function(3,1,3,90,90,0,0.7,0.2,0.7,1)




