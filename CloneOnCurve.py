# CSUF CPSC 305
# Mini-Project 10
#
# Group Members:
#   Matthew Tea

import maya.cmds as cmds

class Paster:
    def __init__(self):#constructor
        self.windowName = 'Paster'
      	f = cmds.group(n='PasterGroup', em=True)
        if cmds.window(self.windowName, exists=True):
            cmds.deleteUI(self.windowName)
        win = cmds.window(self.windowName, title='Paster', widthHeight=(400, 100))
        cmds.rowColumnLayout( numberOfColumns=3, adjustableColumn = 2)
        cmds.text(label= 'Number of Objects')
        SLD = cmds.intSlider(min=0,max=100,value=5,step=1)
        cmds.button(label='OK', command = lambda *x:self.ok(SLD))
        cmds.text(label='Grab')
        cmds.button(label='Group', command = self.grab)
        cmds.showWindow(win)
       
    def grab(self,*args):
        self.f = cmds.group(cmds.ls(selection = True), parent = 'PasterGroup')
    # Callback, called when user clicks Ok.
    def ok(self, obj,*args):
        n = cmds.intSlider(obj,value=True, query = True)#Query slider
        z = cmds.ls(selection = True) #Line Selection
        for i in range(0,n): #From i to N
            x = cmds.pointOnCurve(z,pr=float(i)/float(n), turnOnPercentage = True)
            y = cmds.duplicate(self.f) #place Group
            cmds.move( x[0], x[1], x[2], y[0], absolute = True) #Move Group to point
 
w = Paster()
