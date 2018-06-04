from kivy.uix.screenmanager import Screen, SlideTransition
# import time
# import random
# from kivy.clock import Clock
# from kivy.properties import ObjectProperty
# import cv2
# from darkflow.net.build import TFNet

# options = {
#     'model': 'cfg/yolo.cfg',
#     'load': 'bin/yolov2.weights',
#     'threshold': 0.3
#
# }
# tfnet = TFNet(options)
# # read the color image and covert to RGB
#
# def generateImageArray():
#     img_data = []
#     for x in range(0,4):
#         randNo = random.randint(1, 15)
#         imgPath =  r"D:\Areeba\University\FYP\WORK\code\Count Code\YOLO_DetermineTrafficDensity--master\YOLO_DetermineTrafficDensity--master\sample_img\%s.jpg" %(randNo)
#         img_data.append (imgPath)
#         print(imgPath)
#     return img_data
#
# def countVehicles(imgPath):
#     img = cv2.imread(imgPath,cv2.IMREAD_COLOR)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#
#     # use YOLO to predict the image
#     result = tfnet.return_predict(img)
#     count = len(result)
#     """print(len(result))"""
#     realCount=0
#     for i in range(0,count):
#         tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
#         br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
#         label = result[i]['label']
#
#         if(label == 'bicycle' or label == 'car' or label == 'motorbike' or label == 'bus' or label == 'truck' ):
#             realCount+=1
#             # add the box and label and display it
#             img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
#             img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)
#
#     print("Number of vehicles in image 1 and image 2 respectively")
#     print(realCount)
#     return realCount;


imgpath = 'interface-images/trafficlight14.jpg'
class Connected(Screen):
    def disconnect(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def clickOptions(self):

        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'options'

    def showRecords(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'records'

    def showImg(self):
        #self.ids.image.source = imgpath
       pass

#     def on_enter(self, *args):
# #        self.streeta = imgpath
#     #    Clock.schedule_interval(self., 1.0 / 60.0)
#         w, h = 2, 4;
#         density = [[0 for x in range(w)] for y in range(h)]
#
#         img_data = ObjectProperty()
#         img_data = generateImageArray()
#
#         self.streeta = img_data[0]
#         self.streetb = img_data[1]
#         self.streetc = img_data[2]
#         self.streetd = img_data[3]
#
#
#
#         for x in range(0, 4):
#             imgCountVar = countVehicles(img_data[x]);
#             density[x][0] = imgCountVar;
#             density[x][1] = x;
#         print(density)
#         density.sort(key=lambda x: x[0], reverse=True)
#         print(density)
#         timeAllot = [0 for x in range(4)]
#
#         for i in range(0, 4):
#             if (density[i][0] <= 3):
#                 timeAllot[i] = 5
#             elif (density[i][0] > 3 and density[i][0] <= 5):
#                 timeAllot[i] = 15
#             elif (density[i][0] > 5):
#                 timeAllot[i] = 30
#         print(timeAllot)
#
#         for i in range(0, 4):
#             print('Road No: ' + str(density[i][1]) + ' Go GREEN for ' + str(timeAllot[i]) + 'seconds')
#             time.sleep(timeAllot[i])
