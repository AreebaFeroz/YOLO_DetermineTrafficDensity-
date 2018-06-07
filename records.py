from kivy.uix.screenmanager import Screen, SlideTransition

from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior



import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.properties import ListProperty, StringProperty, BooleanProperty



import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()

            # for bar graph 1
def queryDB(fetchAttr, areaID, roadID):
    query = "SELECT " + fetchAttr + " FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(
        roadID) + " ORDER BY ID DESC LIMIT 2"
    cursor.execute(query)
    record = cursor.fetchone()
    return record[0]

                    # for bar graph 2, bar graph 3, pie chart of average densities and traffic flow
def queryDB1(fetchAttr, areaID, roadID):
    value = 0
    query = "SELECT " + fetchAttr + "  FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(roadID)
    cursor.execute(query)
    datatable = [row[0] for row in cursor.fetchall()]
    for m in range(0, len(datatable)):
        value += datatable[m]
    if (fetchAttr=='congestion' or fetchAttr=='density' or fetchAttr=='trafficFlow'):
        value = value / len(datatable)
        return value
    else:
        return value

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


                        ####### BAR GRAPH ########

                              ########## BAR CHART 1: CURRENT NO OF VEHICLES ##########
    def drawBarGraph1(self):

        post_id1 = queryDB('count',1, 0)
        x1 = [1] #road 1
        y1 = [post_id1]

        post_id2 = queryDB('count', 1, 1)
        x2 = [2] # road 2
        y2 = [post_id2]

        post_id3 = queryDB('count', 1, 2)
        x3 = [3] #road 3
        y3 = [post_id3]

        post_id4 = queryDB('count', 1, 3)
        x4 = [4] # road 4
        y4 = [post_id4]

        plt.bar(x1, y1, label="Road 1", color='r')
        plt.bar(x2, y2, label="Road 2", color='c')
        plt.bar(x3, y3, label="Road 3", color='y')
        plt.bar(x4, y4, label="Road 4", color='g')

        plt.xlabel('Road no')
        plt.ylabel('No of vehicles')
        plt.title('Bar Chart Graph\nNo of vehicles on each road(CURRENT)')
        plt.legend()
        plt.show()

                                   ######  BAR CHART 2 : TOTAL NO OF VEHICLES #####
    def drawBarGraph2(self):

        post_id1 = queryDB1('count',1, 0)
        x1 = [1] #road 1
        y1 = [post_id1]

        post_id2 = queryDB1('count', 1, 1)
        x2 = [2] # road 2
        y2 = [post_id2]

        post_id3 = queryDB1('count', 1, 2)
        x3 = [3] #road 3
        y3 = [post_id3]

        post_id4 = queryDB1('count', 1, 3)
        x4 = [4] # road 4
        y4 = [post_id4]

        plt.bar(x1, y1, label="Road 1", color='r')
        plt.bar(x2, y2, label="Road 2", color='c')
        plt.bar(x3, y3, label="Road 3", color='y')
        plt.bar(x4, y4, label="Road 4", color='g')

        plt.xlabel('Road')
        plt.ylabel('No of Vehicles')
        plt.title('Bar Chart Graph\nNo of vehicles on each road(TOTAL)')
        plt.legend()
        plt.show()

                        ######  BAR CHART 3: Average Congestion Time #####

    def drawBarGraph3(self):


        post_id1 = queryDB1('congestion',1, 0)
        x1 = [1] #road 1
        y1 = [post_id1]

        post_id2 = queryDB1('congestion', 1, 1)
        x2 = [2] # road 2
        y2 = [post_id2]

        post_id3 = queryDB1('congestion', 1, 2)
        x3 = [3] #road 3
        y3 = [post_id3]

        post_id4 = queryDB1('congestion', 1, 3)
        x4 = [4] # road 4
        y4 = [post_id4]

        plt.bar(x1, y1, label="Road 1", color='r')
        plt.bar(x2, y2, label="Road 2", color='c')
        plt.bar(x3, y3, label="Road 3", color='y')
        plt.bar(x4, y4, label="Road 4", color='g')

        plt.xlabel('Road')
        plt.ylabel('Congestion Time')
        plt.title('Bar Chart Graph\nAverage Waiting Time faced by Vehicles')
        plt.legend()
        plt.show()


                  ############## Pie charts #############

                    ######## PIE CHART: AVERAGE DENSITIES  OR AVERAGE TRAFFIC FLOW ########

    def drawPieGraph(self,  colName):

        x = [5]
        post_id1 = queryDB1(colName,1,0)

        post_id2 = queryDB1(colName,1,1)

        post_id3 = queryDB1(colName,1,2)

        post_id4 = queryDB1(colName,1,3)


        slices= [post_id1,post_id2,post_id3,post_id4]
        mylabels= ['Road 1','Road 2','Road 3','Road 4']
        cols= ['c','y','r','b']
        plt.pie(slices, labels= mylabels, colors=cols, startangle=90,shadow=True,autopct='%1.1f%%')

        if(colName=='density'):
            plt.title('Pie Chart Graph\n Average Densities of Vehicles on each road')
        else:
            plt.title('Pie Chart Graph\n Average Traffic Flow on each road')
        plt.show()

      ############# LINE GRAPHS ##################

            ############### LINE GRAPH 1

    def drawLineGraph1(self,attr1,attr2,attr3):


         y = []

         def queryDB2(fetchAttr, areaID, roadID):
             query = "SELECT "+ fetchAttr +"  FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(roadID) + " LIMIT 15"
             cursor.execute(query)
             datatable = [row[0] for row in cursor.fetchall()]
             for m in range(0,15):
               y.append(datatable[m])

         fig = plt.figure()
         ax = fig.gca(projection='3d')
         x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15]
         queryDB2(attr1,attr2,attr3)
         z = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

         plt.title('Line Graph\n')
         ax.plot(x, y, z, label='Duration of GREEN signal on road')
         plt.xlabel('X-axis (No of records=15)')
         plt.ylabel('Y-axis (Congestion Time)')

         ax.legend()

         plt.show()


                 ############ DROP DOWN ##################


class MenuItem(Widget):
    background_color_normal = ListProperty([0.2, 0.2, 0.2, 1])
    background_color_down = ListProperty([0.3, 0.3, 0.3, 1])
    background_color = ListProperty([])
    separator_color = ListProperty([0.8, 0.8, 0.8, 1])
    text_color = ListProperty([1,1,1,1])
    inside_group = BooleanProperty(False)
    pass

class MenuSubmenu(MenuItem, Spinner):
    triangle = ListProperty()

    def __init__(self, **kwargs):
        self.list_menu_item = []
        super().__init__(**kwargs)
        self.dropdown_cls = MenuDropDown

    def add_widget(self, item):
        self.list_menu_item.append(item)
        self.show_submenu()

    def show_submenu(self):
        self.clear_widgets()
        for item in self.list_menu_item:
            item.inside_group = True
            self._dropdown.add_widget(item)

    def _build_dropdown(self, *largs):
        if self._dropdown:
            self._dropdown.unbind(on_dismiss=self._toggle_dropdown)
            self._dropdown.dismiss()
            self._dropdown = None
        self._dropdown = self.dropdown_cls()
        self._dropdown.bind(on_dismiss=self._toggle_dropdown)

    def _update_dropdown(self, *largs):
        pass

    def _toggle_dropdown(self, *largs):
        self.is_open = not self.is_open
        ddn = self._dropdown
        ddn.size_hint_x = None
        if not ddn.container:
            return
        children = ddn.container.children
        if children:
            ddn.width = max(self.width, max(c.width for c in children))
        else:
            ddn.width = self.width
        for item in children:
            item.size_hint_y = None
            item.height = max([self.height, 48])

    def clear_widgets(self):
        self._dropdown.clear_widgets()

class MenuDropDown(DropDown):
        pass

class MenuButton(MenuItem,Button):
    icon = StringProperty(None, allownone=True)
    pass

class MenuEmptySpace(MenuItem):
    pass

class MenuBar(BoxLayout):

    background_color = ListProperty([0.2, 0.2, 0.2, 1])
    separator_color = ListProperty([0.8, 0.8, 0.8, 1])

    def __init__(self, **kwargs):
        self.itemsList = []
        super().__init__(**kwargs)

    def add_widget(self, item, index=0):
        if not isinstance(item, MenuItem):
            raise TypeError("MenuBar accepts only MenuItem widgets")
        super().add_widget(item, index)
        if index == 0:
            index = len(self.itemsList)
        self.itemsList.insert(index, item)


