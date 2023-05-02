

def shoelace_formula(polygonBoundary, absoluteValue = True): #defines and the calculation for finding the area of an polygonal based room.
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    l = [(polygonBoundary[i+1][0] - polygonBoundary[i][0]) * (polygonBoundary[i+1][1] + polygonBoundary[i][1]) for i in range(nbSegment)]#run the shoelace formula on given pionts

    if absoluteValue:
        return abs(sum(l) / 2.) 
             #returns results of formula for use in the program. 
    else:
        return sum(l) / 2.
        

polygonBoundary = []
hight=float(input("what is the hight of your room in metres?")) #takes the hight of the room
con=int(input("how many pionts do you have")) #takes how many pionts to give to the shoelace formula
print("please enter the x and y co-ordinates in metres of the pionts of the room you wish to find the area of with the first piont being 0,0 ")#explains how to give x and y of pionts.

for x in range(con):   
    polygonBoundary.append((int(input("enter x")),int(input("enter y"))))#takes the x and y values for the pionts to be used in the shoelace formula
walls=(float(input("please entre the length of the walls of the room ")))*(hight)#finds the area of the walls   
paint=walls/6.5#converts the area of the walls from metres to litres
Area=shoelace_formula(polygonBoundary)#finds the area of the polygonal room
volume=Area*hight#finds the volume 
print(polygonBoundary)#returns the pionts(for checking)
print("area is",Area,"m^2")#returns area
print("volume is",volume,"m^3")#returns volume
print(paint,"litres of paint required to cover walls")#returns paint required to cover walls
