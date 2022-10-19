import cv2
import numpy as np
import time

colors = [
    (  6,  7,  7),
    ( 31,  7,  7),
    ( 47, 15,  7),
    ( 71, 15,  7),
    ( 87, 23,  7),
    (103, 31,  7),
    (119, 31,  7),
    (143, 39,  7),
    (159, 47,  7),
    (175, 63,  7),
    (191, 71,  7),
    (199, 71,  7),
    (223, 79,  7),
    (223, 87,  7),
    (223, 87,  7),
    (215, 95,  7),
    (215, 95,  7),
    (215,103, 15),
    (207,111, 15),
    (207,119, 15),
    (207,127, 15),
    (207,135, 23),
    (199,135, 23),
    (199,143, 23),
    (199,151, 31),
    (191,159, 31),
    (191,159, 31),
    (191,167, 39),
    (191,167, 39),
    (191,175, 47),
    (183,175, 47),
    (183,183, 47),
    (183,183, 55),
    (207,207,111),
    (223,223,159),
    (239,239,199),
    (255,255,255),]

def semaforo():
    cap = cv2.VideoCapture('./Docs/PDF/Materiais_opencv/traffic_light.mp4')

    # Definindo ranges para detectar amarelo
    lower_range_g = (70, 0, 255)
    upper_range_g = (90,255, 255)

    lower_range_y = (20, 0, 255)
    upper_range_y = (40,255, 255)

    lower_range_r = (0, 0, 255)
    upper_range_r = (10, 255, 255)

    kernel = np.ones((3, 3))
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Aplicando inRange para obter mascara
        mask_g = cv2.inRange(frame_hsv, lower_range_g, upper_range_g)
        mask_y = cv2.inRange(frame_hsv, lower_range_y, upper_range_y)
        mask_r = cv2.inRange(frame_hsv, lower_range_r, upper_range_r)
        # mask_g = cv2.dilate(mask_g,kernel, iterations=10)
        # mask_y = cv2.dilate(mask_y,kernel, iterations=10)
        # mask_r = cv2.dilate(mask_r,kernel, iterations=10)

        current_state = "| "
        if mask_g.sum() > 100000:
            current_state += "green |"
        if mask_y.sum() > 100000:
            print(mask_y.sum(), mask_r.sum())
            current_state += "yellow |"
        if mask_r.sum() > 100000:
            current_state += "red |"

        cv2.putText(frame, current_state, (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1)
        # Resultados
        cv2.imshow('Imagem original', cv2.resize(frame, None, fx=0.5, fy=0.5))
        cv2.imshow('g', cv2.resize(mask_g, None, fx=0.5, fy=0.5))
        cv2.imshow('y', cv2.resize(mask_y, None, fx=0.5, fy=0.5))
        cv2.imshow("r", cv2.resize(mask_r, None, fx=0.5, fy=0.5))

        key = cv2.waitKey(100)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()

def contarArroz():
     #carregando imagem original
    img = cv2.imread('./Docs/PDF/Materiais_opencv/arroz.bmp')

    img = cv2.resize(img, None, fx=0.3, fy=0.3)
    
    kernel = np.ones((3,3))
    #Definindo ranges para detectar amarelo
    lower_range = (34,49,208)
    upper_range  = (255,255,255)

    #aplixando inrange para obter mascara
    mask = cv2.inRange(img, lower_range, upper_range)

    c, h = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    img_copy = img.copy()
    cont = 0
    for cnts in c:
        (x,y,w,h) = cv2.boundingRect(cnts)
        #Desenha linha em volta do pac man
        cv2.rectangle(img_copy, (x,y), (x+w, y+h), (0,255,0), 2, cv2.LINE_AA)
        cont = cont + 1
    
    cv2.putText(img_copy, 'quantidade de Arroz: ' + str(cont), (15, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 1)
    cv2.imshow('Contorno', img_copy)
   

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Chamas():

    array = (256,256,3)
    array = np.zeros(array, dtype=np.uint8)

    for c in range(256):
        array[256, c] = colors[-1]

    while True:
        for c in range(236):
            for i in range(256):
                array[-c - 20,i] = colors[9]
                cv2.imshow('chamas', array)
            cv2.waitKey(1)
        key = cv2.waitKey(0)
        if key == ord("q"):
            break
    cv2.destroyAllWindows()
    
def main():
    Chamas()

if(__name__ == "__main__"):
    main()