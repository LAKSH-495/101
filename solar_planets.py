import cv2
img=cv2.imread("C:\\Users\\Admin\\Desktop\\DESKTOP\\LAKSH\\WHITEHAT JR\\PYTHON CODES\\P-104\\solar-system.jpg")
textshow1="SUN"
textshow2="MERCURY"
textshow3="VENUS"
textshow4="EARTH"
textshow5="MARS"
textshow6="JUPITER"
textshow7="SATURN"
textshow8="URANUS"
textshow9="NEPTUNE"
cv2.putText(img,textshow1,(20,220),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 1,color=(255,255,255))
cv2.putText(img,textshow2,(120,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow3,(200,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow4,(290,270),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow5,(390,260),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow6,(590,390),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow7,(770,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow8,(980,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.putText(img,textshow9,(1120,300),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale = 0.5,color=(255,255,255))
cv2.imshow("planets",img)
cv2.waitKey(0)