import cv2
from darkflow.net.build import TFNet
import time
import random
import matplotlib.pyplot as plt
import sqlite3
import datetime



# define the model options and run
options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.1

}
tfnet = TFNet(options)
# read the color image and covert to RGB

def generateImageArray():
    img_data = []
    for x in range(0,4):
        randNo = random.randint(1, 15)
        imgPath = r"D:\Areeba\University\FYP\WORK\code\Count Code\YOLO_DetermineTrafficDensity--master\YOLO_DetermineTrafficDensity--master\sample_img\%s.jpg" % (randNo)
        img_data.append (imgPath)
        print(imgPath)
    return img_data

def countVehicles(imgPath):
    img = cv2.imread(imgPath,cv2.IMREAD_COLOR)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # use YOLO to predict the image
    result = tfnet.return_predict(img)
    count = len(result)
    """print(len(result))"""
    realCount=0
    for i in range(0,count):
        tl = (result[i]['topleft']['x'], result[i]['topleft']['y'])
        br = (result[i]['bottomright']['x'], result[i]['bottomright']['y'])
        label = result[i]['label']

        if(label == 'bicycle' or label == 'car' or label == 'motorbike' or label == 'bus' or label == 'truck' ):
            realCount+=1
            # add the box and label and display it
            img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
            img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    print("Number of vehicles in image")
    print(realCount)
    # plt.imshow(img)
    # time.sleep(5)
    # cv2.destroyAllWindows()
    # plt.show()
    return realCount;


def calDensity(count, length):
    return ((count * 1000) / length)


def calCongestion(time1, time2):
    return (time2.__sub__(time1)).seconds


def calTrafficFlow(count,greenDur):
    return (count/greenDur)


while True:
    w, h = 2, 4;
    density = [[0 for x in range(w)] for y in range(h)]

    img_data = generateImageArray()

    for x in range(0, 4):
        imgCountVar = countVehicles(img_data[x]);
        density[x][0] = imgCountVar;
        density[x][1] = x;
    print(density)
    density.sort(key=lambda x:x[0], reverse=True)
    #ask density is sorted??
    print(density)
    timeAllot = [0 for x in range(4)]

    db = sqlite3.connect("database.db")
    c = db.cursor()

    temp = 0
    for i in range(0,4):
        if(density[i][0] <= 3 ): timeAllot[i] = 30
        elif(density[i][0]>3 and density[i][0]<=5): timeAllot[i] = 60
        elif(density[i][0]>5) : timeAllot[i] = 120

        if not i is 0:
            temp =temp + timeAllot[i-1]
        if i is 0:
            dateTimeAllot = datetime.datetime.now()
        else:
            dateTimeAllot = datetime.datetime.now() + datetime.timedelta(0, temp)# days, seconds, then other fields.
        c.execute(
             "INSERT INTO density ('areaID', 'roadID', 'count','rec_time','density','congestion',"
             "'greenDur','trafficFlow') VALUES(1, ?, ?, ?, ?, ?, ?, ? )",
             (density[i][1], density[i][0], datetime.datetime.now(), calDensity(density[i][0], 2),
              calCongestion(datetime.datetime.now(), dateTimeAllot), timeAllot[i],calTrafficFlow(density[i][0], timeAllot[i])))

    db.commit()
    c.close()
    db.close()
    print(timeAllot)

    for i in range(0,4):
        print('Road No: ' + str(density[i][1]) + ' Go GREEN for '+ str(timeAllot[i]) + 'seconds')
        #time.sleep(timeAllot[i])


#img2Path = 'D:/FINAL YEAR PROJECT/darkflow-master/sample_img/1.jpg'
#img1Path = 'D:/FINAL YEAR PROJECT/darkflow-master/sample_img/2.jpg'


#for x in range(0,4):
#    imgCountVar = countVehicles(img_data[x]);
#    imgCount.append(imgCountVar)
  #  print(imgCount[x])
# img2Count = countVehicles(img2Path);



