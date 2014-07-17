import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty, StringProperty

from parse_rest.datatypes import Object
from parse_rest.connection import register
from parse_rest.user import User

class LoginScreen(Screen):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    error = ObjectProperty(None, rebind=True)
    
    def login_button(self):
        u = User.login(self.username.text, self.password.text)

        if u.is_authenticated():
            self.manager.switch_to(HomeScreen(username=self.username.text))
        else:
            self.error.text = "Login Failed. Try again."
            self.error.color = [1,0,0,1]

    def signup_button(self):
        u = User.signup(self.username.text, self.password.text)
        self.error.text = "User created successfully. Please Login."
        self.error.color = [0,1,0,1]

class HomeScreen(Screen):
    username = ''
    userDisplayName = ''
    
    def __init__(self, **kwargs):
        # make sure we aren't overriding any important functionality
        self.username = kwargs.get('username', "guest")
        self.userDisplayName = kwargs.get('username', "guest")
        super(HomeScreen, self).__init__(**kwargs)

class SettingsScreen(Screen):
    pass
        
class ProfileScreen(Screen):
    pass
        
class AchievementScreen(Screen):
    pass
        
class LeaderBoardScreen(Screen):
    pass
        
class WaterBoardScreen(Screen):
    pass
        
class RecyclingScreen(Screen):
    pass
        
class ElectricityScreen(Screen):
    pass
        
class FuelScreen(Screen):
    pass

class GreenUpApp(App):
    def build(self):
        register('jeV1sPLXL6cq8EsWAK0Zyoac8b97duQWyXYK7sfE','fl6hQ9dv94IbtA0I7kPzSrawL165HqupSjCFdo3D')
        
        # Create the screen manager
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(LoginScreen(name='login'))
        sm.add_widget(HomeScreen(name='home',username='bob'))
        # sm.add_widget(SettingsScreen(name='settings'))
        # sm.add_widget(ProfileScreen(name='profile'))
        # sm.add_widget(AchievementScreen(name='achievement'))
        # sm.add_widget(LeaderBoardScreen(name='leader'))
        # sm.add_widget(WaterScreen(name='water'))
        # sm.add_widget(RecyclingScreen(name='recycling'))
        # sm.add_widget(ElectricityScreen(name='electric'))
        # sm.add_widget(FuelScreen(name='fuel'))
        return sm

    def on_pause(self):
        # Here you can save data if needed
        return True

    def on_resume(self):
        # Here you can check if any data needs replacing (usually nothing)
        pass


if __name__ == '__main__':
    GreenUpApp().run()
