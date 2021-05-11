import pandas as pd
import numpy as np
import argparse
import cv2

b=g=r=xpos=ypos= 0
clicked=False

ap = argparse.ArgumentParser()
ap.add_argument('-i', '--image', required=True, help="Image Path")
args = vars(ap.parse_args())
img_path = args['image']

img = cv2.imread(img_path)

title=["color","color_name","hex","R","G","B"]
data = pd.read_csv('colors.csv',names=title,header=None)

def draw_fun(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b,g,r,xpos,ypos, clicked
        clicked = True
        xpos,ypos = x,y
        b,g,r = img[y,x]
        b = int(b)
        g = int(g)
        r = int(r)
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(data)):
        d = abs(R- int(data.loc[i,"R"])) + abs(G- int(data.loc[i,"G"]))+ abs(B- int(data.loc[i,"B"]))
        if(d<minimum):
            minimum = d
            cname = data.loc[i,"color_name"]
    return cname

cv2.namedWindow("picture")
cv2.setMouseCallback("picture",draw_fun)


while(1): #continue showing the image until esc 
    cv2.imshow("picture",img)
    if(clicked):
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text=getColorName(r,g,b) + ' R='+ str(r) + ' G='+ str(g) + ' B='+ str(b)

        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.7,(0,0,0),2,cv2.LINE_AA)  #black
        else:
            cv2.putText(img, text,(50,50),2,0.7,(255,255,255),2,cv2.LINE_AA) #white
        
        clicked=False
    if cv2.waitKey(20) & 0xFF ==27:
        break
cv2.destroyAllWindows()

#run using:python3 color.py -i path.jpeg