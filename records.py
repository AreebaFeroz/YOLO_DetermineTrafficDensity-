from kivy.uix.screenmanager import Screen, SlideTransition

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()


def queryDB(fetchAttr, areaID, roadID):
    query = "SELECT " + fetchAttr + " FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(
        roadID) + " ORDER BY ID DESC LIMIT 2"
    cursor.execute(query)
    record = cursor.fetchall()
    return record[0]



class SelectableRecycleGridLayout(FocusBehavior, LayoutSelectionBehavior,
                                  RecycleGridLayout):
    ''' Adds selection and focus behaviour to the view. '''


class SelectableButton(RecycleDataViewBehavior, Button):
    ''' Add selection support to the Button '''
"""   index = None
 selected = BooleanProperty(False)
 selectable = BooleanProperty(True)"""


class Records(Screen):

    data_items = ListProperty([])

    def __init__(self, **kwargs):
        super(Records, self).__init__(**kwargs)
        self.get_users()

    def get_users(self):

        cursor.execute("SELECT * FROM density")
        rows = cursor.fetchall()

        # create data_items
        for row in rows:
            for col in row:
                self.data_items.append(col)


    def RecordsBack(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

    def RecordsLogout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()


    def drawGraph(self):

        post_id1 = queryDB('count',1, 0)
        x = [1] #road 1
        y = [post_id1] #road id 1 wali density ki value yahan dalni h

        post_id2 = queryDB('count', 1, 1)
        x2 = [2] # road 2
        y2 = [post_id2]

        post_id3 = queryDB('count', 1, 2)
        x3 = [3] #road 3
        y3 = [post_id3]

        post_id4 = queryDB('count', 1, 3)
        x4 = [4] # road 4
        y4 = [post_id4]

        plt.bar(x, y, label="Road 1", color='r')
        plt.bar(x2, y2, label="Road 2", color='c')
        plt.bar(x3, y3, label="Road 3", color='y')
        plt.bar(x4, y4, label="Road 4", color='g')

        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Bar Chart Graph\nTotal no of vehicles on each road')
        plt.legend()
        plt.show()


    def drawGraph1(self):

        x = [5]
        post_id1 = queryDB('count',1, 0)

        road1 = [post_id1]

        post_id2 = queryDB('count', 1, 1)

        road2 = [post_id2]

        post_id3 = queryDB('count', 1, 2)

        road3 = [post_id3]

        post_id4 = queryDB('count', 1, 3)

        road4 = [post_id4]


        slices= [post_id1,post_id2,post_id3,post_id4]
        mylabels= ['Road 1','Road 2','Road 3','Road 4']
        cols= ['c','y','r','b']
        plt.pie(slices, labels= mylabels, colors=cols, startangle=90,shadow=True,autopct='%1.1f%%')


        plt.title('Pie Chart Graph\nMaximum No of vehicles')
        plt.show()


    def drawGraph2(self):

         y = []
         query = "SELECT count  FROM density WHERE areaID=1 AND roadID=0 LIMIT 15"
         cursor.execute(query)
         datatable = [row[0] for row in cursor.fetchall()]
         for m in range(0,15):
           y.append(datatable[m])

         fig = plt.figure()
         ax = fig.gca(projection='3d')
         x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
         #y = [5,6,3,13,4,1,2,4,8,5]
         z = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

         plt.title('Line Graph\n')

         ax.plot(x, y, z, label='Increasing No of vehicles on road 1')
         plt.xlabel('X-axis')
         plt.ylabel('Y-axis')

         ax.legend()

         plt.show()



















