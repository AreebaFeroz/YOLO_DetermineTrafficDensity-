from kivy.uix.screenmanager import Screen, SlideTransition
import sqlite3

db= sqlite3.connect("database.db")
c=db.cursor()
db.row_factory = lambda c, row: row[0]

def queryDB(fetchAttr,areaID,roadID):
    query = "SELECT " + fetchAttr + " FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(roadID) +" ORDER BY ID DESC LIMIT 1"
    c.execute(query)
    record = c.fetchone()
    return str(record[0])

def calculateHeaviestFlow(count,timeSec):
    return ((count * 3600)/timeSec)

def saveHeaviestFlow(timePeriod, heavFlow,areaID,roadID):
    c.execute(
        "INSERT INTO heaviestFlow ('areaID', 'roadID', 'period','trafficFlow') VALUES(?, ?, ?, ? )",
        (areaID, roadID, timePeriod, heavFlow))
    db.commit()


def queryForFlow(areaID,roadID):
    max_time = ""
    min_time = ""
    ch = True
    hvFlow = 0.0
    counter = 1
    time = 2350
    while True:
        query = "SELECT count,greenDur,rec_time FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(roadID) + " ORDER BY ID DESC LIMIT "+str(counter)
        chkQuery ="SELECT COUNT(ID) FROM density WHERE areaID=" + str(areaID) + " AND roadID=" + str(roadID)
        c.execute(chkQuery)
        cnt = list(c.fetchone())
        #print(cnt)
        if(counter.__gt__(cnt[0])):
            ch=False
            break

        c.execute(query)
        record = list(c.fetchall())

        totalDur = 0
        totalCount = 0
        for records in record:
            if(counter==1):
                max_time = records[2]
            min_time = records[2]
            totalCount =totalCount + records[0]
            totalDur =totalDur + records[1]
        #print(counter)


        if (int(totalDur).__ge__(time)):
            hvFlow = calculateHeaviestFlow(totalCount, time)
            saveHeaviestFlow(min_time+ " To "+max_time,calculateHeaviestFlow(totalCount,time),areaID,roadID)
            break;
        counter = counter.__add__(1)
    if(ch is False):
        return "not possible(less data record)"
    else:
        return str(hvFlow)




class Options(Screen):

    def on_enter(self, *args):
        self.ids['my_label'].text = ""

    def optionsBack(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'connected'
        self.manager.get_screen('connected')

    def optionsLogout(self):
        self.manager.transition = SlideTransition(direction="right")
        self.manager.current = 'login'
        self.manager.get_screen('login').resetForm()

    def showCount(self):
        count = ""
        for rid in range(0, 4):
            count = count + "\nTotal vehicles on road no. " + str(rid) + " is " + queryDB('count', 1, rid)
        self.ids['my_label'].text = count

    def showDensity(self):
        density = ""
        for rid in range(0,4):
            density  = density +  "\n Density of road no. " + str(rid) + " is " + queryDB('density',1,rid)+ " vehicles/km"
        self.ids['my_label'].text = density


    def showTrafficFlow(self):
        trafficFlow = ""
        for rid in range(0, 4):
            trafficFlow = trafficFlow + "\n Traffic flow on road no. " + str(rid) + " is " + str(round(float(queryDB('trafficFlow', 1, rid)),4)) + " vehicles/seconds"
        self.ids['my_label'].text = trafficFlow


    def showGreenDur(self):
        greenDur = ""
        for rid in range(0, 4):
            greenDur = greenDur + "\n GO GREEN on road no. " + str(rid) + " for " + queryDB('greenDur', 1, rid) + " seconds"
        self.ids['my_label'].text = greenDur


    def showCongestion(self):
        congestion = ""
        for rid in range(0, 4):
            resCong = queryDB('congestion', 1, rid)
            if(resCong == "86399.0"):
                resCong = 0
            congestion = congestion + "\n Congestion period on road no. " + str(rid) + " is " + str(resCong) + " seconds"
        self.ids['my_label'].text = congestion


    def showHeaviestFlow(self):
        heaviestFlow = ""
        for rid in range(0,4):
            heaviestFlow =  heaviestFlow + "\nThe heaviest flow for road no. " +str(rid) + " is " + queryForFlow(1,rid)
        self.ids['my_label'].text = heaviestFlow

