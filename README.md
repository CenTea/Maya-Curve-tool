###############
# CPSC 305
# Mini-Project 10: Implementing your Custom Maya Tool
# Matthew Tea
###############

1. The tool has the ability to group items. When grouped, you are then able to clone the group over a selected curve.

2. How to use:

    When you have a set of object that you want to clone, select them.
    When the objects are selected, clicking the "group" button on the UI will
    create a group for the object set.
    After you have created a group, you can create or select a curve.
    When the curve is selected, moving the slider will increase or decrease
    the amount of cloned objects created. Click "OK" to create x amount of 
    objects in the shape of the curve.

    NOTE: Ensure that you do not delete the PasterGroup during use as it is
    hard coded. Also, subsequent PasterGroups, "PasterGroup1",
    "PasterGroup2"... etc created from other instances of the Paster 
    Tool can be safely deleted.
    Cloned groups will be labeled as "groupX"... etc where X is a number and
    each group will be holding a copy of the original group. These Cloned
    groups will reside under the PasterGroup created at initialization.
	
	
3. What you should see:

    After cloning the group of objects depending on the amount provided and
    the shape of the curve, the result you should see will range from a sparse
    placement of copies of your group in the formation of the curve (Which will
    seem random as the specified number was low.) or you will be able to 
    make out/distinctly identify the curve shape that was used (If the amount set
    was sufficiently high enough).
