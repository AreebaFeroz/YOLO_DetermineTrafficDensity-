from kivy.uix.screenmanager import Screen, SlideTransition


class Live(Screen):

    def goToConnected(self):
        self.manager.transition = SlideTransition(direction="left")
        self.manager.current = 'connected'

