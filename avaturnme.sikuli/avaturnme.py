import os
import shutil
import time
from lackey import *
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
            time.sleep(2)
            # click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image2.png"))
            type(Key.ENTER)
            # click(Region(1956,661,103,46))
        
            click(Region(1681,345,181,286))
            time.sleep(2)
            # click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image0.png"))
            type(Key.ENTER)
            # click(Region(1956,661,103,46))
            
            click(Region(1857,329,220,286))
            time.sleep(2)
            # click(Region(1107,636,858,41))
            paste(os.path.join(cwd, "images", name, "image1.png"))
            type(Key.ENTER)
            # click(Region(1956,661,103,46))
        
            
         
        
        
            
        
            click(find(r"avaturnme.sikuli\male_icon.PNG"))
            click(Region(1626,1260,281,107))
            time.sleep(45)
        
            
            click(find(r"avaturnme.sikuli\download_icon.png"))
            click(find(r"avaturnme.sikuli\avatar_icon.png"))

            time.sleep(2)
            paste(os.path.join(cwd, "charactors", name,  "model.glb"))
            type(Key.ENTER)       
            time.sleep(10)    
            click(find(r"avaturnme.sikuli\x_icon.png"))
            click(find(r"avaturnme.sikuli\back_icon.png"))
        
            # shutil.move(r"C:\Users\detio\Downloads\model.glb", os.path.join(cwd, "charactors", name,  "model.glb"))

   # r.click()