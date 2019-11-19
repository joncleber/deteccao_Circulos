import cv2
import numpy as np

img = cv2.imread('bubles1.jpg')

#cv2.imshow('mostra_img_carregada.jpg', img)

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,
                            param1=50,param2=30,minRadius=25,maxRadius=80)

circles = np.uint16(np.around(circles))
print(circles)
print(img.shape)

#contador = 0


# for i in circles[0,:]:
#     # draw the outer circle
#     cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
#     # draw the center of the circle
#     cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
#     contador = contador + 1

#print(contador)

#tracando linha
cont = 0
while cont < 410:
    img.itemset((cont, 300, 2), 255)
    img.itemset((cont, 300, 1), 0)
    img.itemset((cont, 300, 0), 0)
    cont = cont + 1

imagem_1 = img[0:410, 0:300]
cv2.imwrite("imagem_1.jpg", imagem_1)
gray = cv2.cvtColor(imagem_1,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,
                            param1=50,param2=30,minRadius=25,maxRadius=80)

circles = np.uint16(np.around(circles))

contador = 0


for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(imagem_1,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(imagem_1,(i[0],i[1]),2,(0,0,255),3)
    contador = contador + 1

print(contador)
largura = 50
altura = 50
fonte = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala = 2
grossura = 3
texto = '{}'.format(contador)
tamanho, _ = cv2.getTextSize(texto, fonte, escala, grossura)


cv2.putText(img, texto, (int(largura / 2 - tamanho[0] / 2), int(altura / 2 + tamanho[1] / 2)), fonte, escala, (0, 0, 0), grossura)
imagem_2 = img[0:410, 300:612]
cv2.imwrite("imagem_2.jpg", imagem_2)
cont_ = 0

gray = cv2.cvtColor(imagem_2,cv2.COLOR_BGR2GRAY)
blur = cv2.medianBlur(gray,5)

circles = cv2.HoughCircles(blur,cv2.HOUGH_GRADIENT,1,50,
                            param1=50,param2=30,minRadius=25,maxRadius=80)

circles = np.uint16(np.around(circles))

for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(imagem_2,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(imagem_2,(i[0],i[1]),2,(0,0,255),3)
    cont_ = cont_ + 1
print(cont_)

largura_2 = 1100
altura_2 = 50
fonte_2 = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
escala_2 = 2
grossura_2 = 3
texto_2 = '{}'.format(cont_)
tamanho_2, _ = cv2.getTextSize(texto_2, fonte_2, escala_2, grossura_2)

cv2.putText(img, texto_2, (int(largura_2 / 2 - tamanho_2[0] / 2), int(altura_2 / 2 + tamanho_2[1] / 2)), fonte_2, escala_2, (0, 0, 0), grossura_2)
#cv2.imshow('detected_circles_new',imagem_2)
cv2.imwrite('linha.jpg', img)
cv2.imshow("resultado", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
