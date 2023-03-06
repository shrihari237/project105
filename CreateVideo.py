import os 
import cv2

path = "D:/Python/Project105/Images"
Images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    
    
    if ext in ['.gif','.png','.jpg','.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)
        Images.append(file_name)
       
print(len(Images))
count = len(Images)
frame = cv2.imread(Images[0])
height,width,channels = frame.shape    

size = (width,height)
print(size)

out = cv2.VideoWriter('project.avi',cv2.VideoWriter_fourcc(*'DIVX'),0.5,size)

for i in range(0,count):
   frame =  cv2.imread(Images[i])
   out.write(frame)
   print("Hello")
out.release()   
print('Done')   


