import sys
import os
import numpy as np
import cv2
#from adjust_gamma import adjust_gamma


def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")

	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)

img= cv2.imread(f"/home/crossfire/Downloads/gate dete/gate2.png")
img1=img.copy()
img2=img.copy()
b,g,r=cv2.split(img2)
b2,g2,r2= cv2.split(img)
b1,g1,r1=cv2.split(img1)
imdb = ((b2.max()-b2.min())/2) + b2.min()


alpha=0.9
b[b<imdb]=imdb
for index,value in np.ndenumerate( b ):
   new_value=((255* (value-imdb))/ ((b2.max()-b2.min())/(alpha**2)))
   b[index]= new_value
print(b.shape)
#print(b1.shape)
imdg = ((g2.max()-g2.min())/2) + g2.min()
g[g<imdg]=imdg
for index,value in np.ndenumerate(g):
    new_value=((255* (value-imdg))/((g2.max()-g2.min())*(alpha**2)))
    g[index]= new_value
print(g.shape)

imdr = ((r2.max()-r2.min())/2) + r2.min()
r[r<imdr]=imdr
for index,value in np.ndenumerate(r):
    new_value=((255* (value-imdr))/ ((r2.max()-r2.min())/(alpha**2)))
    r[index]= new_value
print(r.shape)
b1[b1>imdb]=imdb
for index,value in np.ndenumerate( b1 ):
    new_value=((255* (value-b2.min()))/ ((b2.max()-b2.min())*(alpha**2)))
    b1[index]= new_value
print(b1.shape)
#print(b1.shape)

g1[g1>imdg]=imdg
for index,value in np.ndenumerate(g1):
   new_value=((255* (value-g2.min()))/((g2.max()-g2.min())*(alpha**2)))
   g1[index]= new_value
print(g1.shape)

imdr = ((r2.max()-r2.min())/2) + r.min()
r1[r1>imdr]=imdr
for index,value in np.ndenumerate(r1):
    new_value=((255* (value-r2.min()))/ ((r2.max()-r2.min())*(alpha**2)))
    r1[index]=new_value
print(r.shape)
res=cv2.merge((b,g,r))
res1=cv2.merge((b1,g1,r1))
res2= cv2.addWeighted(res,.5,res1,.5,0)

cv2.imshow("",res)
cv2.imshow("1",res1)
cv2.imshow("2",img2)
cv2.imshow("avg",res2)
fin= adjust_gamma(res2,1.2)
cv2.imshow("final",fin)


cv2.waitKey(0)
cv2.destroyAllWindows()
