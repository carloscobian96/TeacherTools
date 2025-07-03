
def xyz_there(xyz):
    
    xyzArray = list(xyz)
    status =""
    status_of_xyz = ""
    
    for x in xyzArray:
      if(x == "x"):
        print(1)
        for w in xyzArray:
          if(xyzArray.index(x)+1 == xyzArray.index("y")):
            print(2)
            if(xyzArray.index("y")+1 == xyzArray.index("z")):
              print(3)
              status_of_xyz = "xyz together"
              for y in xyzArray:
                if(status != "Point in front") :
                  if(y == "."):
                    print(4)                 
                    for z in xyzArray:
                        if(xyzArray.index("x")-1 == xyzArray.index(".")):
                          print(5)                     
                          status = "Point in front"
                          break
                        else:
                          xyzArray.remove(".")                     
                          print(6)                    
                          status = "Point not in front"
                          break                  
                  else:
                    print(7)
                    status = "Point not in front"
          else:   
            xyzArray.remove("x")
  
    if(status_of_xyz =="xyz together"):
     if(status == "Point not in front" ):
       print(True)
     elif(status =="Point in front"):
        print(False)
    else:
     print(False)
             
xyz_there("")
            

      










    
    

        
 