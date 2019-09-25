# -*- coding: UTF-8 -*-
import cv2
import numpy as np

# XML padrão da biblioteca openCV , serve como base para localizar faces
# esse XML é apenas uum arquivo que contem dados para detecção de faces
# cascadeClassifier carrega os dados na memoria para usar 
face_cascade = cv2.CascadeClassifier('opencv/cascades/data/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    #converte cada pixel para uma escala de cinza onde varia de branco de alta intensidade, até preto de menor intensidade
    # e vira um array gigante
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,scaleFactor=1.5,minNeighbors=5)
   
    # apos ter localizado a face, retorna 4 valor x e y == localização onde ficara o retangulo
    # w e h == largura e altura do retangulo 
   
    for (x,y,w,h) in faces:
        # # roi_gray = gray[y:y+h,x:x+w]
        # print("\nESSE È O ROI GRAYYY  : ", gray[y:y+h,x:x+w])
        # # roi_color = frame[y:y+h,x:x+w] 
        # img_item ="my-image.jpg"
        # utiliza uma imagem para facilitar a identificação da face 
        # cv2.imwrite(img_item,roi_gray)
        color = (255,0,0)
        thickness = 2
        width = x + w
        height = y + h
        #desenha um retangulo utilizando largura altura e as posições x, y 
        cv2.rectangle(frame,(x,y),(width,height),color,thickness)
    cv2.imshow('frame',frame)
    #função waitkey função que pode delimitar um tempo para dar quit na tela 
    #nesse caso é utilizado uma letra pra fechar o software
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


cap.release()
#destroi as janelas abertas apos execução do programa
cv2.destroyAllWindows()

