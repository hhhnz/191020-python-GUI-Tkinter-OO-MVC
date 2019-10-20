from tkinter.filedialog import askopenfilename
import cv2
from pubsub import pub
import PIL.ImageTk, PIL.Image
import numpy as np

class Model:
    def __init__(self):

       
        return


    def loadImg(self):
        path= askopenfilename(initialdir="C:/Project/openCVProject/test image",
                       filetypes=[("Image File", "*.jpg"),("All Files","*.*")],
                        title = "Choose a file."
                        )
        
        if len(path)>0:
            self.originalImg = cv2.imread(path)
            self.currentImg = self.originalImg.copy()
            ##image = PIL.Image.fromarray(self.originalImg)#.resize(300,300)
            #update view image
            pub.sendMessage("model_updated", data=self.toTkImg(self.currentImg))

        print (path)
        return
        
    def getCurrentImg(self):
        return 
    def getOriginalImg(self):
        return self.originalImg
    def lineDetection(self,p,th,minlen,maxgap):
        img = self.originalImg.copy() #opencv img
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        #cv2.imshow('gray img',gray)
        #img_blur = cv2.medianBlur(gray, 5)
        #cv2.imshow('gray blur',img_blur)
        edges = cv2.Canny(gray, 50, 150, apertureSize = 3)
        #minLineLength - Minimum length of line. Line segments shorter than this are rejected
        #maxLineGap - Maximum allowed gap between line segments to treat them as single line
        lines = cv2.HoughLinesP(edges,p,np.pi/360,th,minlen,maxgap)
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
            #print (x1,y1,x2,y2)
        #update image
        #cv2.imshow('line detection',img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        self.currentImg=img
        pub.sendMessage("model_updated", data=self.toTkImg(self.currentImg))

    #convert cv2 image to tk image
    def toTkImg(self,img):
        #scale_percent = 3  # percent of original size
        #width = int(img.shape[1] * scale_percent)
        #height = int(img.shape[0] * scale_percent)
        #dim = (width, height)
        # resize image
        #resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        b,g,r = cv2.split(img)
        img = cv2.merge((r,g,b))
        im = PIL.Image.fromarray(img)
        imgtk = PIL.ImageTk.PhotoImage(image=im)
        return imgtk
