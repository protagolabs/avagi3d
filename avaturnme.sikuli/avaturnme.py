import os
import shutil
# while True:

names = os.listdir("images/")

for name in names:
    print(name)
    if not os.path.exists(os.path.join("charactors/", name)):
        os.makedirs(os.path.join("charactors/" + name))  
    click(Region(1025,834,214,171))
    click(Location(2018, 623))
    click(Location(1593, 461))
    click(Region(1365,713,171,45))
    click(Region(2092,512,38,49))
    paste("image2.jpeg")
    doubleClick(Region(1535,636,686,26))
    
    click(Region(1710,354,159,234))
    click(Region(1364,714,176,45))
    click(Region(2084,513,55,53))
    paste("image1.jpeg")
    doubleClick(Region(1536,638,683,24))
    
    click(Region(1905,343,163,245))
    click(Region(1367,715,168,39))
    click(Region(2077,510,70,58))
    paste("image0.jpeg")
    doubleClick(Region(1538,630,684,39))


    

    click(Location(1728, 853))
    click(Region(1670,1254,244,93))
    sleep(40)

    
    click(Region(1868,1304,54,63))
    click(Region(1406,510,368,254))

    
    sleep(10)    
    click(Region(2119,513,81,74))
    click(Region(1053,120,82,67))
    

    shutil.move("/home/xing.di/Downloads/model.glb", "/home/xing.di/Downloads/{}.glb".format(name))

    
   # r.click()