import os
import cv2

path = "Images/"
images= []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file
        print(file_name)  
        images.append(file_name)

count= len(images)
frame= cv2.imread(images[0])
height,width,size = frame.shape
size= width,height

friend = cv2.VideoWriter("friend.mp4",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for i in range(0,count-1):
    image=cv2.imread(images[i])
    friend.write(image)

friend.release()
print("done")