from hnzView import View
from hnzModel import Model
from tkinter import *
from pubsub import pub
class Controller:
    def __init__(self, parent):

        self.parent = parent
        self.model = Model()
        self.view = View(parent)
        self.view.setup()

        pub.subscribe(self.openfile_btn_pressed, "OpenFile_Button_Pressed")
        pub.subscribe(self.model_change_handler, "model_updated")
        pub.subscribe(self.line_detection,"LineDetect_Button_Pressed")



    def openfile_btn_pressed(self):
        #print ('controller receive message - OpenFile_Button_Pressed')
        self.model.loadImg()

    def model_change_handler(self, data):
        self.view.updateImg(data)

    def line_detection(self):
        self.model.lineDetection(self.view.scale1.get(), self.view.scale2.get(),self.view.scale3.get(),self.view.scale4.get())
        print ("control line detetection")


if __name__ == "__main__":
    # Create an instance of Tk. This is popularly called 'root' But let's
    # call it mainwin (the 'main window' of the application. )
    mainwin = Tk()
    WIDTH = 800
    HEIGHT = 800
    mainwin.geometry("%sx%s" % (WIDTH, HEIGHT))
    #mainwin.resizable(0, 0)
    mainwin.title("Image Line Detection")

    game_app = Controller(mainwin)

    mainwin.mainloop()