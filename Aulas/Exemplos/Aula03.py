import cv2
import numpy as np

def SegmentacaoDeCoresFunction():
    #carregando imagem original
    img = cv2.imread('./Docs/PDF/Materiais_opencv/pacman.jpg')

    img = cv2.resize(img, None, fx=0.3, fy=0.3)

    #Definindo ranges para detectar amarelo
    lower_range = (0,200,200)
    upper_range  = (50,255,255)

    #aplixando inrange para obter mascara
    mask = cv2.inRange(img, lower_range, upper_range)

    #Recorte segmentado
    segm = cv2.bitwise_and(img, img, mask=mask)
    
    #Resultados
    cv2.imshow("Imagem original", img)
    cv2.imshow("Imagem mascara de cor", mask)
    cv2.imshow("Imagem objeto segmentado", segm)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def SegmentacaoDeCoresFunctionVideoRGB():
    #carregando imagem original
    cap = cv2.VideoCapture('./Docs/PDF/Materiais_opencv/pacman.mp4')

    lower_range = (0,200,200)
    upper_range  = (50,255,255)

    while(True):
        ret, frame = cap.read()
        mask = cv2.inRange(frame, lower_range, upper_range)
        segm = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame1', frame)
        cv2.imshow('frame2', mask)
        cv2.imshow('frame3', segm)
        
        if cv2.waitKey(1000//30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def SegmentacaoDeCoresFunctionVideoHSV():
    #carregando imagem original
    cap = cv2.VideoCapture('./Docs/PDF/Materiais_opencv/pacman.mp4')

    lower_range = (20,210,255)
    upper_range  = (80,255,255)

    while(True):
        ret, frame = cap.read()
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(frame_hsv, lower_range, upper_range)
        segm = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow('frame1', frame)
        cv2.imshow('frame2', mask)
        cv2.imshow('frame3', segm)
        
        if cv2.waitKey(1000//30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def ContornosFunction():
     #carregando imagem original
    cap = cv2.VideoCapture('./Docs/PDF/Materiais_opencv/pacman.mp4')

    lower_range = (0,200,200)
    upper_range  = (50,255,255)

    while(True):
        ret, frame = cap.read()
        mask = cv2.inRange(frame, lower_range, upper_range)
        c, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.imshow('frame1', frame)
        img_copy = frame.copy()
        for cnts in c:
            (x,y,w,h) = cv2.boundingRect(cnts)
            x -= 10
            y -= 10
            w += 20
            h += 20
            cv2.rectangle(img_copy, (x,y), (x+w, y+h), (0,255,0), 2, cv2.LINE_AA)
        cv2.imshow('Contorno', img_copy)

        img_cut = frame[y:y+h, x:x+w]
        cv2.imshow('Recorte', img_cut)
        cv2.imshow('Mascara', mask)
        
        if cv2.waitKey(1000//30) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def main():
    ContornosFunction()

if(__name__ == "__main__"):
    main()