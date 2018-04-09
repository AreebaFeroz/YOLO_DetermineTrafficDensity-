import cv2
from darkflow.net.build import TFNet
import matplotlib.pyplot as plt


# define the model options and run
"""
options = {
    'model': 'C:/Users/areeba feroz/Documents/MyFiles/fyp/darkflow-master/darkflow-master/cfg/yolo.cfg',
    'load': 'C:/Users/areeba feroz/Documents/MyFiles/fyp/darkflow-master/darkflow-master/bin/yolov2.weights',
    'threshold': 0.3,
}"""
options = {
    'model': 'cfg/yolo.cfg',
    'load': 'bin/yolov2.weights',
    'threshold': 0.3

}
tfnet = TFNet(options)
# read the color image and covert to RGB


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

        if(label == 'bicycle' or label == 'car' or label == 'motorbike' or label == 'bus' or label == 'truck' or label=='person'):
            realCount+=1
            # add the box and label and display it
            img = cv2.rectangle(img, tl, br, (0, 255, 0), 7)
            img = cv2.putText(img, label, tl, cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 0), 2)

    print(realCount)
    plt.imshow(img)
    plt.show()
    return realCount;


img2Path = 'C:/Users/areeba feroz/Documents/MyFiles/fyp/darkflow-master/test2/sample_img/1.jpg'
img1Path = 'C:/Users/areeba feroz/Documents/MyFiles/fyp/darkflow-master/test2/sample_img/4.jpg'

img1Count = countVehicles(img1Path);
img2Count = countVehicles(img2Path);

