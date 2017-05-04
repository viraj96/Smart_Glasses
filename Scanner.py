from PIL import Image
import numpy as np
import cv2
import os

def main():

        #Canny Edge Detection
        image = cv2.imread('/home/pi/Desktop/Scanner/image.jpg')
        image_gray = cv2.imread('/home/pi/Desktop/Scanner/image.jpg', 0)
        image_edges = cv2.Canny(image_gray.copy(), 10, 150)


        #Close Image Structure
        kernel = np.ones((5,5),np.uint8)
        closed = cv2.morphologyEx(image_edges, cv2.MORPH_CLOSE, kernel)

        #Find and Draw Image Contour
        contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
                #Contour Approximation
                epsilon = 0.02 * cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, epsilon, True)


                if len(approx) == 4:
                        cv2.drawContours(image, [approx], -1, (255, 0, 0), 3)

                        copy = np.vstack(approx)

                        coordinate = np.zeros((4,2), dtype = "float32")
                        sum = copy.sum(axis = 1)
                        coordinate[0] = copy[np.argmin(sum)]
                        coordinate[2] = copy[np.argmax(sum)]

                        diff = np.diff(copy,axis = 1)
                        coordinate[1] = copy[np.argmin(diff)]
                        coordinate[3] = copy[np.argmax(diff)]



        #Prespective Transform
        points_old = coordinate
        points_new = np.float32([[0,0], [550,0], [550, 450], [0,450]])
        transform = cv2.getPerspectiveTransform(points_old, points_new)
        transform_apply = cv2.warpPerspective(image_gray.copy(),transform, (550,450))


        #Adaptive Gaussian Threshold
        threshold = cv2.adaptiveThreshold(transform_apply, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)


        #Display images
        cv2.imshow('Scanned Image', threshold)
        cv2.imshow('Original Image', image)
        cv2.imwrite('/home/pi/Desktop/Scanner/image_scan.jpg', threshold)
        cv2.waitKey(0)
        cv2.destroyAllWindows


        #Save Scanned Image as PDF      
        infile = '/home/pi/Desktop/Scanner/image_scan.jpg'
        outfile = os.path.splitext(infile)[0] + ".pdf"
        Image.open(infile).save(outfile)


main()