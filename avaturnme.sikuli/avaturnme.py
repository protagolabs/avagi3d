import os
import shutil
import time
# while True:

names = os.listdir("images/")
cnames = os.listdir("charactors/")
cwd = os.getcwd()

while True:
    selected_names = [x for x in names if not x in cnames]
    if selected_names:
        
        for name in selected_names:
            print(name)
            if not os.path.exists(os.path.join("charactors/", name)):
                os.makedirs(os.path.join("charactors/" + name))  
            click(Region(1057,872,89,116))
            click(Region(1761,286,493,696))
            click(Region(1465,347,197,278))
            click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image0.png"))
            click(Region(1956,661,103,46))
        
            click(Region(1681,345,181,286))
            click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image1.png"))
            click(Region(1956,661,103,46))
            
            click(Region(1857,329,220,286))
            click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image2.png"))
            click(Region(1956,661,103,46))
        
            
         
        
        
            
        
            click(Region(1553,836,292,57))
            click(Region(1626,1260,281,107))
            sleep(45)
        
            
            click(Region(1840,1304,80,81))
            click(Region(1394,556,307,174))
        
            
            sleep(10)    
            click(Region(2099,513,74,100))
            click(Region(991,109,62,103))
        
            shutil.move(r"C:\Users\detio\Downloads\model.glb", os.path.join(cwd, "charactors", name,  name+".glb"))

   # r.click()