import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, StringProperty

from plyer import gps

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    error = ObjectProperty(None, rebind=True)
    
    def button_clicked(self):
        if self.password.text == "hi":
            self.manager.switch_to(HomeScreen(username=self.username.text))
        else:
            self.error.text = "Login Failed. Try again."
            self.error.color = [1,0,0,1]


class HomeScreen(Screen):
    username = ''
    userDisplayName = ''
    
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        self.username = kwargs.get('username', "guest")
        self.userDisplayName = kwargs.get('username', "guest")
        super(HomeScreen, self).__init__(**kwargs)

class AidMeApp(App):
    gps_location = StringProperty('Location?', rebind=True)
    gps_status = StringProperty('Click Start to get GPS location updates', rebind=True)

    def build(self):
        self.gps = gps
        
        try:
            self.gps.configure(on_location=self.on_location,
                    on_status=self.on_status)
        except NotImplementedError:
            import traceback; traceback.print_exc()
            self.gps_status = 'GPS is not implemented for your platform'
        
        # Create the screen manager
        sm = ScreenManager(transition=FadeTransition())
        #sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home',username='bob'))
        return sm

    def on_location(self, **kwargs):
        self.gps_location = 'Location: \n'.join([
            '{}={}'.format(k, v) for k, v in kwargs.items()])

    def on_status(self, stype, status):
        self.gps_status = 'type={}\n{}'.format(stype, status)
    
if __name__ == '__main__':
    AidMeApp().run()

    