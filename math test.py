import math



def piont_plotter(xg,yg):
    
    cordanates=[(0,0)]
    x=xg
    y=yg
    con=int(input("how many pionts do you have"))
    for x in range(con):   
        
        wall= float(input("please enter the lenght of the new wall"))
        theta= float(input("please entre the angle between the old and new wall to 1 dp"))

        if theta <= 90:
            if theta== 180:
                cha_y=0
            else:
                cha_y= (math.sin(math.radians(theta)))*wall

            if theta== 90 or theta == 270:
                cha_x=0
            else:
                cha_x= (math.cos(math.radians(theta)))*wall*-1


            print(cha_y,cha_x)
            x=x+cha_x
            y=y+cha_y
            cordanates.append((x,y))
            
        elif theta <= 180 and theta >90:
            theta = 180-theta
            if theta== 180:
                cha_y=0
            else:
                cha_y= (math.sin(math.radians(theta)))*wall

            if theta== 90 or theta == 270:
                cha_x=0
            else:
                cha_x= (math.cos(math.radians(theta)))*wall

            print(cha_y,cha_x)
            x=x+cha_x
            y=y+cha_y 
            cordanates.append((x,y))
            
        elif theta <= 270 and theta >180:
            theta= theta-180
            if theta== 180:
                cha_y=0
            else:
                cha_y= (math.sin(math.radians(theta)))*wall*-1

            if theta== 90 or theta == 270:
                cha_x=0
            else:
                cha_x= (math.cos(math.radians(theta)))*wall

            print(cha_y,cha_x)
            x=x+cha_x
            y=y+cha_y
            cordanates.append((x,y))
            
        elif theta <= 360 and theta >270:
            theta=360-theta
            if theta== 180:
                cha_y=0
            else:
                cha_y= (math.sin(math.radians(theta)))*wall*-1

            if theta== 90 or theta == 270:
                cha_x=0
            else:
                cha_x= (math.cos(math.radians(theta)))*wall*-1
            print(cha_y,cha_x)
            x=x+cha_x
            y=y+cha_y
            cordanates.append((x,y))
            
        else:
            print("please make sure you give an angle > 0 and <= 360")
            
    return cordanates

cordi = piont_plotter(0,0)
print(cordi)
    
    
