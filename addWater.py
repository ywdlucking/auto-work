import cv2 
import os 


path=input("请输入需要加水印的文件夹路径：")
file_list = os.listdir(path)
for filename in file_list:
    img1 = cv2.imread(path+filename,cv2.IMREAD_COLOR) 
    cv2.putText(img1,'YWD',(10,10) , 1, 1, (255,255,255),1)  #图片，文字，位置，字体，字号，颜色，厚度 
    cv2.imwrite(path+filename, img1)