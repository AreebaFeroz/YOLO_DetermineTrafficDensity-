  #first stop resizable window
from kivy.config import Config
Config.set('graphics','resizable',False)

  #create App window
from kivy.app import App
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition


from kivy.core.window import Window
from kivy.base import EventLoop;


from connected import Connected
from options import Options
from records import Records
from live import Live

Window.clearcolor = (1, 1, 0, 1)  #background color

Window.size = 950,650         # window size
#Window.set_title('Vision Based Traffic Light Control')
#EventLoop.window.title = 'Vision Based Traffic Light Control'


class Login(Screen):


    def do_login(self):

        app = App.get_running_app()

        mypassword = ObjectProperty()


        app.password = self.mypassword.text

        print(app.password)

        if (app.password=='admin'):
            self.manager.transition = SlideTransition(direction="left")
            self.manager.current = 'live'
            self.manager.get_screen('login').resetForm()

            #app.config.read(app.get_application_config())
            #app.config.write()
        else:
            self.ids['label1'].text = "Incorrect password"
            self.ids['password'].text = ""
            self.manager.get_screen('login').resetForm()


    def resetForm(self):
        self.ids['login'].text = "admin"
        self.ids['password'].text = ""
        self.ids['password'].focus = True

class LoginApp(App):
    username = StringProperty(None)
    password = StringProperty(None)

    App.title = 'Vision Based Traffic Light Control'

    def build(self):
        manager = ScreenManager()


        manager.add_widget(Login(name='login'))
        manager.add_widget(Connected(name='connected'))
        manager.add_widget(Options(name='options'))
        manager.add_widget(Records(name='records'))
        manager.add_widget(Live(name='live'))

        return manager

"""
    def get_application_config(self):
        if(not self.username):
            return super(LoginApp, self).get_application_config()

        conf_directory = self.user_data_dir + '/' + self.username

        if(not os.path.exists(conf_directory)):
            os.makedirs(conf_directory)

        return super(LoginApp, self).get_application_config(
            '%s/config.cfg' % (conf_directory)
        )
"""
if __name__ == '__main__':
    LoginApp().run()